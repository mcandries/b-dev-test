#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

N = int (input())
#NUM = [map (int, input().split())]
NUM= [int(i) for i in input().split() ]

AVERAGE = N/2

#sys.stderr.write(str(N) + "\n")
sys.stderr.write('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ' + str(N) +  "seeking value :" + str(AVERAGE) + "\n")
sys.stderr.write(' '.join(map(str,NUM)) + "\n")



RESULT = 0
P_VAL = NUM[0]
for C_VAL in NUM [1:]:
    if P_VAL == C_VAL == AVERAGE :
        RESULT = -1
        break

    if (P_VAL< AVERAGE <=C_VAL) or (P_VAL> AVERAGE >=C_VAL) :
        RESULT +=1

    P_VAL = C_VAL

if RESULT==-1:
    print ("INF")
else:
    print (RESULT)

