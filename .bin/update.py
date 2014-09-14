#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Vítor Brandão <vitor@noiselabs.org>

import subprocess
import os
import sys

cwd = os.path.dirname(os.path.abspath(__file__))
ghost_url = 'http://127.0.0.1:2368/'

os.chdir(cwd + '/..')

sys.stdout.write('Collecting HTML from %s\n' % ghost_url)
subprocess.call(['buster', 'generate', '--domain=%s' % ghost_url, '--dir=.'])

subprocess.call(['buster', 'preview', '--dir=.'])

sys.exit(0)
