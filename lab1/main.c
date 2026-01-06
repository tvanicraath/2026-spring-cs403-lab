#include <stdio.h>
#include "symtab.h"

int main() {
    printf("Lab 1: Symbol Table with Linear Probing\n");
    init_symtab();

    // Test 1: Standard Insertions
    insert("A");
    insert("K");
    
    // Test 2: Force Collision
    // 'A' (65) % 10 = 5
    // 'K' (75) % 10 = 5 -> Should probe to 6
    insert("B"); 
    insert("AA"); 

    // Test 3: Duplicate Error
    printf("\nTesting Duplicate:\n");
    insert("AA"); 

    // Show Table State
    display();

    // Test 4: Search
    printf("\nTesting Search:\n");
    search("B");
    search("XYZ"); // Does not exist

    // Test 5: Fill Table
    printf("\nFilling Table:\n");
    insert("C");
    insert("D");
    insert("E");
    insert("F");
    insert("G");
    insert("H");
    insert("I"); // Should indicate full
    insert("J"); // Should indicate full
    display();

    return 0;
}
