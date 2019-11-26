#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
from operator import itemgetter

a = input()
nb_pierre = int(a.split(' ')[0])
nb_poudre = int(a.split(' ')[1])
cont = int(a.split(' ')[2])

pierres = []
for i in range (0, nb_pierre):
    a = input()
    pierres.append ([ 'pierre', int(a.split(' ')[0]), int(a.split(' ')[1]),  int(a.split(' ')[0])/int(a.split(' ')[1] ) ] )
#pierres.sort (key=itemgetter(2), reverse=True)

poudres = []
for i in range (0, nb_poudre):
    a = input()
    poudres.append ([ 'poudre', int(a.split(' ')[1]) * int(a.split(' ')[0]), int(a.split(' ')[1]),  int(a.split(' ')[0]) ] )
#poudres.sort (key=itemgetter(2), reverse=True)

all = []
all.extend (pierres)
all.extend (poudres)
all.sort (key=itemgetter(3), reverse=True)

reste = cont
again = True 
valeur = 0
#0 : type
#1 : valeur tot
#2 : poids dispo en g
#3 : prix au g
while again:
    if reste>=all[0][2]:
        reste -= all[0][2]
        valeur += all[0][1]
        all.pop(0)
    elif reste<all[0][2]:
        if all[0][0]=='pierre':
            all.pop(0)
        else:
            valeur += reste * all[0][3]
            reste = 0
    if len (all)==0:
        again = False
    if reste ==0:
        again = False

print (valeur)
