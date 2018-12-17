# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("sample_group.csv")

df_grouped = df.groupby(["class", "sex"])

print(df_grouped.groups)
print(df_grouped.get_group(('A', 'F')))

for (class_, sex_), df_split in df_grouped:
    print(class_, sex_)

try:
    print(df_grouped.get_group(('G', 'F')))    
except KeyError as instance:
    print("key error: {}".format(instance))


    


