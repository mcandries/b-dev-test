#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
from operator import itemgetter

def toto ():
    tmp_res = ''
    a = input()
    nb_cab = int(a.split(' ')[0])
    nb_req = int(a.split(' ')[1])

    dat = []
    for i in range (0,nb_req):
        a = input()
        dat.append ([int(a.split(' ')[0]), int(a.split(' ')[1]) ])
        

    #sorted (dat)
    dat.sort (key=itemgetter(0))

    free_cbl = []
    for i in range (1,nb_cab+1):
        free_cbl.append (-1)

    for i in range (0,2500):
        for x in range (0,nb_req):
            if dat[x][1]==i:
                cab_nb = free_cbl.index (x)
                free_cbl[cab_nb] = -1
 
        for x in range (0,nb_req):
            if dat[x][0]==i:
                try :
                    cab_nb = free_cbl.index (-1)
                    free_cbl[cab_nb] = x
                    tmp_res += str (cab_nb+1) + ' '
                except:
                    print ("pas possible")
                    return 0
    
    print (tmp_res[:-1])

toto()