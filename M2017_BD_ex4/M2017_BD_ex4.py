#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/


# E > F
# F > P
# P > E

import sys
from collections import Counter 
from itertools import permutations


m_team_size = int (input ())
m_team = input ()
count_t = Counter (m_team)

e_team_size = int (input ())
e_team = input ()

t_comp = list()
t_typ = 'EFP'

def brute_team (ind, curr):
    global m_team_size
    global t_comp
    global t_typ
    global count_t

    for typ in t_typ:
        l_curr = curr
        if ind<m_team_size-1:
            brute_team (ind+1, l_curr + typ)
        else :
            count_c = Counter (l_curr + typ)
            if count_c['E']==count_t['E'] and count_c['F']==count_t['F'] and count_c['P']==count_t['P']:
                t_comp.append (l_curr + typ)


def test_comp (comp1, comp2):

    def best_w (w1, w2):
        # E > F
        # F > P
        # P > E

        b = ["EE=","EF+","EP-","FE-","FF=","FP+","PE+","PF-","PP="]
        for poss in b:
            if poss[0:2] == (w1 + w2):
                return poss[2]


    fight_end = False
    t1_warrior_ind = 0
    t2_warrior_ind = 0
    while not fight_end:
        if t1_warrior_ind>=len(comp1) and t2_warrior_ind>=(len(comp2)):
            return "="
        elif t1_warrior_ind>=len(comp1) and t2_warrior_ind<(len(comp2)):
            return "-"
        elif t1_warrior_ind<len(comp1) and t2_warrior_ind>=(len(comp2)):
            return "+"

        res_battle = best_w (comp1[t1_warrior_ind], comp2[t2_warrior_ind])

        if res_battle == '=' :
            t1_warrior_ind += 1
            t2_warrior_ind += 1
        
        if res_battle == "+":
            t2_warrior_ind += 1

        if res_battle == "-":
            t1_warrior_ind += 1





point = {'-':-1, '=':0,'+':1}
best_res = '-'
best_res_full = '-'
t_comp = permutations (m_team, len (m_team))
#brute_team (0, '')
for team in t_comp:
    res = test_comp (team, e_team)
    if point[res]>=point[best_res]:
        best_res=res
        best_res_full = res + ''.join (team)

print(best_res_full)
    

#sys.stderr.write(str(t_comp))