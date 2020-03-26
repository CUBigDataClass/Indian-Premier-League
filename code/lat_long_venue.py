import geopy.geocoders
from geopy.geocoders import Nominatim
import ssl
import certifi
import pandas as pd

#/Users/lokin/Documents

match_data = pd.read_csv("../Indian-Premier-League/data/matches/matches_latlong.csv")

# print(match_data.shape)

match_data['venue'] = [x.split(',')[0] for x in match_data['venue']]

# print(match_data['venue'])

places = match_data['venue'].unique()

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

geolocator = Nominatim()

dt = {}

for p in places:
    try:
        location = geolocator.geocode(p)
        dt[p] = [location.latitude, location.longitude]
        # print(location.latitude, location.longitude)
    except:
        dt[p] = [0.0, 0.0]
        # print(0.0,0.0)

dt["Dr DY Patil Sports Academy"] = [19.041944, 73.026667]
dt['OUTsurance Oval'] = [-29.116678, 26.205269]
dt['Barabati Stadium'] = [20.481111, 85.868611]
dt['Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium'] = [17.79751345, 83.35300264041362]
dt['Subrata Roy Sahara Stadium'] = [18.6745, 73.7065]
dt['Shaheed Veer Narayan Singh International Stadium'] = [21.204167, 81.823333]
dt['Rajiv Gandhi International Stadium'] = [17.406528299999998, 78.55048949386448]
dt['Green Park'] = [26.481944, 80.347778]
dt['Newlands'] = [-33.970556, 18.468333]
dt['Kingsmead'] = [-29.850058, 31.027814]
dt['New Wanderers Stadium'] = [-26.131158, 28.057414]
dt['Sardar Patel Stadium'] = [23.042118, 72.564354]

# print(dt)

# ctx = ssl.create_default_context(cafile=certifi.where())
# geopy.geocoders.options.default_ssl_context = ctx
#
# geolocator = Nominatim()
#
def get_lat(row):
    # print(dt[row])
    return dt[row][0]

def get_long(row):
    return dt[row][1]

match_data['latitude'] = match_data['venue'].apply(get_lat)
match_data['longitude'] = match_data['venue'].apply(get_long)


# print(match_data['latitude'])

# print(match_data['longitude'])

match_data.to_csv('../Indian-Premier-League/data/matches/matches_latlong.csv')

# print((location.latitude, location.longitude))

# location = geolocator.reverse("40.741059199999995, -73.98964162240998")

# print(location.address)
# print (location.raw)