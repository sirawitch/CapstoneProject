import pandas as pd
df = pd.read_csv('WebScrap/DataWithOtherData.csv')
next_df = pd.read_csv('WebScrap/DataWithOtherData2.csv')
df = pd.concat([df, next_df], ignore_index=True)
next_df = pd.read_csv('WebScrap/DataWithOtherData3.csv')
df = pd.concat([df, next_df], ignore_index=True)
df.to_csv('WebScrap/DataWithOtherDataAll.csv')