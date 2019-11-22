#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/


""" Format des données

Entrée
Ligne 1 : un entier N compris entre 1 et 1000, indiquant le nombre de pylônes le long de la vallée.
Lignes 2 à N+1 : la hauteur d'un pylône, un entier compris entre 1 et 100. """





import sys




lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


