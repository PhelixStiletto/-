from opencage.geocoder import OpenCageGeocode
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be


def get_coordinates(city,key):
     geocoder = OpenCageGeocode(key)
     query = city
     results=geocoder.geocode(query)
     if results:
         return results[0]['geometry']['lat'],results[0]['geometry']['lng']
     else:
        return 'Город е найден.'

key = '82f3b2fd29a54869a709e582a85e84b7'
city='Moscow'
coordinates = get_coordinates(city,key)
print(f"Координаты города {city}: {coordinates}")

