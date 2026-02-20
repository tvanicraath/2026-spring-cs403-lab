#include <stdio.h>
#include <string.h>
#include "symtab.h"

SymNode SymTab[SYMTAB_SIZE];

void init_symtab() {
    for(int i=0; i<SYMTAB_SIZE; i++) SymTab[i].is_occupied = 0;
}

int hash(char *str) {
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++) sum += str[i];
    return sum % SYMTAB_SIZE;
}

int insert_symbol(char *symbol, int address) {
    int idx = hash(symbol);
    int start = idx;

    while (SymTab[idx].is_occupied) {
        if (strcmp(SymTab[idx].symbol, symbol) == 0) return 0; // Duplicate
        idx = (idx + 1) % SYMTAB_SIZE;
        if (idx == start) return -1; // Full
    }

    strcpy(SymTab[idx].symbol, symbol);
    SymTab[idx].address = address;
    SymTab[idx].is_occupied = 1;
    return 1; // Success
}

int search_symbol(char *symbol) {
    int idx = hash(symbol);
    int start = idx;

    while (SymTab[idx].is_occupied) {
        if (strcmp(SymTab[idx].symbol, symbol) == 0) return SymTab[idx].address;
        idx = (idx + 1) % SYMTAB_SIZE;
        if (idx == start) break;
    }
    return -1; // Not found
}

void display_symtab() {
    printf("\n[Symbol Table]\n");
    printf("Index\tLabel\tAddress\n");
    for(int i=0; i<SYMTAB_SIZE; i++) {
        if(SymTab[i].is_occupied) 
            printf("%d\t%s\t%X\n", i, SymTab[i].symbol, SymTab[i].address);
    }
}