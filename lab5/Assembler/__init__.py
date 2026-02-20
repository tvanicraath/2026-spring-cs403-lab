from .pass1 import Pass1Assembler, AssemblerError
from .pass2 import Pass2Assembler

class Assembler:
    """Main Assembler class that orchestrates Pass 1 and Pass 2."""
    def __init__(self, source_file, target_file):
        self.source_file = source_file
        self.target_file = target_file
        self.start_addr = 0
        self.program_length = 0
        self.program_name = ""
    
    @property
    def _intermediate_file(self):
        return self.source_file + ".pass1"

    def assemble(self):
        """Runs the full assembly process."""
        # --- Pass 1 ---
        with open(self.source_file, 'r') as source_file, open(self._intermediate_file, 'w') as target_file:
            pass1_assembler = Pass1Assembler(source_file, target_file)
            pass1_assembler.run()
            self.start_addr = pass1_assembler.start_addr
            self.program_length = pass1_assembler.program_length
            self.program_name = pass1_assembler.program_name
        
        # --- Pass 2 ---
        with open(self._intermediate_file, 'r') as intermediate_file, open(self.target_file, 'w') as obj_file:
            pass2_assembler = Pass2Assembler(intermediate_file, obj_file, self.program_name, self.start_addr, self.program_length)
            pass2_assembler.run()
        
        # self.cleanup()
    
    def cleanup(self):
        """Removes intermediate files."""
        import os
        if os.path.exists(self._intermediate_file):
            os.remove(self._intermediate_file)