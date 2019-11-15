# E > F
# F > P
# P > E


m_team_size = int (input ())
m_team = input ()

e_team_size = int (input ())
e_team = input ()

global t_comp = 'EEE'

def brute (ind):
    global m_team_size
    global m_team
    global e_team_size
    global e_team

    t_comp = t_comp[ind]


    if ind<m_team_size:
        brute (ind+1)



brute (0)