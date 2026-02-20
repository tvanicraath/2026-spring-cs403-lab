COPY    START   1000
FIRST   LDA     ALPHA
        ADD     ONE
        STA     BETA
HALT    J       HALT        . Infinite loop to stop execution
ALPHA   RESW    1
BETA    RESW    1
ONE     WORD    1
        END     FIRST
