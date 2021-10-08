
import folium
from flask import Flask
import geocoder

app = Flask(__name__)

@app.route("/")
def index():
    city = "高雄市"
    gps = geocoder.osm(city).latlng
    m = folium.Map(location=gps, zoom_start=16)
    folium.Marker(gps, popup=city).add_to(m)
    return m.get_root().render()

@app.route("/<address>")
def show(address):
    gps = geocoder.osm(address).latlng
    m = folium.Map(location=gps, zoom_start=16)
    folium.Marker(gps, popup=address).add_to(m)
    return m.get_root().render()
if __name__=='__main__':
    app.run()    
