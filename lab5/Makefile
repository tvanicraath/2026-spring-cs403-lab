# Generate Position Independent Code for shared libraries
SHFLAGS = -shared -fPIC
CTYPESGEN = ../.venv/bin/ctypesgen

# Phony targets
.PHONY: ffi test clean #tells make: "These targets are commands to run, not files to create."
all: test

# 2. Shared Library
Assembler/liblab3.so:
	gcc $(SHFLAGS) -o Assembler/liblab3.so Assembler/symtab.c Assembler/optab.c

# 3. Python Bindings
Assembler/bindings.py: Assembler/liblab3.so
	@$(CTYPESGEN) -l lab3 -L . Assembler/symtab.h Assembler/optab.h -o Assembler/bindings.py

# 4. Littab 
Assembler/littab.py: Assembler/littab.py
	cp Assembler/littab.py Assembler/littab.py

# 5. FFI Build
ffi: Assembler/liblab3.so Assembler/bindings.py
	@echo "✅ FFI Build Successful."

# 6. Test Suite
test: ffi Assembler/pass1.py Assembler/littab.py
	@echo "--- Running Python Test ---"
	DYLD_LIBRARY_PATH=. LD_LIBRARY_PATH=. python3 lab5-test.py
	@echo "\n✅ All Tests Passed."

# Clean Artifacts
clean:
	rm -rf Assembler/__pycache__ __pycache__
	rm -f samples/*.asm.pass1
	rm -f samples/*.asm.obj
	rm -f Assembler/liblab3.so Assembler/bindings.py