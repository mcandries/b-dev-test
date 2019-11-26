#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

pl=[]
for i in range (0,4):
    pl.append (int(input()))

lng = min (pl)

j = 0
for p in pl:
    j += p-lng

print (j)