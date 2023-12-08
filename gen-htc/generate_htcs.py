from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from lacbox.htc import HTCFile

# initialize htc file
startPath = 'DTU-Clinic'                                # initial path to the git repo (make sure this is in your home folder)
modelpath = Path(startPath) / 'hawc2-main/VAWT_model'   # path from git repo to the model
fname =  modelpath / 'htc/H-rotor_3blades.htc'          # path from the model to the htc file
htc = HTCFile(fname, modelpath=modelpath)               # create htc file object

# create a series of htc files with different windspeeds 
