#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

p1_lat, p1_lng, p2_lat, p2_lng = map (float, lines[0].split())

nb_ppl = int (lines[1])

nb_ppl_in = 0
for ppl in lines [2:nb_ppl+2]:
    ppl_lat, ppl_lng = map (float, ppl.split (" ")) 
    if p1_lat <= ppl_lat <= p2_lat and p1_lng <= ppl_lng <= p2_lng:
        nb_ppl_in += 1

print (str(nb_ppl_in))