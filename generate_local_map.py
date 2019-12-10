import folium
import pandas as pd

import os
import geoip2.database
import settings
import main_window

import webbrowser


def show_info(response):
    print("IP Info:")

    print("Continent: {}({})".format(response.continent.names["es"],
                                     response.continent.names["zh-CN"]))

    print("Country: {}({}) ,iso_code: {}".format(response.country.name,
                                                 response.country.names["zh-CN"],
                                                 response.country.iso_code))

    print("State/Province: {}({})".format(response.subdivisions.most_specific.name,
                                          response.subdivisions.most_specific.names["zh-CN"]))

    print("City: {}({})".format(response.city.name,
                                response.city.names["zh-CN"]))

    print("Longitude: {} ,Latitude: {}".format(response.location.longitude,
                                               response.location.latitude))

    print("Time_zone: {}".format(response.location.time_zone))

    print("Postal code: {}".format(response.postal.code))


def get_location(ip):
    path = os.path.join(settings.MEDIA_ROOT, 'GeoLite2-City.mmdb')
    reader = geoip2.database.Reader(path)
    response = reader.city(ip)

    show_info(response)

    return [response.location.longitude, response.location.latitude]


def main():

    window = main_window.MainWindow()

    local_map = folium.Map(location=get_location(
        settings.IP), zoom_start=13, tiles='Stamen Toner')
    local_map.save('local_map.html')
    webbrowser.open('local_map.html')


if __name__ == "__main__":
    main()
