import os
import geoip2.database
from geoip2.errors import AddressNotFoundError
import folium
import webbrowser
import plotly.graph_objs as go
from plotly.offline.offline import plot
import tkinter as tk

import settings
import tkinter.messagebox
# from main_window import MainWindow


class Configuration:

    path = {
        # City in China
        'Anhui':'an_hui',
        'Aomen':'ao_men',
        'Beijing':'bei_jing',
        'Chongqing':'chong_qing',
        'Fujian':'fu_jian',
        'Gansu':'gan_su',
        'Guangdong':'guang_dong',
        'Guangxi':'guang_xi',
        'Guizhou':'gui_zhou',
        'Hainan':'hai_nan',
        'Hebei':'he_bei',
        'Henan':'he_nan',
        'Heilongjiang':'hei_long_jiang',
        'Hubei':'hu_bei',
        'Hunan':'hu_nan',
        'Jilin':'ji_lin',
        'Jiangsu':'jiang_su',
        'Jiangxi':'jiang_xi',
        'Liaoning':'liao_ning',
        'Neimenggu':'nei_meng_gu',
        'Ningxia':'ning_xia',
        'Qinghai':'qing_hai',
        'Shandong':'shan_dong',
        'Sichuan':'si_chuan',
        'Taiwan':'tai_wan',
        'Tianjing':'tian_jing',
        'Xizang':'xi_zang',
        'Xianggang':'xiang_gang',
        'Xinjiang':'xin_jiang',
        'Yunnan':'yun_nan',
        'Zhejiang':'zhe_jiang',
        # City in other country
        'America':'America',
        'Australia':'Australia',
        'Brazil':'Brazil',
        'Canada':'Canada',
        'England':'England',
        'Finland':'Finland',
        'France':'France',
        'Germany':'Germany',
        'India':'India',
        'Mexico':'Mexico',
        'Mongolia':'Mongolia',
        'Russia':'Russia',
        'Saudi Arabia':'Saudi Arabia',
        'Singapore':'Singapore',
        'The Philippines':'The Philippines'
    }


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
        print(settings.MAP_TYPE)
        # print(settings.API_KEY)
        try:
            # local_map = folium.Map(location=self.__get_location(),
            #                     zoom_start=12, tiles=settings.MAP_TYPE, API_key=settings.API_KEY)
            if settings.MAP_TYPE == 'custom tileset':
                local_map = folium.Map(location=self.__get_location(),
                                        zoom_start=12, tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png'
                                        , attr='My Data Attribution')
            else:
                if settings.MAP_TYPE == 'Mapbox':
                     
                    fig = dict(
                        data = [
                                    go.Scattermapbox(
                                        mode='markers',
                                        marker=dict(
                                            size=9
                                        )
                                    )
                                ],

                        layout =
                                    go.Layout(
                                        autosize=True,
                                        hovermode='closest',
                                        mapbox=dict(
                                            accesstoken=settings.API_KEY,
                                            bearing=0,
                                            center=dict(
                                            lat=self.__get_location()[1],
                                            lon=self.__get_location()[0]
                                            ),
                                        pitch=0,
                                        zoom=10
                                        ),
                                    )
                        )
                    plot(fig, filename='local_map.html')
                    return
                else:
                    local_map = folium.Map(location=self.__get_location(),
                                    zoom_start=12, tiles=settings.MAP_TYPE)
        except ValueError:
            tkinter.messagebox.showinfo('ValueError:','You must pass an API key if using Cloudmade or non-default Mapbox tiles.')
            print("Failed to open!")
        else:
            local_map.save('local_map.html')
            webbrowser.open('local_map.html')
            print("Successfully open!")

    def insert_info(self, var_infos):#,label_left,label_right):

        response = self.__get_response()
        if response is None:
            var_infos[0].set("The address "+settings.IP+" is not in the database.")
            return

        var_infos[0].set( "IP Info:")

        try:
            continent_names_zh = response.continent.names["zh-CN"]
            country_names_zh = response.country.names["zh-CN"]
            sub_names_zh = response.subdivisions.most_specific.names["zh-CN"]
            city_names_zh = response.city.names["zh-CN"]

        except KeyError:
            var_infos[1].set("Continent: {}({})".format(response.continent.names["es"],
                                                               "None"))
            var_infos[2].set("Country: {}({}) ,iso_code: {}".format(response.country.name,
                                                                           "None",
                                                                           response.country.iso_code))
            var_infos[3].set("State/Province: {}({})".format(response.subdivisions.most_specific.name,
                                                                    "None"))

            var_infos[4].set("City: {}({})".format(response.city.name,
                                                          "None"))
        else:
            var_infos[1].set("Continent: {}({})".format(response.continent.names["es"],
                                                               continent_names_zh))

            var_infos[2].set("Country: {}({}) ,iso_code: {}".format(response.country.name,
                                                                           country_names_zh,
                                                                           response.country.iso_code))

            var_infos[3].set("State/Province: {}({})".format(response.subdivisions.most_specific.name,
                                                                    sub_names_zh))

            var_infos[4].set("City: {}({})".format(response.city.name,
                                                          city_names_zh))

        var_infos[5].set("Longitude: {} ,Latitude: {}".format(response.location.longitude,
                                                                     response.location.latitude))

        var_infos[6].set("Time_zone: {}".format(
            response.location.time_zone))

        var_infos[7].set("Postal code: {}".format(response.postal.code))


        
        '''
        Addons here.
        '''
        try:
           
            m_name = self.path[response.subdivisions.most_specific.name]
            print(m_name)
            
        except KeyError:
            # MainWindow.photo_left = tk.PhotoImage(file='city_scenery/error.png')
            m_name = 'error'
            print('photo_left error')
        else:
            # MainWindow.photo_left = tk.PhotoImage(file='city_scenery/'+
            #                           self.path[response.subdivisions.most_specific.name]+'.png')
            print('photo_left found')

        return m_name

        # MainWindow.label_left = tk.Label(image=MainWindow.photo_left).grid(row=6,column=0,rowspan=8,columnspan=1)
        
        # photo_right = tk.PhotoImage(file='city_description/'+
        #             self.path[response.subdivisions.most_specific.name]+'.png')