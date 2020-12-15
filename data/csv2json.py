import re
import json
import numpy as np
import pandas as pd

columns = ['full_name', 'follows_count', 'followed_by_count', 'biography']
df_in = pd.read_csv('data.csv')
df_in = df_in[columns]
df_in['biography'] = df_in['biography'].replace(np.nan, '', regex=True)
df_in['biography'] = df_in['biography'].apply(lambda x: re.sub(r'\n', ' ', x))
df_in['biography'] = df_in['biography'].apply(lambda x: re.sub(r'\s+', ' ', x))
df_in['biography'] = df_in['biography'].apply(str.strip)
data = dict()
for i, entry in enumerate(df_in.values):
    output = '{\n'
    for key, val in zip(columns, entry):
        output += '  \"%s\": \"%s\"\n' % (key, val)
    output += '}'
    data[i+1] = output
with open('data.json', 'w') as f:
    json.dump(data, f)

df_in = pd.read_csv('data.csv')
df_in = df_in['username']
data = dict()
for i, username in enumerate(df_in.values):
    data[i+1] = 'https://www.instagram.com/%s/' % username
with open('url.json', 'w') as f:
    json.dump(data, f)
