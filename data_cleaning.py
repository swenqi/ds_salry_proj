#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:38:58 2020

@author: Nikki
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# =============================================================================
#Data Cleansing:
# Salary parsing - only keep numeric part
#   Deleted rows without salary
#   Remove unnecessary str ('Glassdoor est.')
#   Remove 'K' and '$' value to empty str
# Campany name txt only
# State field
# Added a column for if the job was at the company’s headquarters
# Age of company
# Parsing of job description (python, etc.)
# =============================================================================


df.info()

# Salary Parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
miuns_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))
miuns_hr = miuns_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = miuns_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = miuns_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) /2

# Campany name txt only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# State field
df['job_state'] = df['Location'].apply(lambda x: x.split(', ')[1])
#df.job_state.value_counts()

# Added a column for if the job was at the company’s headquarters
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)

# Age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# Parsing of job description (Python, R, Spark, AWS, Excel, SAS, Tableau, GCP, etc.)
df['Job Description'][3]

df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#df['python_yn'].value_counts()

df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() or 'R-Studio' in x else 0)
df['R_yn'].value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark'].value_counts()

df['aws']  = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws'].value_counts()

df['excel']  = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel'].value_counts()

df['sas']  = df['Job Description'].apply(lambda x: 1 if 'sas' in x.lower() else 0)
df['sas'].value_counts()

df['tableau']  = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['tableau'].value_counts()

df['gcp']  = df['Job Description'].apply(lambda x: 1 if 'gcp' in x.lower() else 0)
df['gcp'].value_counts()

df['power_bi']  = df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() else 0)
df['power_bi'].value_counts()

df['sql']  = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['sql'].value_counts()


# Drop Unnamed column
# df.columns
df_out = df.drop(['Unnamed: 0'], axis = 1)
df_out.to_csv('salary_data_cleaned.csv', index = False)
pd.read_csv('salary_data_cleaned.csv')
