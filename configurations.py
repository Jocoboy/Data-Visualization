import os
import geoip2.database
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
        self.response = reader.city(settings.IP)
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

        edit_text.insert(1.0, "IP Info:\n")

        edit_text.insert(2.0, "Continent: {}({})\n".format(response.continent.names["es"],
                                                           response.continent.names["zh-CN"]))

        edit_text.insert(3.0, "Country: {}({}) ,iso_code: {}\n".format(response.country.name,
                                                                       response.country.names["zh-CN"],
                                                                       response.country.iso_code))

        edit_text.insert(4.0, "State/Province: {}({})\n".format(response.subdivisions.most_specific.name,
                                                                response.subdivisions.most_specific.names["zh-CN"]))

        edit_text.insert(5.0, "City: {}({})\n".format(response.city.name,
                                                      response.city.names["zh-CN"]))

        edit_text.insert(6.0, "Longitude: {} ,Latitude: {}\n".format(response.location.longitude,
                                                                     response.location.latitude))

        edit_text.insert(7.0, "Time_zone: {}\n".format(
            response.location.time_zone))

        edit_text.insert(8.0, "Postal code: {}\n".format(response.postal.code))
