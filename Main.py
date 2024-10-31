from opencage.geocoder import OpenCageGeocode

def get_coordinates(city,key):
    try:
         geocoder = OpenCageGeocode(key)
         query = city
         results=geocoder.geocode(query)
         if results:
             return results[0]['geometry']['lat'],results[0]['geometry']['lng']
         else:
            return 'Город е найден.'
    except Exception as e:
        return  f'Возникла ошибка {e}'

key = '82f3b2fd29a54869a709e582a85e84b7'
city='London'
coordinates = get_coordinates(city,key)
print(f"Координаты города {city}: {coordinates}")

