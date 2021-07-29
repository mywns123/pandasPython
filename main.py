import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('./data/gapminder.tsv', sep='\t')
# print(type(df))  # df 타입
# print(df.columns)  # df 열
# print(df.dtypes)  # df 열들의 타입
# print(df.info())   # df 모든정보
# print(df.head())   # df 앞5개 출력
# print(df.tail())   # df 뒤5개 출력
# print(df['country'])
# print(df['continent'])
# print(type(df['country']))
# print(type(df['continent']))
# print(type(df))
# choice = df[['country', 'pop']]
# print(type(choice))
# print(choice)
# print(choice.info())
# print(choice.head)

# print(df.loc[:10]) # index"이름" (0 ~ 10) 11개
# print("======================================================================")
# print(df.iloc[:10]) # index순서  (0 ~ 9)  10개
# df.index = df.index+1
# print(df.loc[5])
# print("======================================================================")
# print(df.iloc[4])
# print(df.loc[5] == df.iloc[4])

# print(df[['year', 'country']].iloc[10:101])
# print(df[['year', 'country']].loc[10:100])
# print(df['lifeExp'].mean())
# print(df['lifeExp'].sum())
# print(df['lifeExp'].shape)
# print(df[['lifeExp', 'pop']].mean())
# result = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
# print(result)
#
# df = pd.read_csv('./data/gapminder.tsv', sep='\t')
# df['pop1000000'] = df['pop']/1000000
# df['gdpPercap100'] = df['gdpPercap']/100
# test = df.groupby('year')[['lifeExp', 'pop1000000', 'gdpPercap100']].mean()
# print(test)
# plt.title("gapminder")
# plt.xlabel('year')
# plt.ylabel('number')
# plt.plot(test, '--^', markersize=10)
# plt.show()

