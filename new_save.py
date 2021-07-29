import pandas as pd

# exam = ['김지용', 20]
# exam_index = ['name', 'age']
# make_series = pd.Series(exam, exam_index)
# print(make_series)

data = {'NAME': ['TaeYeon', 'Jenny', 'Yuju' ],
        'GROUP': ['SNSD', 'BlackPink', 'GFriend'],
        'RORN': ['1989-03-09', '1996-91-16', '1997-10-04'],
        'AGE': [33, 26, 25],
        'COMPANY': ['SM', 'YG', 'Source_Music']}
index_make = ['1번', '2번', '3번']
make_DataFrame = pd.DataFrame(data, index_make)
# print(make_DataFrame)
# print(make_DataFrame.info())
# one = make_DataFrame.iloc[:2]
# two = make_DataFrame.iloc[2]
# print(two)
# print(type(two))
# print("======================================================================")
# print(one)
# print(type(one))
# print("======================================================================")
# print(two.keys)
# print(two.values)
# print("======================================================================")
# age = make_DataFrame['AGE']
# print(type(age))
# print('AGE의 평균값: ', age.mean())
# print('AGE의 최대값: ', age.max())
# print('AGE의 최소값: ', age.min())
# print('AGE의 표준편차: ', age.std())
# print("======================================================================")
# aa = make_DataFrame.describe()
# print(aa)