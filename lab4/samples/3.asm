PROG    START   2000
        LDA     =C'EOF'
        LDX     =X'05'
        STA     BUFFER
        LTORG
BUFFER  RESB    10
INPUT   BYTE    C'TEST'
        LDA     =C'EOF'  . Duplicate literal, should share address
        LDA     =X'1F'   . New literal
        END     PROG
