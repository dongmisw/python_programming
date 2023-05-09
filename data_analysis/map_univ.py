
import pandas as pd
import folium
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)

seoul_map.save('./seoul.html')

seoul_map2 = folium.Map(location=[37.51,126.88], tiles='Stamen Terrain', zoom_start=15) # 학교위치.




df = pd.read_excel('https://github.com/dongmisw/python_programming/blob/main/data/seoul_univ.xlsx?raw=true', index_col=0)

seoul_map4=folium.Map(location=[37.55,126.98] , tiles = 'Stamen Terrain', zoom_start=12)

for name, lat, lng in zip (df.index, df.위도, df.경도) : 
    #folium.Marker([lat, lng], popup=name).add_to(seoul_map4)
    folium.CircleMarker([lat, lng],
                        radius=10, 
                        color='brown',
                        fill=True,
                        fill_color='coral',
                        fill_opacity=0.7,
                        popup=name
                        ).add_to(seoul_map4)
seoul_map4.save('seoul_univ.html')
seoul_map4.show_in_browser() 

