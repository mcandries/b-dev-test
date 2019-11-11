#!/usr/bin/env python3


################################ SETTINGS
ex_to_launch = "M2016_ex1"
input_to_open = "input1.txt"
output_to_compare = "output1.txt"
################################

import sys
import os
import colored
from contextlib import redirect_stdout
import io

red = colored.fg('red')
yellow = colored.fg ('yellow')
blue = colored.fg ('blue')
white_on_green = colored.fg ('white') + colored.bg ('green')
reset = colored.attr('reset')


try :
    if len (sys.argv[1])!=0:
        print (yellow + "Using ARG as exercice to launch : " + sys.argv[1])
        ex_to_launch = sys.argv[1]
except:
    pass


i_lines = []    #store input lines
c_lines = []    #store Correct Lines  (output file)
o_lines = []    #store my output


with open (os.path.dirname(os.path.realpath(__file__)) + "/" + ex_to_launch + "/sample/" + input_to_open ,"r") as f:
    i_lines = f.readlines ()

with open (os.path.dirname(os.path.realpath(__file__)) + "/" + ex_to_launch + "/sample/" + output_to_compare ,"r") as f:
    c_lines = f.readlines ()


sys.stdin = i_lines


####################################################################################################################
stream = io.StringIO()
with redirect_stdout(stream):
    exo = __import__ (ex_to_launch+'.'+ex_to_launch)
o_lines = stream.getvalue().split("\n")[0:-1]

#####################################################################################################################
#print (o_lines)

are_tests_ok = True

if len(c_lines)!=len(o_lines):
    print (red  + f"KO nb of line differ from corrects lines ({len(c_lines)}) to my lines ({len(o_lines)})") 
    are_tests_ok = False
else :
    print (blue + f"Nb of result lines are matching {len(c_lines)}")

for i,l in enumerate (c_lines):
    if i< len (o_lines):
        if l != o_lines [i]:
            print (red + f"KO on line {str (i)} :\n     correct lines : {l}\n     my lines      : {o_lines[i]}") 
            are_tests_ok = False
        else :
            print (blue + f"OK on line {str (i)} :\n     correct lines : {l}\n     my lines      : {o_lines[i]}")

if are_tests_ok==True:
    print (white_on_green + "Hey, tests seem's ok !")

print (reset, end='')