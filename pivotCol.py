import pandas as pd

pd.set_option('max_columns', None)
# pd.set_option('max_rows', None)

# pew = pd.read_csv('./data/pew.csv')#
# test = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')#
#
# print(pew)
# print('=================================절취선=================================')
# print(test)


# billboard = pd.read_csv('./data/billboard.csv')
#
# billboard_pivot = pd.melt(
#     billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='test', value_name='ttt')
# print(billboard_pivot)

# weather = pd.read_csv('./data/weather.csv')
# weather_pivot = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temperature')
# new_weather = weather_pivot.pivot_table(
#     index=['id', 'year', 'month', 'day'], columns='element', values='temperature', dropna=False)

# print(weather)
# print('=================================절취선=================================')
# print(weather_pivot)
# print('=================================절취선=================================')
# print(new_weather.info())
# print('=================================절취선=================================')
# print(new_weather.reset_index())

# billboard = pd.read_csv('./data/billboard.csv')
# billboard_song = pd.melt(
#     billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='week', value_name='rating')
# billboard_songs = billboard_song[['year', 'artist', 'track', 'time', 'date.entered']]
# billboard_songs = billboard_songs.drop_duplicates()
# print(billboard_song[billboard_song.track == 'Loser'])
# print('=================================절취선=================================')
# print(billboard_songs[billboard_songs.track == 'Loser'])
# print('=================================절취선=================================')
# print(billboard_songs)

# raw_data_urls = pd.read_csv('./data/raw_data_urls.txt')
# print(raw_data_urls.columns)
