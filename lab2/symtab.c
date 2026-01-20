#include <stdio.h>
#include <string.h>
#include "symtab.h"

SymNode SymTab[SYMTAB_SIZE];

void init_symtab() {
    for(int i=0; i<SYMTAB_SIZE; i++) SymTab[i].is_occupied = 0;
}

int hash(char *str) {
    /* Write code here. */
    //should return sum of ASCII values of characters mod SYMTAB_SIZE
}

int insert_symbol(char *symbol, int address) {
    /* Write code here. */
}

int search_symbol(char *symbol) {
    /* Write code here. */
}

void display_symtab() {
    printf("\n[Symbol Table]\n");
    printf("Index\tLabel\tAddress\n");
    for(int i=0; i<SYMTAB_SIZE; i++) {
        if(SymTab[i].is_occupied) 
            printf("%d\t%s\t%X\n", i, SymTab[i].symbol, SymTab[i].address);
    }
}