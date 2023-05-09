
import pandas as pd
import folium
import json
import urllib.request
#file_path = 'C:\\Users\\user\\Documents\\workspace\\2023\\python_programming\\population.xlsx'
file_path="https://github.com/dongmisw/python_programming/blob/main/data/population.xlsx?raw=true" 
df = pd.read_excel(file_path, index_col='구분')
df.columns = df.columns.map(str)

'''
#file에서 읽어올때
geo_path='C:\\Users\\user\\Documents\\workspace\\2023\\python_programming\\00\\gyonggido.json'
try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))
'''

#url에서 읽어올때
url = 'https://raw.githubusercontent.com/dongmisw/python_programming/main/data/gyonggido.json'
text_data = urllib.request.urlopen(url).read().decode('utf-8')
geo_data = json.loads(text_data) 

g_map = folium.Map(location=[37.5502, 126.982],
                   tiles='Stamen Terrain',
                   zoom_start=9)

year ='2007'
folium.Choropleth(geo_data=geo_data,
                  data= df[year],
                  columns = [df.index, df[year]],
                  fill_color='YlOrRd',
                  fill_opacity=0.7,
                  line_opacity= 0.3,
                  threshold_scale=[10000,100000,300000, 500000, 700000],
                  key_on='feature.properties.name',
                  ).add_to(g_map)

g_map.save('gyonggi_population_'+year+'.html')
g_map.show_in_browser() 