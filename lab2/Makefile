lab2: lab2.o symtab.o optab.o
	gcc lab2.o symtab.o optab.o -o lab2

lab2.o: lab2.c symtab.h optab.h
	gcc -c lab2.c

symtab.o: symtab.c symtab.h
	gcc -c symtab.c

optab.o: optab.c optab.h
	gcc -c optab.c

test: lab2
	./lab2 > my_output.txt
	@diff -w -y --suppress-common-lines test_out.txt my_output.txt && echo "✅ Test Passed!" || echo "❌ Test Failed! See differences above."
	@rm my_output.txt

clean:
	rm *.o lab2