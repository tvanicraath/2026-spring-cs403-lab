# Lab 2: Symbol Table and Opcode Table

Modify the Symbol Table from Lab 1 to include address (so we know where each symbol points to in memory). 
Additionally, implement an Opcode Table that will be used later to build an assembler.

## Symbol Table
Recall that SymTab tells us what the programmer defined.
Find its header file at `symtab.h`.
The skeleton implementation is provided in `symtab.c` that you need to complete.

## Opcode Table
Recall that OpTab tells us what the machine knows.
Find its header file at `optab.h`.
The skeleton implementation is provided in `optab.c` that you need to complete.
After completing both, `symtab.c` and `optab.c`, you can test them in `lab2.c`.


## Compilation, Execution, and Testing
To compile, use the provided `Makefile`.
To test your implementation, compare the output of your program with the expected output present in `test_output.txt` by running `make test`.
For cleaning up the compiled files, run `make clean`.

## tl;dr
- Complete `symtab.c` and `optab.c` appropriately.
- Run `make test` to test your implementation.
