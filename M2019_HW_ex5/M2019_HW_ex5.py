#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use:  to display debugging information to STDERR
#* ***/
import sys
from itertools import permutations 

nb = int(input())
mots = []
lettres = set ()
for i in range (0, nb):
    mots.append (input())
    for l in mots[-1]:
        lettres.add (l)

lettres.add (" ")    

for y in range (1,10):
    sys.stderr.write ("perm deep " + str (y) + '\n')

    for perm in permutations (lettres,y):
        sys.stderr.write ("Test perm" + str(perm) + '\n')
        resp = []
        for i,mot in enumerate (mots):
            resp.append (mot)
            for p_letter in perm:
                if resp[i].find (p_letter):
                    resp[i] = resp[i].replace (p_letter, '')
        
        ok = True
        for i in range (1, len (resp)):
            #sys.stderr.write (resp[i])
            #sys.stderr.write (resp[i-1])
            #sys.stderr.write (str (resp[i]!=resp[i-1]))            
            if resp[i]!=resp[i-1]:
                ok = False
        if ok:
            print (resp[0])
            quit()





#sys.stderr.write(str(mots))
#sys.stderr.write(str(poss))

