try:
    import pandas as pd
    from matplotlib import pyplot as plt
except ImportError:
    pass

df = pd.read_csv('./data/waterQuality1.csv')
# print(df.columns)
# print(df)
# print(df['ammonia'].describe())
# # plt.plot(df['aluminium'][0:101], 's', )
# plt.hist(x=df['aluminium'][0:101])
# plt.show()
print(df['aluminium'][0:101])
print(df['aluminium'][0:101].T)
print(df['aluminium'].index)

# ax = plt.subplots()
