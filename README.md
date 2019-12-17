# Geographic Information System (GIS)

A light system to query map infomation based on IP, yet to be advised.

## :mag:Preview

### Main Window

<img src="preview2.0.png" style="width: 100%;" align="center" />

### Map in Web Browser

<img src="local_map-2.png" style="width: 100%;" align="center" />

## :nut_and_bolt:Dependencies

- Python 3.7
    ```
    pip install folium
    pip install geoip2
    pip install plotly
    ```
    For demestic user, please use pypi mirror ```pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package``` instead.
- MaxMind DataBase [GeoLite2-City](https://dev.maxmind.com/geoip/geoip2/geolite2/)

## :pencil:Usage

- MEDIA_ROOT: 
        The root path of the offline database GeoLite2-City.
- IP:
        Since IP is unique worldwide, we establish the mapping relations between IP and Geographic Information.
- MAP_TYPE:
        ``folium`` builds on the mapping strengths of the ``leaflet.js`` library. The library has a number of built-in tilesets from ***OpenStreetMap***, ***Stamen Terrain***, ***Stamen Toner***, ***Stamen Watercolor***, ***CartoDB positron***, ***CartoDB dark_matter***, ***Mapbox Bright***, ***Mapbox Control Room***, and supports custom tilesets with [***Mapbox***](https://www.mapbox.com/) or [***Cloudmade***](https://cloudmade.com/) API keys. You can just select one and open in your web browser.

- API_KEY:
        API keys is a must if you choose custom tilesets with Mapbox or Cloudmade. Here we use ``plotly.graph_objs`` and ``plotly.offline.offline`` to plot local maps if you have passed the mapbox accesstoken. Note that Cloudmade is not available temporarily.

- custom tileset:
        ``folium`` supports passing any ``leaflet.js`` compatible custom tileset. Before you choose a custom tileset, you are supposed to configure ``tiles`` and ``attr``
        ```
        tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png', attr='My Data Attribution'
        ```
        at ``Configuration.get_local_map()`` in ``configurations.py``.

## :octocat:Contributors

[@Jocoboy](https://github.com/Jocoboy)

[@outputlimitexceed](https://github.com/outputlimitexceed)