#!/usr/bin/env python3


################################ SETTINGS
ex_to_launch = "M2017_BD_ex5"
input_to_open = "input1.txt"
output_to_compare = "output1.txt"
################################

import sys, os, glob, io
import colored
from contextlib import redirect_stdout
from importlib import reload
import importlib
import subprocess

root_dir = os.path.dirname(os.path.realpath(__file__))

reset = colored.attr('reset')
green = reset + colored.fg('green')
red = reset + colored.fg('red')
yellow = reset + colored.fg ('yellow')
blue = reset + colored.fg ('blue')
white_on_blue = reset + colored.fg ('white') + colored.bg ('blue')
red_on_blue = reset + colored.fg ('red') + colored.bg ('blue')
white_on_green = reset + colored.fg ('white') + colored.bg ('green')
white_on_yellow = reset + colored.fg ('white') + colored.bg ('yellow')
white_on_red = reset + colored.fg ('white') + colored.bg ('red')
white = reset + colored.fg ('white')

are_tests_ok = True
missing_file = False
nb_input_file = 0
mod_loaded = False
mod = ""

############################################### Functions

def exec_exe (p_ex_to_launch, p_input_to_open, p_output_to_compare ):

    global are_tests_ok
    global mod_loaded
    global mod

    i_lines = []    #store Input lines
    c_lines = []    #store Correct Lines  (output file)
    o_lines = []    #store my Output

    with open (root_dir + "/" + p_ex_to_launch + "/sample/" + p_input_to_open ,"r") as f:
        i_lines = f.readlines ()

    with open (root_dir + "/" + p_ex_to_launch + "/sample/" + p_output_to_compare ,"r") as f:
        c_lines = f.readlines ()


    sys.stderr.write(white +'INPUT   DATA :\n' + ''.join(i_lines[:]) + "\n\n")
    sys.stderr.write(white +'CORRECT OUTPUT  DATA :\n ' + ''.join(c_lines[:]) + "\n\n")

    ##################################################
    sys.stdin = io.StringIO(''.join(i_lines))
    stream = io.StringIO()
    with redirect_stdout(stream):
        #if not mod_loaded:
        #    mod = __import__ (p_ex_to_launch+'.'+p_ex_to_launch)
        #    mod_loaded = True
        #else:
        #    mod = reload (mod)
        name = p_ex_to_launch+'.'+p_ex_to_launch
        spec = importlib.util.find_spec(name)
        modul = importlib.util.module_from_spec(spec)
        sys.modules[name] = modul
        spec.loader.exec_module(modul)

    o_lines = stream.getvalue().split("\n")[0:-1]

    #scrpt = os.path.join (root_dir, p_ex_to_launch, p_ex_to_launch + ".py")
    #o_lines = subprocess.run(["python",scrpt], capture_output=True, text=True, input=''.join(i_lines) ).stdout
    #if o_lines[-1:]=="\n":
    #    o_lines=o_lines[0:-1]
    #o_lines = o_lines.split('\n')

    ##################################################
    #print (o_lines)


    if len(c_lines)!=len(o_lines):
        print (red  + f"KO nb of line differ from corrects lines ({len(c_lines)}) to my lines ({len(o_lines)})") 
        are_tests_ok = False
    else :
        print (green + f"Nb of result lines are matching ({len(c_lines)})")

    for i,l in enumerate (c_lines):
        if i< len (o_lines):
            if l != o_lines [i]:
                print (red + f"KO on line {str (i)} :\n     correct lines : {l}\n     my lines      : {o_lines[i]}") 
                are_tests_ok = False
            else :
                print (green + f"OK on line {str (i)} :\n     correct lines : {l}\n     my lines      : {o_lines[i]}")

############################################### Main Script

all_sample = False
try :
    if len (sys.argv[1])!=0 and sys.argv[1]!="wrapper" :
        print (blue + "Using ARG as exercice to launch : " + sys.argv[1])
        ex_to_launch = sys.argv[1]
        
        if len (sys.argv[2])!=0 and sys.argv[2]=="--all-samples" :
            all_sample = True
except:
    pass


all_sample = False

if not all_sample:
    exec_exe (ex_to_launch, input_to_open, output_to_compare  )
    nb_input_file +=1
else:
    for input_file in os.listdir( root_dir + "/" + ex_to_launch + "/sample"):
        if input_file.startswith("input") and input_file.endswith(".txt"):
            input_file_name, input_file_ext = os.path.splitext (os.path.basename (input_file))
            output_file="output"+input_file_name[5:]+input_file_ext
            output_file_full_path = os.path.join (root_dir, ex_to_launch , "sample", output_file)
            if not os.path.exists(output_file_full_path) :
                sys.stderr.write (red_on_blue + f"ERROR, NOT FINDING THE OUTPUT FILE {output_file_full_path} CORRESPONDING TO INPUT FILE {input_file} \n\n" )
                missing_file = True
            else :
                sys.stderr.write (white_on_blue + f'\n-------------------\nLAUNCHING WITH FILE {input_file_name} \n')
                exec_exe (ex_to_launch, input_file, output_file)
                nb_input_file +=1 
                sys.stderr.write ('\n\n')

if are_tests_ok==True:
    if not missing_file:
        print (white_on_green + f"Hey, tests seem's ok for all input files ({nb_input_file})!")
    else:
        print (white_on_yellow + f"Seem's ok but missing files !")
else:
    print (white_on_red + "Don't give up, try again :)")

print (reset, end='')