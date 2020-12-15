import shutil
import requests
import pandas as pd


df_in = pd.read_csv('data.csv')
df_in = df_in['profile_pic_url']

for i, url in enumerate(df_in):
    print(i)
    r = requests.get(url, stream=True)
    with open('../icons/%s.jpg' % (i+1), 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
