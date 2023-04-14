10 LET a = 0
20 LET b = 0
30 LET c = 0
40 LET delta = 0

50 INPUT "Primeiro numero: "; a
60 INPUT "Segundo numero: "; b
70 INPUT "Terceiro numero: "; c

80 delta = b*b - 4*a*c

90 IF delta<0 THEN GOTO 100 ELSE GOTO 120
100 PRINT "Sem raizes reais"
110 END

120 IF delta>0 THEN GOTO 130 ELSE GOTO 160
130 PRINT "Raiz 1: "+ (-b+SQR(delta))/2*a
140 PRINT "Raiz 2: "+ (-b-SQR(delta))/2*a
150 END

160 PRINT "Raizes iguais: "+ (-b+SQR(delta))/2*a
170 END
