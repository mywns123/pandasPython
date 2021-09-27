import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')
# print(df.mean())
# print(df.median())
# print(df.std())
# print(df.corr())

test = df[['year', 'lifeExp', 'pop']].corr()
print(test)