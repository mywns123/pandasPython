import seaborn as sns
try:
    import matplotlib.pyplot as plt
except ImportError:
    pass
# anscombe = sns.load_dataset('anscombe')
# # print(anscombe)
#
# dataset1 = anscombe[anscombe['dataset'] == 'I']
# dataset2 = anscombe[anscombe['dataset'] == 'II']
# dataset3 = anscombe[anscombe['dataset'] == 'III']
# dataset4 = anscombe[anscombe['dataset'] == 'IV']
#
# fig = plt.figure()
#
# axe1 = fig.add_subplot(1, 4, 1)
# axe2 = fig.add_subplot(1, 4, 2)
# axe3 = fig.add_subplot(1, 4, 3)
# axe4 = fig.add_subplot(1, 4, 4)
#
# axe1.plot(dataset1['x'], dataset1['y'], 'o')
# axe2.plot(dataset2['x'], dataset2['y'], '*')
# axe3.plot(dataset3['x'], dataset3['y'], 's')
# axe4.plot(dataset4['x'], dataset4['y'], '^')
#
# fig.suptitle('Anscombe Data')
# fig.tight_layout()
# axe1.set_title("DataSet I")
# axe2.set_title("DataSet II")
# axe3.set_title("DataSet III")
# axe4.set_title("DataSet IV")
#
# plt.show()

tips = sns.load_dataset('tips')
# print(tips['total_bill'].describe())
#
# fig = plt.figure()
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.hist(tips['total_bill'], bins=10)
# axes1.set_title('Histogram of Total Bill')
# axes1.set_xlabel('Frequency')
# axes1.set_ylabel('Total Bill')
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.scatter(tips['total_bill'], tips['tip'])
# axes1.set_title('Scatter Graph')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')
# plt.show()


# def recode_sex(sex):
#     if sex == 'Female':
#         return 'red'
#     else:
#         return 'blue'
#
#
# tips['sex_color'] = tips['sex'].apply(recode_sex)
# fig = plt.figure()
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.scatter(x=tips['total_bill'], y=tips['tip'], s=tips['size']*10, c=tips['sex_color'], alpha=0.5)
# axes1.set_title('Scatter Graph')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')
# plt.show()



