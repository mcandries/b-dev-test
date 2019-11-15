#!/usr/bin/env python3
import sys, os, glob, io
import urllib.request
import subprocess
import shutil


root_dir = os.path.dirname(os.path.realpath(__file__))

if len (sys.argv)<3 :
    print ("Need two parameter : NAME_OF_EXO URL_OF_ZIP_SAMPLE")
    quit(1)

NAME = sys.argv[1]
URL  = sys.argv[2]

if os.path.exists(os.path.join(root_dir, NAME)):
    print (f"{NAME} already exist")
    quit(1)

try :
    sample_dir = os.path.join(root_dir, NAME, 'sample')
    os.makedirs(sample_dir, exist_ok=False)
    f = open (os.path.join(root_dir, NAME, NAME+'.py'), 'w+')
    f.close()
except :
    print (f"Error creating folders and file !!")
    quit(1)

try:
    local_zip_file = os.path.join(root_dir, NAME, 'sample', '__tmpx.zip')
    urllib.request.urlretrieve(URL, local_zip_file )
except Exception as e :
    print (f"Error downloading file !!!" + str(e))
    quit(1)


try:
    subprocess.call (['unzip', local_zip_file ], cwd=sample_dir)
    LS = os.listdir (sample_dir)
    DIRS = [os.path.join(sample_dir,name) for name in LS if os.path.isdir(os.path.join(sample_dir,name))]
    if len (DIRS)>1:
        raise Exception ("MORE THAN ONE DIR IN SAMPLE DIR")
    files = os.listdir(DIRS[0])
    files.sort()
    for f in files:
        src = os.path.join(DIRS[0],f)
        dst = os.path.join(sample_dir,f)
        shutil.move(src,dst)
    
    os.remove (local_zip_file)
    shutil.rmtree (DIRS[0])


except Exception as e :
    print (f"Error unpacking files !!!" + str(e))
    quit(1)