#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/


""" Format des données

Entrée
Ligne 1 : un entier N compris entre 1 et 100000 indiquant le nombre de poteaux de l'entrée.
Lignes 2 à N+1 : un entier compris entre 1 et 100000 représentant la hauteur d'un poteau.

Sortie
Un entier représentant la longueur totale de banderole que vous pourrez accrocher sur les poteaux 
en considérant que la distance entre deux poteaux consécutifs est de 1 mètre. """

import sys

nb_pot = int(input())

pots = []
for line in sys.stdin:
	pots.append(int(line.rstrip('\n')))


banderole = 0
for i, pot in enumerate (pots):
    ok = True
    j = 1
    while ok:
        if (i+j)>=nb_pot :
            ok=False
        else :
            if pots[i+j]<pot:
                banderole += 1
            elif pots[i+j]==pot:
                banderole += 1
                ok = False       
            elif pots[i+j]>pot:
                ok = False
        j +=1

print (banderole)