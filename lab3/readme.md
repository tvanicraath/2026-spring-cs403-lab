# Lab 3: C Bindings for Python

When we write Systems Code, we often build libraries that other programs can use. 
In Lab-2 we built core data structures for an assembler: a Symbol Table and an Opcode Table.
In this lab, we will access these libraries from Python using C bindings.
For that ensure you have `ctypesgen` installed: `pip install ctypesgen`.[^python-venv]

## Sample lab3.py and lab3.c
Refer to the provided `lab3.py` and `lab3.c` files for sample implementations that test the Symbol Table and Opcode Table from Lab-2.
You should not change these.

## Python and C are Friends
To make Python talk to C, we need to bridge the gap between Python's high-level objects and C's low-level memory management.

### Shared Objects (`.so`)
An `.so` file contains compiled C code that isn't a standalone program (it has no main function).
Instead, it is loaded into memory at runtime by other programs (like the Python interpreter).
To create a shared object from your C code, you compile it with special flags:

* -shared: Tells GCC to produce a shared library, not an executable.
* -fPIC: "Position Independent Code." This ensures the code can be loaded anywhere in memory, which is required for shared libraries.[^fpic]

[^fpic]: Recall that in Assemblers discussed in class, we have only seen absolute addresses. For example, if a program is loaded at address 0x1000, all its instructions and data refer to absolute addresses based on that. Position Independent Code (PIC) allows the code to be loaded at any address without modification, which is essential for shared libraries that can be used by multiple programs simultaneously.

```Bash
# The resulting shared library combines symtab.c and optab.c 
# and will be named liblab3.so 
gcc -shared -fPIC -o liblab3.so symtab.c optab.c
```

### Bindings
Bindings are the "glue code" that acts as a translator to tell Python how a C struct looks like or how to call a C function.
While you can manually write these bindings using the `ctypes` library, it is tedious and error-prone.
`ctypesgen` is a tool that automates this[^ctypesgen-warning1].
It reads your C header files (`.h`), analyzes the structs and function signatures, and auto-generates a pure Python file that can be imported as if it were a normal Python module[^ctypesgen-warning2].
[^ctypesgen-warning1]: Note that `ctypesgen` may not support all C features perfectly, especially macros or complex structs. However, for the purposes of this lab, it should work fine.
[^ctypesgen-warning2]: You may get some warnings from `ctypesgen` about syntax errors, but you can ignore them for this lab.
Look for *INFO: Status: Writing to bindings.py.
INFO: Status: Wrapping complete.* to confirm that the bindings were generated successfully.

```Bash
# Note the missing prefix `lib`:
# -l lab3 tells it to link against liblab3.so
# in the current directory (-L .) 
ctypesgen -l lab3 -L . symtab.h optab.h -o bindings.py
```



### Running the Tests
When you run the Python script, the OS needs to know where to find your custom `.so` file.
If on Mac, replace `LD_LIBRARY_PATH` with `DYLD_LIBRARY_PATH`.

```Bash
python3 lab3.py  #  will fail
LD_LIBRARY_PATH=. python3 lab3.py # correct
```

## Write the Makefile to build and test your libraries
Write your own Makefile that automates the build and test of your libraries.
If you are stuck for a long time, first look at the provided Makefile for Lab-2 and if you are still stuck, look at the provided Makefile for Lab-3.
To test your implementation, run `make test`.

## Literal Table
Until now in this lab, we built the shared library `liblab3.so` that can be used in Python via the generated `bindings.py` file.
While we can complete the data structure suite by implementing a Literal Table in `littab.c` that handles constants like `=C'EOF'` or `=X'05'`, for convenience we will implement it in Python.
The skeleton code is provided in `littab.py` that you need to complete.
You should use `lab3-littab.py` to test your implementation.
If at the end of the course you (still) prefer C/C++, you can always come back and implement it in C/C++ and share it through `liblab3.so` later.
Complete the missing functions in `littab.py`.


## tl;dr
- Run `make test` to build and test your C libraries. It gives failed LitTab test, that's expected!
- Implement `littab.py` following the provided interface.
- Run `make test` to test your Literal Table implementation in Python. It should give "✅ All Tests Passed."

[^python-venv]: It is recommended to use a Python virtual environment to manage dependencies. You can create one using `python3 -m venv .venv` and activate it with `source .venv/bin/activate`. This will help keep your project dependencies isolated.
