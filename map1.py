import folium
import pandas

map = folium.Map(location=[33.888098263578, 35.49224025579559], zoom_start=2)

fg = folium.FeatureGroup(name="FG1")

data = pandas.read_csv('./Volcanoes.txt')
data_lat = data['LAT']
data_lon = data['LON']
data_elev = data['ELEV']
data_name = data['NAME']

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
Height: %s m
"""

def marker_elevation_color(elev):
  if elev < 1000:
    return 'green'
  if elev < 3000:
    return 'orange'
  return 'red'

for lat,lon,elev,name in zip(data_lat,data_lon,data_elev,data_name):
  fg.add_child(folium.CircleMarker(radius=6,location=[lat,lon], popup=folium.Popup(folium.IFrame(html=html % (name,name,str(elev)),width=200,height=200)), opacity=0.9, fill_opacity=0.8, weight=1, color='black', fill_color=marker_elevation_color(elev)))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fg)
map.save("Map1.html")

