#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:52:22 2020

@author: Nikki
"""

import glassdoor_scaper as gs
import pandas as pd

path = "/Users/shiwenqi/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 10, False, path, 15)

# df

df.to_csv('glassdoor_jobs.csv', index = False)

