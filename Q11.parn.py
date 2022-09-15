import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = r'C:\Users\gati6\Desktop\Python\Data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    lats, lons, brightnesses, hover_texts = [], [], [], []
    for row in reader:
        lat = row[0]
        lon = row[1]
        brightness = float(row[2])
        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)
    hover_texts = brightnesses              #เอาออกเเทปหนึ่ง
        
# Map the world fire
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/50 for brightness in brightnesses],
        'color' : brightnesses,
        'colorscale': 'sunsetdark',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
        
    },
}]

my_layout = Layout(title='World Fires')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='world_fires.html')
