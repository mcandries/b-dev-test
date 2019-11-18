#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import copy

class Dead_Past(Exception):
   """Raised when PAst in Dead"""
   pass

class Win(Exception):
   """Raised when Win"""
   pass

class No_More_Move(Exception):
   """Raised when Win"""
   pass

world_h = int(input())
space = []
for line in sys.stdin:
	space.append(list(line.rstrip('\n')))


def find_past (space):
    for i_l, l in enumerate (space):
        for i_c, c in enumerate (space[i_l]):
            if c == "O":
                return [i_c, i_l]

def next_space_time (prev):
    """ futur = list ()
    for i_l, l in enumerate (prev):
        futur.append([])
        for i_c, c in enumerate (prev[i_l]):
            futur[i_l].append(prev[i_l][i_c]) """
    futur = copy.deepcopy(prev)
    move_done = False

    possible_move = [
        [0,-1],
        [+1,0],
        [0,+1],
        [-1,0],
    ]

    for i_l, l in enumerate (prev):
        for i_c, c in enumerate (prev[i_l]):
            if c == "M":
                for x, y in possible_move:
                    real_y = i_l+y
                    if real_y >= len (futur):
                        real_y = real_y - len (futur)
                    real_x = i_c+x
                    if real_x >= len (futur[real_y]):
                        real_x = real_x - len (futur[real_y])

                    if futur[real_y][real_x ]=="." or futur[real_y][real_x ]=="C" :
                        futur[real_y][real_x ]="M"
                        move_done=True
                    elif futur[real_y][real_x ]=="O":
                        raise Dead_Past   

    for i_l, l in enumerate (prev):
        for i_c, c in enumerate (prev[i_l]):                  
            if c == "C":
                for x, y in possible_move:
                    real_y = i_l+y
                    if real_y >= len (futur):
                        real_y = real_y - len (futur)
                    real_x = i_c+x
                    if real_x >= len (futur[real_y]):
                        real_x = real_x - len (futur[real_y])

                    if futur[real_y][real_x]=="." :
                        futur[real_y][real_x]="C"
                        move_done=True
                    elif futur[real_y][real_x]=="O":
                        raise Win     
    if not move_done:
        raise No_More_Move
    return futur

    



space_time = []
space_time.append (space)

### wher is the PAstille ?
Past_X, Past_Y = find_past (space)

###Si pas de fantome on ne calcul rien
casper = False
for l in space:
    if "M" in l:
        casper = True
        break

if casper: 
    try :
        i = 0
        while True:
            space_time.append (next_space_time (space_time[i]))
            i +=1
    except Dead_Past:
        print ("0")
    except No_More_Move:
        print ("0")
    except Win:
        print (str(i+1))

else:
    pass


pass
