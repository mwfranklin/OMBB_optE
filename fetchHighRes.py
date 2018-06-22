import os
import numpy as np
import glob

with open("HighRes_OMBBs.txt", "r") as DBlist:
    DBlist = DBlist.readlines()

DBlist = [value.strip("\n") for value in DBlist]
#print(DBlist)

"""for value in DBlist:
    os.system("curl https://files.rcsb.org/download/%s.pdb -o PDBs/%s.pdb" %(value, value))
    os.system("gzip PDBs/%s.pdb" %value)
    #os.system("./reduce -HIS -NOADJust %s.pdb > %sH.pdb" % (value, value))
"""    
with open("HighRes_OMBB_inputs.txt", "w+") as outData:
    for value in DBlist:
        outData.write("inputs/%s.pdb.gz\n"%value)