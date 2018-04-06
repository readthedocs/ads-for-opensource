#!/usr/bin/env python

"""Generates adblock whitelists based on templates in ``list-templates``."""

import os
import subprocess


BASE_PATH = os.path.dirname(__file__)
OUTPUT_DIR = 'docs/source/_static/lists'
TEMPLATE_DIR = 'list-templates'
TEMPLATES = [
    'opensource-ads.template',
    'readthedocs-ads.template',
]

# Includes in templates are relative
os.chdir(BASE_PATH)

for template in TEMPLATES:
    infile = os.path.join(TEMPLATE_DIR, template)
    outfile = os.path.join(OUTPUT_DIR, template.replace('.template', '.txt'))
    subprocess.check_call([
        'flrender',
        '-i',
        'lists=.',
        infile,
        outfile,
    ])
    print(u'- Wrote whitelist to {}'.format(outfile))
