try:
    import pandas as pd
except ImportError:
    pass
# df1 = pd.read_csv('./data/concat_1.csv')
# df2 = pd.read_csv('./data/concat_2.csv')
# df3 = pd.read_csv('./data/concat_3.csv')
#
# total = pd.concat([df1, df2, df3])
#
# new_Series = pd.Series(['new1', 'new2', 'new3', 'new4'])
# result = pd.concat([total, new_Series])
#
# new_DataFrame ={
#     'A': ['new1'],
#     'B': ['new2'],
#     'C': ['new3'],
#     'D': ['new4']
# }
# make_Frame = pd.DataFrame(new_DataFrame)
# result1 = pd.concat([total, make_Frame])
# result1 = total.append(new_DataFrame, ignore_index=True)
# print(result1)
#
# df1.columns = ['A', 'B', 'C', 'D']
# df2.columns = ['E', 'F', 'G', 'H']
# df3.columns = ['A', 'C', 'F', 'H']
#
# total_row = pd.concat([df1, df2, df3], axis=0)
# total_attr = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
#
# print(total_row)
# print('=====================================================')
# print(total_attr)

# total_row = pd.concat([df1, df2, df3])
# df1_df3 = pd.concat([df1, df3], join='inner', ignore_index=True)
# df2_df3 = pd.concat([df2, df3], join='inner', ignore_index=True)
# print(df1_df3)
# print(df2_df3)

# data1 = {'NAME': ['TaeYeon', 'Jenny', 'Yuju'],
#         'GROUP': ['SNSD', 'BlackPink', 'GFriend'],
#         'RORN': ['1989-03-09', '1996-91-16', '1997-10-04'],
#         'AGE': [33, 26, 25],
#         'COMPANY': ['SM', 'YG', 'Source_Music'],
#         'TEST1': ['t1', 't2', 't3']}
#
# df1 = pd.DataFrame(data1)
#
#
# data2 = {'NAME': ['태연', 'Jenny', 'Yuju'],
#         'GROUP2': ['SNSD', 'BlackPink', 'GFriend'],
#         'RORN2': ['1989-03-09', '1996-91-16', '1997-10-04'],
#         'AGE2': [33, 26, 25],
#         'COMPANY2': ['SM', 'YG', 'Source_Music'],
#         'TEST2': ['t1', 't2', 't3']}
#
# df2 = pd.DataFrame(data2)
# print(df1['NAME'])
# print(df2['NAME'])
# total = pd.merge(df1['NAME'], df2['NAME'])
# total = pd.merge(df1, df2)
# print(total)

# person = pd.read_csv('./data/survey_person.csv')
# site = pd.read_csv('./data/survey_site.csv')
# visited = pd.read_csv('./data/survey_visited.csv')
# survey = pd.read_csv('./data/survey_survey.csv')
# print(person)
# print(survey)
# merge_example = person.merge(survey, left_on='ident', right_on='person')
# # merge_example = person.merge(visited, left_on='ident', right_on='site')
# print(merge_example)

evola = pd.read_csv('./data/country_timeseries.csv')
# print(evola.isnull().sum())  # Nan값의 수
# evola_parts = evola.iloc[:10, :5]
# print(evola_parts)
# print('=================================절취선=================================')
# print(evola_parts.fillna(0))  # 0대체
# print('=================================절취선=================================')
# print(evola_parts.fillna(method='ffill'))  # 앞의 숫자로 채움
# print('=================================절취선=================================')
# print(evola_parts.fillna(method='bfill'))  # 뒤의 숫자로 채움
# print('=================================절취선=================================')
# print(evola_parts.interpolate())  # 평균값(보간)로 채움
# print('=================================절취선=================================')
# print(evola_parts.dropna())  # Nan값 삭제
three_country = evola.loc[:10, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone']]
# print(three_country)
evola['country_sum'] = evola['Cases_Guinea'] + evola['Cases_Liberia'] + evola['Cases_SierraLeone']
c_sum = evola.loc[:10, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'country_sum']]
print(c_sum)
