SUMPRT  START   2000
        . --- Part 1: Calculate Sum (1..100) ---
        LDA     ZERO
        STA     INDEX
        STA     TOTAL
SLOOP   LDA     INDEX
        ADD     ONE
        STA     INDEX
        ADD     TOTAL
        STA     TOTAL
        LDA     INDEX
        COMP    LIMIT
        JLT     SLOOP       . Loop until INDEX = 100

        . --- Part 2: Extract Digits to Buffer ---
        LDX     ZERO        . X = 0 (Buffer Offset)
CONV    LDA     TOTAL
        DIV     TEN
        STA     QUOT
        MUL     TEN
        STA     TEMP
        LDA     TOTAL
        SUB     TEMP        . A = Remainder
        ADD     ASCII       . Convert to '0'-'9'
        
        STCH    BUFFER,X    . Store character in BUFFER[X]
        
        . Manually increment X (Standard SIC has no TIXR)
        LDA     XPTR        
        ADD     ONE
        STA     XPTR
        LDX     XPTR        . Update X register
        
        LDA     QUOT
        STA     TOTAL       . Move quotient to total for next division
        COMP    ZERO
        JGT     CONV        . Loop if Quotient > 0

        . --- Part 3: Print Buffer Backwards ---
PRNT    LDA     XPTR        . Get current buffer size
        SUB     ONE         . Move to last stored index
        STA     XPTR
        LDX     XPTR        . Load index into X
        LDCH    BUFFER,X    . Load character
        
WAIT    TD      STDOUT
        JEQ     WAIT
        WD      STDOUT
        
        LDA     XPTR
        COMP    ZERO
        JGT     PRNT        . Loop until all digits printed

HALT    J       HALT        . Finished

. --- Data Section ---
INDEX   WORD    0
TOTAL   WORD    0
ONE     WORD    1
LIMIT   WORD    100
TEN     WORD    10
ASCII   WORD    48
ZERO    WORD    0
QUOT    WORD    0
TEMP    WORD    0
XPTR    WORD    0           . Manual X register tracker
STDOUT  BYTE    X'01'
BUFFER  RESB    10          . Space for "5050"
        END     SUMPRT