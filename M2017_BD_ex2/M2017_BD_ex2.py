#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

nb_games = int(input())

an = []
for i in range (nb_games):
    an.append (int(input()))


print (str (max (an) - min (an)))