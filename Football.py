import pandas as pd

df = pd.read_excel('./save/Football_team.xlsx')
# pd.set_option('display.max_columns', None)
print(df.columns)
# df.index = df.index+1
# print(df.sort_values(by='Tournament', ascending=False))
# print(set(df['Tournament'].values))
# df1 = df[['Team', 'Possession%', 'Pass%']].loc[:10]
# df2 = df[['Team', 'Possession%', 'Pass%']].iloc[:10]
# print(df1)
# print(df2)
df3 = df.groupby(['Team'])[['Possession%', 'Pass%']].mean()
print(df3)
print(df3.nunique())