lab1: main.o symtab.o
	gcc main.o symtab.o -o lab1

main.o: main.c symtab.h
	gcc -c main.c

symtab.o: symtab.c symtab.h
	gcc -c symtab.c

clean:
	rm *.o lab1
