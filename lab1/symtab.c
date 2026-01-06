#include <stdio.h>
#include <string.h>
#include "symtab.h"

// Define the global variable here
Node SymTab[TABLE_SIZE];

// Initialize the table (clearing is_occupied flags)
void init_symtab() {
    for(int i = 0; i < TABLE_SIZE; i++) {
        SymTab[i].is_occupied = 0;
    }
}

// Simple Hash Function: Sum of ASCII % TABLE_SIZE
int hash(char *str) {
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        sum += str[i];
    }
    return sum % TABLE_SIZE;
}

int check_full() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (SymTab[i].is_occupied == 0) {
            return 0; // Found an empty slot
        }
    }
    return 1;
}

// Insert with Linear Probing
void insert(char *symbol) {
    int index = hash(symbol);

    if (check_full()) {
        printf("Error: Symbol Table is Full!\n");
        return;
    }

    while (SymTab[index].is_occupied) {
        // Check for duplicates
        if (strcmp(SymTab[index].symbol, symbol) == 0) {
            printf("Duplicate Symbol '%s' at index %d\n", symbol, index);
            return;
        }
        // Linear Probe: Move to next slot
        index = (index + 1) % TABLE_SIZE;
    }

    // Insert new symbol
    strcpy(SymTab[index].symbol, symbol);
    SymTab[index].is_occupied = 1;
    printf("Inserted '%s' at index %d\n", symbol, index);
}

// Search Function
void search(char *symbol) {
    int index = hash(symbol);
    int start_index = index;

    while (SymTab[index].is_occupied) {
        if (strcmp(SymTab[index].symbol, symbol) == 0) {
            printf("Found: '%s' at Index %d\n", symbol, index);
            return;
        }
        index = (index + 1) % TABLE_SIZE;
        
        if (index == start_index) break; // Looped around
    }
    printf("Not Found: '%s'\n", symbol);
}

// Display Function
void display() {
    printf("\n--- SYMBOL TABLE ---\n");
    printf("Index\tSymbol\n");
    printf("------------------\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (SymTab[i].is_occupied) {
            printf("%d\t%s\n", i, SymTab[i].symbol);
        } else {
            printf("%d\t---\n", i);
        }
    }
    printf("------------------\n");
}
