PRNT12  START   2000
        . --- Arithmetic ---
        LDA     ONE         . Load value 1 into A
        ADD     TWO         . Add value 2 (A = 3)
        
        . --- Convert to ASCII ---
        ADD     ASCII       . Add 48 to A to get ASCII '3'
        
        . --- Output ---
WAIT    TD      STDOUT      . Test if device 01 is ready
        JEQ     WAIT        . Loop until ready
        WD      STDOUT      . Write the character in A to device 01
        
        . --- Halt ---
HALT    J       HALT        . Infinite loop to stop execution

        . --- Data & Constants ---
ONE     WORD    1
TWO     WORD    2
ASCII   WORD    48          . Hex 30, decimal 48 (ASCII for '0')
STDOUT  BYTE    X'01'       . Device 01 is usually the screen/terminal
        END     PRNT12