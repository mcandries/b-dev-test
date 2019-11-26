#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

prenom = []
taille = []
nb = int(input())
for i in range (0,nb):
    inp = input()
    prenom.append (inp.split(' ')[0])
    taille.append (int(inp.split(' ')[1]))

xmin = min(taille)

print (prenom[taille.index(xmin)])
