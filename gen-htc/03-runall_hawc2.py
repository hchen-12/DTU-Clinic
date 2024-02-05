"""Run all HAWC2 cases in specific file.

Revised from script sent from Jenni on 12 Dec 2023
"""
from pathlib import Path
import subprocess


MODEL_DIR = Path('../hawc2-main/VAWT_model/')  # model directory
HTC_RELDIR = Path('htc')                       # folder with htc files
HAWC2_PATH = '../hawc2-main/HAWC2MB.exe'       # relative path to HAWC2 executable

# get list of htc filepaths (defined with respect to currect directory)
htc_files_list = [f for f in (MODEL_DIR / HTC_RELDIR).glob('*.htc') if 'test' in f.as_posix()] 

for i, (h2_exe, htc_files) in enumerate(zip(HAWC2_PATH, htc_files_list)):

    print(f'\nExecuting run with {h2_exe}.\n')

    # iterate over files and run hawc2
    for i, htc_file in enumerate(htc_files):
        rel_path = HTC_RELDIR / htc_file.name  # path defined w.r.t. model directory
        print(f' Running file {i+1} of {len(htc_files)}...')
        proc = subprocess.run([h2_exe, rel_path], capture_output=True, cwd=MODEL_DIR)
        if proc.returncode:
            print('  FAILED! Error message:')
            print(proc.stderr.decode())
        else:
            print('  Success.')
