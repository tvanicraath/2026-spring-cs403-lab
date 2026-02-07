# Lab 4: Assembler - Pass 1 

In the previous labs, we built the foundational components: a Symbol Table (Lab 1 & 2), an Opcode Table (Lab 2), and a Literal Table (Lab 3). 
We also learnt how to interface with Data Structures implemented in C from Python using Foreign Function Interfaces (FFIs).
In this lab, we will use the same to implement Pass 1 of a two-pass assembler.

## Goal of Pass 1 of the Assembler
The primary goal of Pass 1 is to assign addresses to all statements in the program and to resolve the values of all labels.
It separates the analysis of source statements from the generation of object code (which happens in Pass 2).

### Input
The input to Pass 1 is an assembly source code file.

### Output
The output of Pass 1 is an intermediate file with assigned addresses and a populated Symbol Table and Literal Table.
Recall that `LTORG` assigns addresses to all literals currently in the pool.
`END` also triggers an implicit `LTORG` for any remaining unassigned literals.
For intermediate file, use the following format:
```
[Address]   [Verbatim Source Line]
```


Where all comments and empty lines are skipped.
All other source lines (excluding END and LTORG directives) are prefixed with their assigned addresses in hexadecimal format.

See `samples/` for examples of sample assembly source files and their corresponding intermediate files.

## tl;dr
- Copy your `littab.py` file from Lab 3 to the `lab4/Assembler/` directory.

- Complete `lab4/Assembler/pass1.py` by handling **Assembler directives**: `START`, `END`, `WORD`, `RESW`, `RESB`, `BYTE`, and `LTORG`.

- Verify your implementation by running `make test` from the `lab4/` directory.