FACTOR   START   2000
         LDX     ZERO
         LDA     ZERO
         STA     N

. --- Print Prompt ---
PRLOOP   LDCH    PROMPT,X    . Load character from prompt
         WD      OUTDEV      . Write character to output device
         TIX     PRLEN       . Increment X and compare to length
         JLT     PRLOOP      . Loop until all characters are printed

. ---------------------------------------------------------
. 1. INPUT ROUTINE
. ---------------------------------------------------------
READ     TD      INDEV
         JEQ     READ
         
         LDA     ZERO        . <--- CRITICAL FIX: Clear A before Read
         RD      INDEV       . Now A will be 0000XX
         
         COMP    NEWLINE     . Check for Enter
         JEQ     PREP
         COMP    ASCII0      . Validate digit
         JLT     PREP

         SUB     ASCII0      . Convert char to int
         STA     DIGIT
         
         LDA     N
         MUL     TEN         . N = N * 10
         ADD     DIGIT       . N = N + Digit
         STA     N
         J       READ

. ---------------------------------------------------------
. 2. PREPARE OUTPUT
. ---------------------------------------------------------
PREP     LDA     N
         STA     VAL
         JSUB    PRINT       . Print N

         LDCH    EQ_SIGN
         WD      OUTDEV
         LDCH    SPACE
         WD      OUTDEV

         LDA     TWO         . Start Divisor at 2
         STA     DIVSR

. ---------------------------------------------------------
. 3. FACTORIZATION LOOP
. ---------------------------------------------------------
MAINLP   LDA     N
         COMP    ONE         . Stop if N == 1
         JEQ     HALT

         . -- Check Divisibility --
         LDA     N
         DIV     DIVSR
         MUL     DIVSR
         STA     TEMP
         LDA     N
         SUB     TEMP        . Remainder

         COMP    ZERO
         JEQ     IS_FACT

         . -- Increment Divisor --
         LDA     DIVSR
         ADD     ONE
         STA     DIVSR
         J       MAINLP

. ---------------------------------------------------------
. 4. FACTOR FOUND HANDLER
. ---------------------------------------------------------
IS_FACT  LDA     DIVSR
         STA     VAL
         JSUB    PRINT

         LDA     N
         DIV     DIVSR
         STA     N

         COMP    ONE
         JEQ     HALT
         
         LDCH    SPACE
         WD      OUTDEV
         LDCH    X_SIGN
         WD      OUTDEV
         LDCH    SPACE
         WD      OUTDEV
         
         J       MAINLP      . Check same divisor again

HALT     J       HALT

. ---------------------------------------------------------
. SUBROUTINE: PRINT
. ---------------------------------------------------------
PRINT    STX     SAVEX
         LDA     ZERO
         STA     COUNT

EXTRACT  LDA     VAL
         COMP    ZERO
         JEQ     CHECK_Z

         DIV     TEN
         MUL     TEN
         STA     TEMP
         LDA     VAL
         SUB     TEMP        . Digit
         ADD     ASCII0      
         
         LDX     COUNT
         STCH    BUFFER,X
         
         LDA     COUNT
         ADD     ONE
         STA     COUNT

         LDA     VAL
         DIV     TEN
         STA     VAL
         J       EXTRACT

CHECK_Z  LDA     COUNT
         COMP    ZERO
         JGT     PRT_LP
         
         LDCH    ASCII0
         WD      OUTDEV
         J       EXIT_P

PRT_LP   LDA     COUNT
         COMP    ZERO
         JEQ     EXIT_P

         SUB     ONE
         STA     COUNT
         LDX     COUNT
         LDCH    BUFFER,X
         WD      OUTDEV
         J       PRT_LP

EXIT_P   LDX     SAVEX
         RSUB

. ---------------------------------------------------------
. DATA VARIABLES
. ---------------------------------------------------------
N        WORD    0
VAL      WORD    0
DIVSR    WORD    2
DIGIT    RESW    1
TEMP     RESW    1
COUNT    WORD    0
SAVEX    RESW    1

BUFFER   RESB    6           . Buffer for text chars

. Constants
ZERO     WORD    0
ONE      WORD    1
TWO      WORD    2
TEN      WORD    10
ASCII0   WORD    48
NEWLINE  WORD    10

EQ_SIGN  BYTE    C'='
X_SIGN   BYTE    C'x'
SPACE    BYTE    C' '

INDEV    BYTE    X'F1'
OUTDEV   BYTE    X'05'

PROMPT   BYTE    C'ENTER NUMBER (2-1000): '
PRLEN    WORD    23

         END     FACTOR