# CS 403: System Software (Spring 2026)

> **Lab assignments and reference implementations for CS403. This Readme will evolve as the course progresses.**

## Overview
Unlike traditional approaches that use a single language, we will use a multi-language strategy in this course.
This mirrors real-world projects where different components are implemented in languages best suited for those tasks.

* **Core in C:** Performance-critical components are implemented in C.
* **Foreign Function Interface (FFI):** loading shared C libraries (`.so`) into Python.
* **System Tooling:** Automating builds and bindings with `make`.
* **Scripting and Testing:** Using Python for high-level scripting, testing, and validation.

> ### Why bother with FFIs? Why can't I use `dict` instead?!
This is an exercise to practice hashing algorithms, collision resolution, manual memory management etc, which IMO is a must for a Systems Programming course.
We then learn how to interface them with higher-level languages like Python.
In real-world systems, we write in high-level language.
Then we **profile** (identify bottlenecks), and rewrite only the critical parts in low-level languages like C/C++/Rust. 

## Labs Schedule

### Lab 1: Symbol Table
* **Concepts:** Hash Tables and Linear Probing.
* **Task:** Implement a fixed-size SymTab in C that handles insertions, collisions, and lookups.
* **Skills:** Writing own header files.

### Lab 2: Operation Code Table & Makefile
* **Concepts:** Static Lookup Table and Modular Compilation
* **Task:** Implement an OpTab. Test both, SymTab and OpTab in a single C program using a Makefile. Write a Makefile to build the test pipeline.
* **Skills:** Build and test pipelines using Makefiles. 

### Lab 3: C Bindings for Python
* **Concepts:** Foreign Function Interface (FFI) and Dynamic Linking
* **Task:** Compile the C modules into a Shared Object library (`.so`). Use `ctypesgen` to generate Python wrappers for it. Build LitTab as Python module. Write a Python test script to verify the library and cross-check with a C test script.
* **Skills:** Creating Shared Libraries and interfacing C with Python.

## Roadmap


### Lab 4: Assembler Pass 1
* **Concepts:** Two-Pass Assembler, Symbol Resolution, and Intermediate Representation
* **Task:** Implement the first pass of a two-pass assembler in Python using bindings to the SymTab and OpTab C libraries along with the LitTab Python module from Lab 3.
* **Skills**: File I/O in Python and Hybrid Data Structures.


### Lab 5: Assembler Pass 2

### Lab 6: Macro Processor

### Lab 7: Lexical Analyzer

### Lab 8: Parser

### Lab 9: Intermediate Code Generation and Optimization

### Lab 10: Linker and Loader
