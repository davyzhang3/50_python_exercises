def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input ('Enter mm rain: ')
        # rainfall.get(city_name, 0): 
        # Python checks to see if city_name already exists as a key in rainfall.
        #  If so, then the call to rainfall.get will return the value associated with that key. 
        # If city_name is not in rainfall, we get 0 back.
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

        for city, rain in rainfall.items():
            print(f'{city}:{rain}')
get_rainfall()