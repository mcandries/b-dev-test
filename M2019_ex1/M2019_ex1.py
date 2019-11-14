#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

my_place = int(input ())

for i in range (42):
    perte, gain = map (int,input().split())
    my_place -= gain-perte

gain = 0
if my_place<=100:
    gain += 1000
elif my_place<=10000:
    gain += 100

if gain==0:
    print ("KO")
else:
    print (gain)