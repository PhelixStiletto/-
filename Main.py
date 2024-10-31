from django.templatetags.i18n import language
from opencage.geocoder import OpenCageGeocode

def get_coordinates(city,key):
    try:
         geocoder = OpenCageGeocode(key)
         results=geocoder.geocode(city,language='ru')
         if results:
             lat = round (results[0]['geometry']['lat'],2)
             lon = round (results[0]['geometry']['lng'],2)
             return lat,lon
         else:
            return 'Город е найден.'
    except Exception as e:
        return  f'Возникла ошибка {e}'

key = '82f3b2fd29a54869a709e582a85e84b7'
city='Химки'
coordinates = get_coordinates(city,key)
print(f"Координаты города {city}: {coordinates}")

