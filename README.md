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
* **Task:** Implement and test OpTab.
* **Skills:** Build and test pipelines using Makefiles. 

### Lab 3: C Bindings for Python
* **Concepts:** Foreign Function Interface (FFI) and Dynamic Linking
* **Task:** Compile the C modules into a Shared Object library (`.so`) and use `ctypesgen` to generate Python wrappers for it. Build LitTab as Python module. Use the Python test script to verify the library and cross-check with the C test script.
* **Skills:** Creating Shared Libraries and interfacing C with Python.


### Lab 4: Assembler Pass 1
* **Concepts:** Two-Pass Assembler, Symbol Resolution, and Intermediate Representation
* **Task:** Implement the first pass of a two-pass assembler in Python using bindings to the SymTab and OpTab C libraries along with the LitTab Python module from Lab 3.
* **Skills**: File I/O in Python and Hybrid Data Structures.


## Roadmap

### Lab 5: Assembler Pass 2
* **Concepts:** Two-Pass Assembler and Object Code Generation
* **Task:** Implement the second pass of the assembler to generate object code from the intermediate representation produced in Pass 1.
* **Skills:** Addressing Modes in Assembly and Simulating SIC Machine

### Lab 6: Lexical Analyzer

### Lab 7: Parser

### Lab 8: Intermediate Code Generation

### Lab 9: Optimization

### Lab 10: Linker and Loader
