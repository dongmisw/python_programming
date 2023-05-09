 
######################
# 6) 지도 관련 나타내기 _korea
#######################

import pandas as pd
import folium 
  
#state_geo = 'C:\\Users\\user\\Downloads\\Folium_Test\\korea.json'
state_geo='https://raw.githubusercontent.com/dongmisw/python_programming/main/data/korea.json'

#state_unemployment = 'C:\\Users\\user\\Downloads\\Folium_Test\\Total_People_2018.csv'
state_unemployment = 'https://raw.githubusercontent.com/dongmisw/python_programming/main/data/Total_People_2018.csv'
state_data = pd.read_csv(state_unemployment, encoding = 'euc-kr')
  
m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)
 
# Add the color for the chloropleth:

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['Code', 'Population'],
 key_on='feature.properties.SIG_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('folium_kr.html')
m.show_in_browser() 
