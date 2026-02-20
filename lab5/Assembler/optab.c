#include <stdio.h>
#include <string.h>
#include "optab.h"

typedef struct {
    char mnemonic[10];
    char machine_code[3];
} OpNode;

// Hardcoded SIC Standard Opcodes (Partial List)
OpNode OPTAB[] = {
    {"LDA", "00"}, {"LDX", "04"}, {"LDL", "08"}, {"LDCH", "50"},
    {"STA", "0C"}, {"STX", "10"}, {"STL", "14"}, {"STCH", "54"},
    {"ADD", "18"}, {"SUB", "1C"}, {"MUL", "20"},
    {"DIV", "24"}, {"COMP","28"}, {"TIX", "2C"},
    {"JEQ", "30"}, {"JGT", "34"}, {"JLT", "38"},
    {"J",   "3C"}, {"AND", "40"}, {"OR",  "44"},
    {"JSUB","48"}, {"RSUB","4C"},
    {"RD", "D8"}, {"WD", "DC"}, {"TD", "E0"}
};
const int OPTAB_LEN = sizeof(OPTAB)/sizeof(OpNode);

char* search_optab(char *mnemonic) {
    for(int i=0; i<OPTAB_LEN; i++) {
        if(strcmp(OPTAB[i].mnemonic, mnemonic) == 0) {
            return OPTAB[i].machine_code;
        }
    }
    return NULL;
}