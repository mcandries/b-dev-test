#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import itertools

anc_temple = input()
lst_ville = set()
links = {}
ville = []
liens_ville = []
for i in range (0, 21):
    a = input()
    lst_ville.add (a.split(' ')[0]) 
    lst_ville.add (a.split(' ')[1])
    ville_A = a.split(' ')[0]
    ville_B = a.split(' ')[0]
    #if not ville_A in links :
    links[ville_A] = ville_B
    links[ville_B] = ville_A

    if not ville_A in ville:
        ville.append (ville_A)
        liens_ville.append (0)
    if not ville_B in ville:
        ville.append (ville_B)
        liens_ville.append (0)
    i = ville.index (ville_A)
    liens_ville[i]+=1
    

print ("a")
