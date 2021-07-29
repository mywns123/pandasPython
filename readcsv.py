import pandas as pd
import new_save

# df = pd.read_csv('./data/scientists.csv')
# age = df['Age']
# result = age > age.mean()
# print(age)
# print("=====절취선=====")
# print(age.mean())
# print("=====절취선=====")
# print(result)
# print("=====절취선=====")
# print(age[age > age.mean()])
# print("Age 데이터", age, sep='\n')
# print("=====절취선=====")
# print(age + age)
# print("=====절취선=====")
# print(age * 5)
# print("=====절취선=====")
# age = df['Age']
# Born = df['Born']
# Name = df['Name'].sort_values(ascending=False)
# result1 = age.append(Name)
# result2 = result1.sample()
# print(result1)
# print("=====절취선=====")
# print(result2)
# make_DataFrame = pd.DataFrame(new_save.data)
# age = df['Age']
# new_ages = make_DataFrame['AGE']
# # print(age)
# # print(new_ages)
# print(age+new_ages)

scientist = pd.read_csv('./data/scientists.csv')
# Born = scientist['Born']
# Died = scientist['Died']
# print(Born)
# print("=====절취선=====")
# print(Died)
# print("=====절취선=====")
# Born_change = pd.to_datetime(scientist['Born'], format='%Y/%m/%d')
# print(Born_change)
# print("=====절취선=====")
# Dide_change = pd.to_datetime(scientist['Died'], format='%Y/%m/%d')
# print(Dide_change)
# print("=====절취선=====")
# scientist['Born_change'] = pd.to_datetime(scientist['Born'], format='%Y/%m/%d')
# scientist['Dide_change'] = pd.to_datetime(scientist['Died'], format='%Y/%m/%d')
# print(scientist['Born_change'].describe)
# print(scientist)
# print(scientist['Dide_change'].dtype)
# drop_Born = scientist.drop(['Born', 'Died'], axis=1)
# print(drop_Born)
# print(scientist['Born'] == drop_Born['Born_change'])
# print(scientist['Born'])
# print(drop_Born['Born_change'])
# print(1 == '1')

# name_test = scientist['Name']
# born_test = scientist['Born']
# died_test = scientist['Died']
# age_test = scientist['Age']
# occ_test = scientist['Occupation']
# name_test.to_pickle('./save/name_test.pickle')
# born_test.to_pickle('./save/born_test.pickle')
# died_test.to_pickle('./save/died_test.pickle')
# age_test.to_pickle('./save/age_test.pickle')
# occ_test.to_pickle('./save/occ_test.pickle')
# reading_name = pd.read_pickle('./save/name_test.pickle')
# reading_born = pd.read_pickle('./save/born_test.pickle')
# reading_died = pd.read_pickle('./save/died_test.pickle')
# reading_age = pd.read_pickle('./save/age_test.pickle')
# reading_occ = pd.read_pickle('./save/occ_test.pickle')
# print(reading_name)
# print(reading_born)
# print(reading_died)
# print(reading_age)
# print(reading_occ)
# all_test = scientist
# all_test.to_csv('./save/all_test.csv')
# all_test.to_csv('./save/all_test.tsv', sep='\t')
# reading_all1 = pd.read_csv('./save/all_test.csv')
# reading_all2 = pd.read_csv('./save/all_test.tsv', sep='\t')
# print(reading_all1)
# print(reading_all2)

# scientist.to_excel('./save/excel_test1.xls')
# scientist.to_excel('./save/excel_test2.xlsx')
excel_test1 = pd.read_excel('./save/excel_test2.xlsx')
print(excel_test1)