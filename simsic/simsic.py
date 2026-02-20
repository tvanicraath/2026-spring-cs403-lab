import sys
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

OPTAB = { 0x00: 'LDA', 0x0C: 'STA', 0x10: 'STX', 0x14: 'STL',
    0x04: 'LDX', 0x08: 'LDL', 0x48: 'JSUB', 0x4C: 'RSUB',
    0x28: 'COMP', 0x30: 'JEQ', 0x38: 'JLT', 0x3C: 'J', 0x34: 'JGT',
    0x18: 'ADD', 0x1C: 'SUB', 0x20: 'MUL', 0x24: 'DIV',
    0x2C: 'TIX',
    0x50: 'LDCH', 0x54: 'STCH', 0xE0: 'TD', 0xD8: 'RD', 0xDC: 'WD'}
MAX_MEM = 1<<15  # 32KB Memory
instructions_limit = 100000 # Prevent infinite loops

class SICSimulatorError(Exception):
    pass


class SICSimulator:
    def __init__(self, obj_fpath: str):
        self.A = 0     # Accumulator
        self.X = 0     # Index Register
        self.L = 0     # Linkage Register
        self.PC = 0    # Program Counter
        self.SW = 0    # Status Word (Condition Code: < -1, = 0, > 1)
        self.memory = bytearray(MAX_MEM)  # 32KB Memory
        self._start_address = 0
        self._program_len = 0
        with open(obj_fpath, 'r') as obj_code:
            self.load(obj_code)
        
    def print_state(self):
        print(f"\n{'-'*60}\nFINAL STATE.... PC: {hex(self.PC)}, A: {hex(self.A)}, X: {hex(self.X)}, L: {hex(self.L)}, SW: {self.SW}\n{'-'*60}")

    @property
    def _end_address(self):
        return (self._start_address + self._program_len) % MAX_MEM

    def load(self, obj_code) -> None:
        """Loads an object file into memory."""
        for line in obj_code:
            line = line.strip()
            if not line: 
                continue
            record_type = line[0]

            if record_type == 'H':
                # H Name(6) Start(6) Length(6)
                start_addr = int(line[7:13], 16)
                self._start_address = start_addr
                self._program_len = int(line[13:19], 16)
                # self.PC is usually set by E record
                logger.info(f"Header: Program starts at {hex(start_addr)}")
                
            elif record_type == 'T':
                # T Start(6) Length(2) Mask(2-optional) Data(...)
                start_addr = int(line[1:7], 16)
                length = int(line[7:9], 16)
                data_hex = line[9:]
                
                # Load bytes into memory
                for i in range(length):
                    byte_val = int(data_hex[2*i : 2*i+2], 16)
                    self.memory[start_addr + i] = byte_val
                    logger.debug(f"Loaded byte {hex(byte_val)} at {hex(start_addr + i)}")
                    
            elif record_type == 'E':
                    # E StartAddr(6)
                    if len(line) > 1:
                        self.PC = int(line[1:7], 16)
                    logger.info(f"End: Execution begins at {hex(self.PC)}")

    def get_word(self, addr):
        """Reads a 3-byte word from memory."""
        first, second, third = addr % MAX_MEM, (addr+1) % MAX_MEM, (addr+2) % MAX_MEM
        return (self.memory[first] << 16) | (self.memory[second] << 8) | self.memory[third]

    def set_word(self, addr, val):
        """Writes a 3-byte word to memory."""
        val = val & 0xFFFFFF # Mask to 24 bits
        first, second, third = addr % MAX_MEM, (addr+1) % MAX_MEM, (addr+2) % MAX_MEM
        self.memory[first] = (val >> 16) & 0xFF
        self.memory[second] = (val >> 8) & 0xFF
        self.memory[third] = val & 0xFF
    
    @staticmethod
    def decode(instruction) -> tuple[str, bool, int]:
        """Decodes instruction bytes into (mnemonic, indexed, address)."""
        op = (instruction & 0xFF0000) >> 16
        mnemonic = OPTAB[op]
        indexed = (instruction & 0x008000) >> 15
        addr = instruction & 0x007FFF   
        return mnemonic, indexed, addr
        

    def step(self):
        """Fetch-Decode-Execute Cycle"""
        if self.PC >= self._end_address:
            logger.debug(f"PC {hex(self.PC)} out of program bounds. Halting execution.")
            self.running = False
            return

        # Format: | OP (8) | X (1) | Address (15) |
        # 1. Fetch
        instruction = self.get_word(self.PC)
        logger.debug(f"Fetched instruction {hex(instruction)} from PC: {hex(self.PC)}")

        # 2. Decode
        mnemonic, indexed, target_addr = self.decode(instruction)
        effective_addr = target_addr + self.X if indexed else target_addr
        logger.debug(f"Decoded instruction: {mnemonic}, Effective Address: {hex(effective_addr)}")
    
        # Advance PC immediately
        self.PC += 3

        # --- Execute ---
        # Data Movement
        if mnemonic == 'LDA':
            self.A = self.get_word(effective_addr)
            # Handle 24-bit signed numbers
            if self.A & 0x800000: self.A -= 0x1000000
        elif mnemonic == 'LDX':
            self.X = self.get_word(effective_addr)
        elif mnemonic == 'LDL':
            self.L = self.get_word(effective_addr)
        elif mnemonic == 'STA':
            self.set_word(effective_addr, self.A)
        elif mnemonic == 'STX':
            self.set_word(effective_addr, self.X)
        elif mnemonic == 'STL':
            self.set_word(effective_addr, self.L)
        
        # Byte Handling
        elif mnemonic == 'LDCH':
            # Loads byte into rightmost 8 bits of A
            byte_val = self.memory[effective_addr]
            self.A = (self.A & 0xFFFF00) | byte_val
        elif mnemonic == 'STCH':
            # Stores rightmost 8 bits of A
            byte_val = self.A & 0xFF
            self.memory[effective_addr] = byte_val
            
        # Arithmetic
        elif mnemonic == 'ADD':
            val = self.get_word(effective_addr)
            if val & 0x800000: val -= 0x1000000 # Sign extend
            self.A += val
            self.A &= 0xFFFFFF # Keep 24 bits
        elif mnemonic == 'SUB':
            val = self.get_word(effective_addr)
            if val & 0x800000: val -= 0x1000000
            self.A -= val
            self.A &= 0xFFFFFF
        elif mnemonic == 'MUL':
            val = self.get_word(effective_addr)
            if val & 0x800000: val -= 0x1000000
            self.A *= val
            self.A &= 0xFFFFFF
        elif mnemonic == 'DIV':
            val = self.get_word(effective_addr)
            if val == 0:
                print("Runtime Error: Division by Zero")
                self.running = False
                return
            if val & 0x800000: val -= 0x1000000
            # SIC DIV result goes to A, Remainder discarded (Std SIC behavior)
            self.A //= val 
            self.A &= 0xFFFFFF

        # Control Flow
        elif mnemonic == 'COMP':
            val = self.get_word(effective_addr)
            if val & 0x800000: val -= 0x1000000
            # Compare A with Memory
            # We treat A as signed 24-bit
            curr_a = self.A
            if curr_a & 0x800000: curr_a -= 0x1000000
            
            if curr_a < val: self.SW = -1
            elif curr_a == val: self.SW = 0
            else: self.SW = 1
            
        elif mnemonic == 'J':
            if self.PC-3 == effective_addr:
                self.running = False
                logger.debug("Infinite Loop Detected: Jumping to same PC. Treating it as program end.")
                return
            self.PC = effective_addr
        elif mnemonic == 'JEQ':
            if self.SW == 0: self.PC = effective_addr
        elif mnemonic == 'JLT':
            if self.SW == -1: self.PC = effective_addr
        elif mnemonic == 'JGT':
            if self.SW == 1: self.PC = effective_addr
        elif mnemonic == 'JSUB':
            self.L = self.PC
            self.PC = effective_addr
        elif mnemonic == 'RSUB':
            self.PC = self.L
        
        # increment
        elif mnemonic == 'TIX':
            self.X += 1
            self.X &= 0xFFFFFF
            val = self.get_word(effective_addr)
            if val & 0x800000: val -= 0x1000000
            # Compare X with Memory
            curr_x = self.X
            if curr_x & 0x800000: curr_x -= 0x1000000
            
            if curr_x < val: self.SW = -1
            elif curr_x == val: self.SW = 0
            else: self.SW = 1

        # I/O Devices
        elif mnemonic == 'TD':
            # Test Device: Always return < (Ready) for simulation simplicity
            self.SW = -1 
        elif mnemonic == 'RD':
            # Read 1 byte from stdin (Device 00)
            # Blocks until input available
            char = sys.stdin.read(1)
            if not char:
                val = 0 # EOF
            else:
                val = ord(char)
            self.A = (self.A & 0xFFFF00) | val
        elif mnemonic == 'WD':
            # Write 1 byte to stdout (Device 01)
            val = self.A & 0xFF
            sys.stdout.write(chr(val))
            sys.stdout.flush()

    def run_program(self):
        self.running = True
        count = 0
        
        while self.running and count < instructions_limit:
            self.step()
            count += 1
            
        if count >= instructions_limit:
            print("\n[Simulator] Limit Exceeded (Infinite Loop?)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 simsic.py <object_file.obj>")
        sys.exit(1)

    sim = SICSimulator(sys.argv[1])
    sim.run_program()
    sim.print_state()