"""Run all HAWC2 cases in specific file.

Revised from script sent from Jenni on 12 Dec 2023
"""
from pathlib import Path
import subprocess


MODEL_DIR = Path('./') #../hawc2-main/3blade_1strut_model/')  # model directory
HTC_RELDIR = Path('htc')                       # folder with htc files
HAWC2_PATH = 'hawc2' #'../hawc2-main/HAWC2MB.exe'       # relative path to HAWC2 executable

# get list of htc filepaths (defined with respect to currect directory)
htc_files_list = [f for f in (MODEL_DIR / HTC_RELDIR).glob('*.htc') if '20240408' in f.as_posix()] 

for i in range(len(htc_files_list)):

    h2_exe = HAWC2_PATH
    htc_file = htc_files_list[i]

    print(f'\nExecuting run with {h2_exe}.\n')

    # iterate over files and run hawc2
    
    rel_path = HTC_RELDIR / htc_file.name  # path defined w.r.t. model directory
    print(f' Running file {i+1} of {len(htc_files_list)}...')
    proc = subprocess.run([h2_exe, rel_path], capture_output=True, cwd=MODEL_DIR)
    if proc.returncode:
        print('  FAILED! Error message:')
        print(proc.stderr.decode())
    else:
        print('  Success.')
