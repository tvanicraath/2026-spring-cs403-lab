# Generate Position Independent Code for shared libraries
SHFLAGS = -shared -fPIC

# Phony targets
.PHONY: all test clean #tells make: "These targets are commands to run, not files to create."

# Default target
all: lab3 littab.py liblab3.so bindings.py

# 1. C Executable
lab3: lab3.o symtab.o optab.o
	gcc lab3.o symtab.o optab.o -o lab3

# 2. Shared Library
liblab3.so: symtab.c optab.c
	gcc $(SHFLAGS) -o liblab3.so symtab.c optab.c

# 3. Python Bindings
bindings.py: liblab3.so symtab.h optab.h
	ctypesgen -l lab3 -L . symtab.h optab.h -o bindings.py

# Object File Rules
lab3.o: lab3.c symtab.h optab.h
	gcc -c lab3.c

symtab.o: symtab.c symtab.h
	gcc -c symtab.c

optab.o: optab.c optab.h
	gcc -c optab.c

# 4. Test Suite
test: all
	@echo "--- Running C Test for SymTab and OpTab ---"
	./lab3 > c_output.txt
	@diff -w -y --suppress-common-lines test_out.txt c_output.txt && echo "✅ C Test Passed!" || (echo "❌ C Test Failed!"; exit 1)
	
	@echo "\n--- Running Python Test for SymTab and OpTab ---"
	DYLD_LIBRARY_PATH=. LD_LIBRARY_PATH=. python3 lab3.py > py_output.txt
	@diff -w -y --suppress-common-lines test_out.txt py_output.txt && echo "✅ Python liblab3.so Test Passed!" || (echo "❌ Python Test Failed!"; exit 1)
	@rm -f c_output.txt py_output.txt
	
	@echo "\n--- Running Python Test for LitTab ---"
	@python3 lab3-littab.py > /dev/null && echo "✅ Python LitTab Tests Passed!" || (echo "❌ Python LitTab Tests Failed!"; exit 1)

	@echo "\n✅ All Tests Passed."
	

# Clean Artifacts
clean:
	rm -f *.o lab3 liblab3.so bindings.py
	rm -f *_output.txt
	rm -rf __pycache__