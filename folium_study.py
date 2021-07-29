import folium
import pandas as pd

# daegu_map = folium.Map(location=[35.87, 128.60], zoom_start=12)
# daegu_map.save('./save/daegu_map.html')
#
# daegu_map1 = folium.Map(location=[35.87, 128.60], zoom_start=12, tiles='Stamen Terrain')
# daegu_map1.save('./save/daegu_map1.html')
#
# daegu_map2 = folium.Map(location=[35.87, 128.60], zoom_start=12, tiles='Stamen Toner')
# daegu_map2.save('./save/daegu_map2.html')

df = pd.read_excel('./data/영남인재교육원위치.xlsx')
youngnam_map = folium.Map(location=[35.87, 128.60], zoom_start=13)
print(df['Unnamed: 0'])
print(df.index)

for name, lat, lng in zip(df['Unnamed: 0'], df.위도, df.경도):  # ['Unnamed: 0']
    folium.Marker([lat, lng], popup=name).add_to(youngnam_map)

youngnam_map.save('./save/youngnam.html')
