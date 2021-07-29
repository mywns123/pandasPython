import seaborn as sns
import pandas as pd
import numpy as np

# tips = sns.load_dataset('tips')
# print("['sex'].memory :", tips['sex'].memory_usage())
# tips['sex'] = tips['sex'].astype(object)
# print('=================================절취선=================================')
# print("['sex'].memory :", tips['sex'].memory_usage())
# print(tips['total_bill'].loc[[1, 2]].dtype)
# tips.loc[[1, 2], 'total_bill'] = '오입력'
# print('=================================절취선=================================')
# print(tips['total_bill'].loc[[1, 2]].dtype)
# print(tips['total_bill'].astype(float))
# print(pd.to_numeric(tips['total_bill'], errors='ignore'))
# a = pd.to_numeric(tips['total_bill'], errors='coerce')
# print(a)
# tips['total_bill'] = a
# print(tips.dtypes)


# def my_sq(x):
#     return x ** 2
#
#
# def my_exp(x, n):
#     return x ** n
#
#
# def avg_3(col):
#     x = col[0]
#     y = col[1]
#     z = col[2]
#     return (x+y+z)/3
#
#
# df = pd.DataFrame({'a': [10, 20, 30],
#                    'b': [20, 30, 40]})
#
# result1 = df['a'].apply(my_sq)
# print(result1)
#
# result2 = df['a'].apply(my_exp, n=3)
# print(result2)
#
# result3 = df.apply(avg_3)
# print(result3)

titanic = sns.load_dataset('titanic')


def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count


def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return (num/dem) * 100


def prop_complete(vec):
    return 1 - prop_missing(vec)


# cmis_col = titanic.apply(count_missing)
# print(cmis_col)
# print('=================================절취선=================================')
# pmis_col = titanic.apply(prop_missing)
# print(pmis_col)

titanic['num_missing'] = titanic.apply(count_missing, axis=1)
# print(titanic)
print(titanic.loc[titanic['num_missing'] > 1, :])