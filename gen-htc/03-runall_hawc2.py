"""Run all HAWC2 cases in specific file.

Note that some simulations require 12.9 while others are 13.1.
"""
from pathlib import Path
import subprocess


MODEL_DIR = Path('./nrel_5mw/')  # model directory
HTC_RELDIR = Path('htc') / 'lidar_2023-12-12_09-55'  # folder with htc files
HAWC2_129_PATH = './HAWC2_12.9_win32/HAWC2MB.exe'  # relative path to 12.9 HAWC2 executable
HAWC2_NEW_PATH = './HAWC2_13.0.9-2-gd959326_win32/HAWC2MB.exe'  # relative path to new HAWC2 executable

RUN_129 = True  # run 12.9 cases?
RUN_NEW = True  # run new cases?

# get list of htc filepaths (defined with respect to currect directory)
htc_files_129 = [f for f in (MODEL_DIR / HTC_RELDIR).glob('*.htc') if '_v12' in f.as_posix()]
htc_files_new = [f for f in (MODEL_DIR / HTC_RELDIR).glob('*.htc') if '_v12' not in f.as_posix()]

for i, (run, h2_exe, htc_files) in enumerate(zip([RUN_129, RUN_NEW],
                                                 [HAWC2_129_PATH, HAWC2_NEW_PATH],
                                                 [htc_files_129, htc_files_new])):

    # skip run if not requested
    if not run:
        print(f'\nSkipping run with {h2_exe}.\n')
        continue
    else:
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
