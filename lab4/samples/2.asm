. Sets the program name to COPY and the Starting Address (LOCCTR) to 1000 (Hex).
COPY    START   1000
. Pass 1 Action: Initialize LOCCTR = 1000
FIRST   LDA     ALPHA
. Main Instruction Block
        ADD     ONE
        SUB     TWO
        STA     BETA
        LDA     =C'EOF'
        STA     =X'F1'
        LTORG
ALPHA   RESW    1
BETA    RESW    1
ONE     WORD    1
TWO     WORD    2
STR     BYTE    C'HELLO'
        END     FIRST
