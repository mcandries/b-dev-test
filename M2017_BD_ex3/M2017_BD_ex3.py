#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

largeur = int(input())
niv = input()

s_prev = '*'
max = 1
cur_jump=1
for s in niv:
    if s == '_':
        cur_jump+=1
    if s == "-" and s_prev == '_':
        if cur_jump>max:
            max = cur_jump
        cur_jump=1
    s_prev = s

print (max)


