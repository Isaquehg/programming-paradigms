REM Comentário
10 PRINT "OLA MUNDO"

REM Declaramos as variáveis com a palavra LET
19 LET X = 77
30 LET Y = 78

REM Criando-se arrays
40 ARRAY a
50 a[0] = "nome1"
60 a[1] = "nome2"
70 a[2] = "nome3"

REM Matriz
80 ARRAY b,2
90 b[0][0]="n1"
110 b[0][1]="n2"
120 b[1][0]="n3"
130 b[1][1]="n4"
140 PRINT b[0][1]

REM Entrada
150 INPUT "VALOR"; X

REM Ir para outras linhas:
160 GOTO 190

REM Condicionais
170 X = -6
180 IF X>0 THEN PRINT "Positivo" ELSE PRINT "Negativo"

REM Repeticao
190 FOR I = 0 TO 10 STEP 2
200 PRINT I 
210 NEXT I