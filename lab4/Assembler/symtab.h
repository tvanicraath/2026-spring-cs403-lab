#ifndef SYMTAB_H
#define SYMTAB_H

#define SYMTAB_SIZE 20000  // Increased size for future
#define SYMBOL_LEN 20 // Increased size for future

typedef struct {
    char symbol[SYMBOL_LEN];
    int address;
    int is_occupied;    
} SymNode;

void init_symtab();
int insert_symbol(char *symbol, int address); // Returns 1 on success, 0 on duplicate/full
int search_symbol(char *symbol); // Returns address or -1 if not found
void display_symtab();

#endif
