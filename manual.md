# Lab 1: Symbol Table (Linear Probing)

Implement a Symbol Table using a Hash Table with Linear Probing to resolve collisions. This structure is fundamental for compilers to store identifiers.

### Requirements
- Use a fixed-size array of `TABLE_SIZE=10` nodes.
- Each node should store a symbol (string) and a status flag (empty/occupied).
- Implement a hash (`Sum(ASCII) % TABLE_SIZE`) to map strings to indices.
- If a hashed index is occupied, check the next slot sequentially, wrapping around, to find an empty spot.
- If the table is full, report an error on insertion attempts.

### Operations
```C
void insert(char *symbol); //Add a symbol to the table
int search(char *symbol);  //Search for a symbol in the table returning its index or -1 if not found
void display();            //Display the contents of the symbol table
```

### Main Function
In main function, show:
- insertions
- collision handling
- handling duplicates
- handling full table

### Good Practices (for C)
- Modular code with separate header and source files.
- Makefile