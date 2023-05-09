######################
# 5) 지도 관련 나타내기 - USA
#######################

 
import folium
import pandas as pd


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
print(state_unemployment)
state_data = pd.read_csv(state_unemployment)

m = folium.Map(location=[48, -102], zoom_start=3, tiles="Stamen Toner")

folium.Choropleth(
    state_geo,
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)


popup = "Must be on top of the choropleth"

folium.CircleMarker(
    location=[48, -102],
    radius=10,
    fill=True,
    popup=popup,
    weight=1,
).add_to(m)

m.save('folium_usa.html')
m.show_in_browser()

 