PRIME    START   2000
         LDX     ZERO        . Initialize X (not strictly used, but good practice)
         LDA     ZERO        . Clear Accumulator
         STA     NUM         . Initialize resulting number to 0

. --- Print Prompt ---
PRLOOP   LDCH    PROMPT,X    . Load character from prompt
         WD      OUTDEV      . Write character to output device
         TIX     PRLEN       . Increment X and compare to length
         JLT     PRLOOP      . Loop until all characters are printed

. --- Input Loop (Read characters) ---
READ     TD      INDEV       . Test Input Device
         JEQ     READ        . Loop until ready
         RD      INDEV       . Read character into A (rightmost byte)

         COMP    NEWLINE     . Check if 'Enter' key (End of input)
         JEQ     CHECK       . If Enter, go to Prime Check logic
         COMP    ASCII0      . Check if char is below '0' (validity check)
         JLT     CHECK       . If not a digit, stop reading

         . --- Convert ASCII to Int & Accumulate ---
         SUB     ASCII0      . Convert char to integer (A = A - 48)
         STA     DIGIT       . Save the single digit temporarily

         LDA     NUM         . Load current total number
         MUL     TEN         . NUM = NUM * 10
         ADD     DIGIT       . NUM = NUM + DIGIT
         STA     NUM         . Store updated number
         J       READ        . Read next digit

. --- Logic Setup ---
CHECK    LDA     NUM         . Load the full number
         COMP    TWO         . Compare with 2
         JLT     NOTP        . If NUM < 2, it is Not Prime

         DIV     TWO         . Calculate Limit (NUM / 2)
         STA     LIMIT       . Store upper bound for checking

         LDA     TWO         . Start divisor at 2
         STA     DIVSR       . Store in DIVSR variable

. --- Main Check Loop ---
LOOP     LDA     DIVSR       . Load current Divisor
         COMP    LIMIT       . Compare Divisor with Limit
         JGT     ISPRIME     . If Divisor > Limit, it is Prime

         . --- Modulo Calculation (NUM % DIVSR) ---
         LDA     NUM         . Load N
         DIV     DIVSR       . A = N / DIVSR (Integer division)
         MUL     DIVSR       . A = (N / DIVSR) * DIVSR
         STA     TEMP        . Store result temporarily
         LDA     NUM         . Load N again
         SUB     TEMP        . A = N - TEMP (This is the Remainder)

         COMP    ZERO        . Check if Remainder is 0
         JEQ     NOTP        . If Remainder == 0, factor found -> Not Prime

         . --- Increment Divisor ---
         LDA     DIVSR       . Load Divisor
         ADD     ONE         . Add 1
         STA     DIVSR       . Save new Divisor
         J       LOOP        . Repeat loop

. --- Output Section ---
ISPRIME  LDA     CHAR_P      . Load 'P'
         J       PRINT       . Jump to Print

NOTP     LDA     CHAR_N      . Load 'N'

PRINT    WD      OUTDEV      . Write result to Output Device
         
HALT     J       HALT        . Infinite loop to end program

. --- Data Section ---
NUM      WORD    0           . Final Integer
DIGIT    RESW    1           . Temp digit storage
DIVSR    WORD    2           . Current Divisor
LIMIT    RESW    1           . Loop Limit (N/2)
TEMP     RESW    1           . Temp storage for math

ZERO     WORD    0
ONE      WORD    1
TWO      WORD    2
TEN      WORD    10
ASCII0   WORD    48          . ASCII value for '0'
NEWLINE  WORD    10          . ASCII for Line Feed/Enter
CHAR_P   WORD    80          . Output 'P'
CHAR_N   WORD    78          . Output 'N'

INDEV    BYTE    X'F1'       . Input Device Code
OUTDEV   BYTE    X'05'       . Output Device Code

PROMPT   BYTE    C'ENTER NUMBER (2-255): '
PRLEN    WORD    23

         END     PRIME