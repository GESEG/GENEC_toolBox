#!/usr/bin/env python
'''
'comments 
'''
import numpy as np
import commands
import os
import sys
import GENEC_toolBox as GtB

import subprocess 

wg_folder='/lupus/hirschi/data/Grids2010/wg/'
for zed in ['Z020','Z014','Z006','Z002','Z4m4','Z1m5','Z000']:
#for zed in ['Z014']:
 print zed
# lastvZfolder='../lastv/'+zed+'/'
# command_string = 'ls -1 '+lastvZfolder+'P*S0*[0-9] | egrep -v "P[0-2]p" | egrep -v "/P00[0-7]"'
# os.system(command_string)


#Non-rotating super-solar massive star loop (M>=9 Mo):
for gfile in commands.getoutput('ls -1 '+wg_folder+'P*S[0,4].wg | egrep -v "P[0-2]p" | egrep -v "/P00[0-7]"').split():
  #print(vfile)
  path_gfile = gfile
  print(path_gfile) 
  #os.system("python /lupus/hirschi/data/GESEG/UtilsEvol/CoresCalc.py %s", %(path_vfile))
  #subprocess.check_call(["python /lupus/hirschi/data/GESEG/UtilsEvol/CoresCalc.py ", path_vfile])
  #command_string = 'python CoresCalc_zed.py '+path_vfile
  #os.system(command_string)
  GtB.loadE(path_gfile,key_structures=True)

