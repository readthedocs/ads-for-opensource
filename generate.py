#!/usr/bin/env python
import os
import subprocess


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = 'readthedocs.template'
OUTPUT_PATH = os.path.join('output', 'readthedocs-ads.txt')

# Includes in readthedocs.template are relative
os.chdir(BASE_PATH)

subprocess.check_call([
    'flrender',
    '-i',
    'readthedocs=.',
    INPUT_PATH,
    OUTPUT_PATH,
])
print(u'Wrote output list to {}'.format(OUTPUT_PATH))
