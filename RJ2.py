import json
import pandas as pd

with open('catalog.json',encoding='utf-8') as file:
    jsn=json.load(file)
    
    for i in jsn:
        jk=[jk for jk in jsn if jk['name']=='jacket']
    
    df=pd.DataFrame(jk)
    
    print(len(df))
    print(max(df['price']))
    print(min(df['price']))