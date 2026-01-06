#ifndef SYMTAB_H
#define SYMTAB_H

#define TABLE_SIZE 10   // Small size to force collisions
#define SYMBOL_LEN 10   // Max length of a label

// Data Structure Definition
typedef struct {
    char symbol[SYMBOL_LEN];
    int is_occupied; // 0 = empty, 1 = occupied
} Node;

// Global Symbol Table (extern tells the compiler it lives in symtab.c)
extern Node SymTab[TABLE_SIZE];

// Function Prototypes
void init_symtab();
int hash(char *str);
void insert(char *symbol);
void search(char *symbol);
void display();

#endif
