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

    def insert_info(self, var_infos):

        response = self.__get_response()
        if response is None:
            var_infos[1].set("The address "+settings.IP+" is not in the database.")
            return

        var_infos[1].set( "IP Info:")

        try:
            continent_names_zh = response.continent.names["zh-CN"]
            country_names_zh = response.country.names["zh-CN"]
            sub_names_zh = response.subdivisions.most_specific.names["zh-CN"]
            city_names_zh = response.city.names["zh-CN"]

        except KeyError:
            var_infos[2].set("Continent: {}({})".format(response.continent.names["es"],
                                                               "None"))
            var_infos[3].set("Country: {}({}) ,iso_code: {}".format(response.country.name,
                                                                           "None",
                                                                           response.country.iso_code))
            var_infos[4].set("State/Province: {}({})".format(response.subdivisions.most_specific.name,
                                                                    "None"))

            var_infos[5].set("City: {}({})".format(response.city.name,
                                                          "None"))
        else:
            var_infos[2].set("Continent: {}({})".format(response.continent.names["es"],
                                                               continent_names_zh))

            var_infos[3].set("Country: {}({}) ,iso_code: {}".format(response.country.name,
                                                                           country_names_zh,
                                                                           response.country.iso_code))

            var_infos[4].set("State/Province: {}({})".format(response.subdivisions.most_specific.name,
                                                                    sub_names_zh))

            var_infos[5].set("City: {}({})".format(response.city.name,
                                                          city_names_zh))

        var_infos[6].set("Longitude: {} ,Latitude: {}".format(response.location.longitude,
                                                                     response.location.latitude))

        var_infos[7].set("Time_zone: {}".format(
            response.location.time_zone))

        var_infos[8].set("Postal code: {}".format(response.postal.code))
