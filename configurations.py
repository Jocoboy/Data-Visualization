import os
import geoip2.database
from geoip2.errors import AddressNotFoundError
import folium
import webbrowser

import settings


class Configuration:

    def __init__(self):
        pass

    def __get_response(self):
        settings.FULL_PATH = os.path.join(
            settings.MEDIA_ROOT, 'GeoLite2-City.mmdb')
        reader = geoip2.database.Reader(settings.FULL_PATH)
        try:
            self.response = reader.city(settings.IP)
        except AddressNotFoundError:
            return None
        return self.response

    def __get_location(self):
        response = self.__get_response()
        return [response.location.longitude, response.location.latitude]

    def get_local_map(self):
        local_map = folium.Map(location=self.__get_location(),
                               zoom_start=12, tiles=settings.MAP_TYPE)
        local_map.save('local_map.html')
        webbrowser.open('local_map.html')
        print("Successfully open!")

    def insert_info(self, edit_text):

        response = self.__get_response()
        if response is None:
            edit_text.insert(1.0,"The address "+settings.IP+" is not in the database.")
            return

        edit_text.insert(1.0, "IP Info:\n")

        try:
            continent_names_zh = response.continent.names["zh-CN"]
            country_names_zh = response.country.names["zh-CN"]
            sub_names_zh = response.subdivisions.most_specific.names["zh-CN"]
            city_names_zh = response.city.names["zh-CN"]

        except KeyError:
            edit_text.insert(2.0, "Continent: {}({})\n".format(response.continent.names["es"],
                                                               "None"))
            edit_text.insert(3.0, "Country: {}({}) ,iso_code: {}\n".format(response.country.name,
                                                                           "None",
                                                                           response.country.iso_code))
            edit_text.insert(4.0, "State/Province: {}({})\n".format(response.subdivisions.most_specific.name,
                                                                    "None"))

            edit_text.insert(5.0, "City: {}({})\n".format(response.city.name,
                                                          "None"))
        else:
            edit_text.insert(2.0, "Continent: {}({})\n".format(response.continent.names["es"],
                                                               continent_names_zh))

            edit_text.insert(3.0, "Country: {}({}) ,iso_code: {}\n".format(response.country.name,
                                                                           country_names_zh,
                                                                           response.country.iso_code))

            edit_text.insert(4.0, "State/Province: {}({})\n".format(response.subdivisions.most_specific.name,
                                                                    sub_names_zh))

            edit_text.insert(5.0, "City: {}({})\n".format(response.city.name,
                                                          city_names_zh))

        edit_text.insert(6.0, "Longitude: {} ,Latitude: {}\n".format(response.location.longitude,
                                                                     response.location.latitude))

        edit_text.insert(7.0, "Time_zone: {}\n".format(
            response.location.time_zone))

        edit_text.insert(8.0, "Postal code: {}\n".format(response.postal.code))
