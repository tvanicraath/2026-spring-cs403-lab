JAY      START   2000
         LDX     ZERO        . X = 0 (Index for the string)

LOOP     LDCH    STR,X       . Load character from STR + X into Reg A
         COMP    SENTINEL    . Check if we hit the '!' (End of string)
         JEQ     HALT        . If A == '!', jump to HALT
         
WAIT     TD      STDOUT      . Test if Device 01 is ready
         JEQ     WAIT        . Loop until ready
         WD      STDOUT      . Write the character in A to Device 01
         
         . --- Increment X ---
         TIX     MAX         . X = X + 1, compare to a high number
         . (In Standard SIC, TIX increments X and sets SW)
         
         J       LOOP        . Back to loop

HALT     J       HALT        . Infinite loop to end program

. --- Data Section ---
STDOUT   BYTE    X'01'       . Device 01 (Terminal)
ZERO     WORD    0
MAX      WORD    100         . Arbitrary limit for TIX
SENTINEL WORD    33          . ASCII for '!' (used as null-terminator)
STR      BYTE    C'Jay Automata!'
         END     JAY