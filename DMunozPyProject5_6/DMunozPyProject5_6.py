import geocoder

#forward geocoding
print("Forward Lookup")
g = geocoder.osm('Phoenix, Az')
print(g.latlng)
#print(g.postal)
print(g.country)
print("\n")

#reverse geocoding example
print("Reverse Lookup")
g = geocoder.arcgis([51.5074, -0.1278], method='reverse')
print(g.city)
print(g.state)
print(g.country)
print("\n")

#ip address 1
print("IP Address 1")
g = geocoder.ip('8.8.8.8')
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + ", " + g.state)
print("\n")

#ip address 2
print("IP Address 2")
g = geocoder.ip('me')
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + ", " + g.state)
print("\n")

#house address
print("House Address")
g = geocoder.osm("1600 Pennsylvania Avenue NW, Washington D.C.")
print(g.housenumber)
print(g.postal)
print(g.street)
print(g.city)
print(g.state)
print(g.country)
