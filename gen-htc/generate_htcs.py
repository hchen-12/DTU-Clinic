from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from lacbox.htc import HTCFile

# initialize htc file
startPath = '../hawc2-main/3blade_1strut_model'                  # initial (relative) path to the git repo (make sure this is in your home folder) and to the model
modelpath = Path(startPath)                             # path to the model
fname =  modelpath / 'htc/H-rotor_3blades_hmc1strut.htc'          # path from the model to the htc file
htc = HTCFile(fname, modelpath=modelpath)               # create htc file object

# set constant parameters 
windSpeed = 3               # wind speed
htc.wind.wsp = windSpeed    # set wind speed in htc file
rotorR = 0.75               # rotor radius

# generate a series of htc files with varying windspeeds 
for i in range(5):     
    w = [x*windSpeed/rotorR for x in range(5)]                  # list comprehension sets up the desired rotational velocities
    htc.new_htc_structure.constraint.bearing3.omegas = w[i]     # change rotational velocity in htc file
    htc.set_name('wsp3_htc'+str(i))                                # set name for log and results files
    outName = startPath+'/htc/wsp3_htc'+str(int(i))+'_20240408.htc'     # create name to save as
    print(outName)
    htc.save(outName)                                           # save htc files
