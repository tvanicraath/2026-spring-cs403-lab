# Lab 5: Assembler - Pass 2

In Lab 4, we implemented **Pass 1** of the Assembler, which scanned the source code, assigned addresses to instructions using the Location Counter (`LOCCTR`), and populated SymTab and LitTab.
In this lab, we will implement **Pass 2** to convert those mnemonics and labels into the hexadecimal machine code that the SIC simulator can actually execute.
We have also included a simple SIC simulator as a submodule in this repo, so you can test your generated object code directly.
For simplicity, 
- Assume that there is no instruction-block appearing after reservation directives (`RESW`/`RESB`) and literals.
- Assume that the code will end with an infinite loop (for e.g. `HALT    J       HALT`).

## Goal

The primary goal of Pass 2 is to translate the **Intermediate File** (generated in Lab 4) into an **Object Program** (`.obj`) that follows the SIC standard format.
Execute this by the SIC simulator.

## Object File Format (SIC Standard)

The assembler must generate records in the following standard format.
The helper methods for writing these records are provided in `pass2.py`, but you must implement the logic to determine when and how to write them.

- **Header Record (`H`)**. Describes the program name, starting address, and total length. `H<PROGRAM_NAME>  <START_ADDR><LENGTH>`, where `PROGRAM_NAME` is left-justified and padded to 6 characters, and `START_ADDR` and `LENGTH` are 6-digit hex values.
- **Text Record (`T`)**. Contains the actual machine code. A text record can hold a maximum of 30 bytes (60 hex characters) of object code. `T<START_ADDR><LENGTH><OBJECT_CODE...>`, where `START_ADDR` is the address of the first byte in the record, `LENGTH` is the number of bytes in the record, and `OBJECT_CODE` is the concatenated hex string of machine code.
- **End Record (`E`)**. Marks the end of the program and specifies the address of the first executable instruction. `E<FIRST_INSTRUCTION_ADDR>`, where `FIRST_INSTRUCTION_ADDR` is a 6-digit hex value.
---

## Task Breakdown

Read the intermediate object file, say, `1.asm.pass1`, line by line and proceed as follows.


### 1. Instruction Assembly

For each executable instruction (e.g., `LDA ALPHA`), you must:

1. **Lookup Opcode:** Use your C library bindings (`bindings.search_optab`) to get the opcode (e.g., `LDA` -> `00`).
2. **Lookup Operand:** Use `bindings.search_symbol` (or your Python `littab`) to find the address of the operand (e.g., `ALPHA` -> `1003`).
3. **Combine:** Concatenate them to form the instruction: `001003`.
* *Note:* If the opcode is `RSUB`, the operand is usually `0000`.



### 2. Handling Directives

* **BYTE:** Convert the constant to its hex representation (e.g., `C'EOF'` -> `454F46`).
* **WORD:** Convert the integer to a 6-digit hex string (e.g., `WORD 10` -> `00000A`).
* **RESW / RESB:** Do **not** generate any object code. These directives simply reserve space.
* *Important:* These directives break the current Text Record. You must close the current record and start a new one at the next valid instruction address.



### 3. Buffering Text Records

You cannot write a Text Record immediately. You must "buffer" the object codes in a list or string.
Only write the record to the file when:

1. The buffer length exceeds 30 bytes (60 hex chars).
2. A `RESW`/`RESB` is encountered.
3. The program ends.

---

## Verification: Simulating the Machine

Since we are building system software, we need hardware to test it. 
Unfortunately, we don't have a real SIC machine in this world, but we can use a simulator to verify that our assembler is generating correct object code.
After generating the object file (`output.obj`), simulate it:
```bash
python simsic.py output.obj
```

## Further Exploration
Since the Assembler is now complete, you may experiment with writing your own SIC assembly programs and assembling them using your assembler.
If brave, implement simple sorting algorithms (e.g., Bubble Sort) in SIC assembly and test them on the simulator.
If not, ask your LLM assistant to generate some sample SIC assembly programs for you to test.
Ensure that they do not contain XE extensions, they end with infinite loop, and do not contain LTORG directives.
See `samples/` for inspiration: 
- `5.asm` adds $1$ and $2$ and displays the result
- `6.asm` computes and displays the sum of the first 100 natural numbers
- `7.asm` prints 'Jay Automata'
- `8.asm` enter a number between $2$ and $255$ and it prints whether the number is prime or not
- `9.asm` enter a number between $2$ and $1000$ and it prints its prime factorization

## tl;dr

1. Complete missing parts of `lab5/Assembler/pass2.py` to read the intermediate file, generate object code, and write the object file in the correct format.
2. Run `make test` from the `lab5/` directory to execute the test script and ensure you get "✅ All Tests Passed."
3. Use provided `simsic.py` to simulate the generated object code and verify its correctness.