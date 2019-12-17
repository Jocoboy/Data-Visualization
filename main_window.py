import tkinter as tk
from tkinter import ttk
import tkinter.font as tf
# from openpyxl.styles.fonts import Font
# from tkinter.ttk import Scrollbar

import settings
from configurations import Configuration


class MainWindow:
    __width = 800
    __height = 600
    __root = tk.Tk()

    def __get_inner_info(self):
        settings.IP = self.var_ip.get()
        settings.MEDIA_ROOT = self.var_media_root.get()
        settings.MAP_TYPE = self.var_map_type.get()
        settings.API_KEY = self.var_api_key.get()

    def __btn_show_msg_click(self):
        #self.edit_text.delete('1.0', 'end')
        self.__get_inner_info()
        Configuration().insert_info(self.var_infos)

    def __btn_web_browser(self):
        self.__get_inner_info()
        Configuration().get_local_map()

    def __init__(self):

        window = self.__root
        width = self.__width
        height = self.__height

        self.var_ip = tk.StringVar()
        self.var_media_root = tk.StringVar()
        self.var_ip.set(settings.IP)
        self.var_media_root.set(settings.MEDIA_ROOT)
        self.var_map_type = tk.StringVar()
        self.var_map_type.set(settings.MAP_TYPE)
        '''
        Plugin here.
        '''
        self.var_api_key = tk.StringVar()
        self.var_api_key.set(settings.API_KEY)


        # Cofigure some basic information for the main window.
        window.title("Geographic Information System")
        window.geometry("%sx%s" % (width, height))
        window.resizable(width=False, height=False)

        # Let the window to be displayed in the center of screen.
        x = int((window.winfo_screenwidth()-width)/2)
        y = int((window.winfo_screenheight()-height)/2)
        window.geometry("%sx%s+%s+%s" % (width, height, x, y))

        # Set the icon for the application.
        window.iconbitmap("images/favicon.ico")

        # Set the canvas for main window.
        canvas_head = tk.Canvas(window, width=width,
                                height=height/3, bg='white')
        image_file_head = tk.PhotoImage(file='images/canvas_head.png')
        image_head = canvas_head.create_image(
            0, 0, anchor='nw', image=image_file_head)
        canvas_head.grid(row=0, column=0, columnspan=3)

        tk.Label(window, text="Input your MEDIA_ROOT:").grid(
            row=1, column=0, pady=5)
        tk.Label(window, text="Input your IP:").grid(
            row=2, column=0, pady=5)
        '''
        Plugin here.
        '''
        tk.Label(window,text="Input yout API_KEY:").grid(
            row=3,column=0,pady=5
        )

        tk.Entry(window, textvariable=self.var_media_root).grid(
            row=1, column=1, columnspan=2, sticky='w'+'e', padx=30)
        tk.Entry(window, textvariable=self.var_ip).grid(
            row=2, column=1, columnspan=1, sticky='w'+'e', padx=30)
        '''
        Plugin here.
        '''
        tk.Entry(window,textvariable=self.var_api_key,show='*').grid(
            row=3,column=1,columnspan=1,sticky='w'+'e',padx=30
        )


        font_style = tf.Font(family="Times", size=10, weight=tf.BOLD)

        self.edit_text = tk.Text(window, font=font_style)
        #self.edit_text = tk.Text(window)
        #self.edit_text.grid(row=4, column=0, rowspan=1, columnspan=3,
        #                    pady=30, ipady=30)
        # scroll_y = Scrollbar(window,command=self.edit_text.yview)
        # self.edit_text.configure(yscrollcommand=scroll_y.set)
        self.label_list = []
        self.var_infos = []
            
        for i in range(5,14):
            self.var_str = tk.StringVar()
            self.var_infos.append(self.var_str)
            self.label = tk.Label(window,text="",textvariable=self.var_str)
            # if i == 13:
            #     self.label.grid(row=i,column=0,columnspan=3,pady=8)
            # else:
            self.label.grid(row=i,column=0,columnspan=3,pady=1)
            self.label_list.append(self.label)
        
            
            

        #font_style = Font(name='Times New Roman', size=11, italic=False, color='FF000000', bold=False)
        box_map_type = ttk.Combobox(
            window, text="Select map type", textvariable=self.var_map_type, state='readonly')
        box_map_type['values'] = ('OpenStreetMap', 'Stamen Terrain', 'Stamen Toner', 'Stamen Watercolor', 'CartoDB positron',
                                  'CartoDB dark_matter', 'Mapbox Bright', 'Mapbox Control Room'
                                  ,'Cloudmade','Mapbox','custom tileset')
        box_map_type.grid(row=2, column=2, columnspan=1)
        btn_web_browser = tk.Button(window, command=self.__btn_web_browser, text="Open in web browser", height=1,
                                    borderwidth=0, cursor='target', bg='#D3D3D3', activeforeground='#A9A9A9')
        btn_web_browser.grid(row=3, column=2, columnspan=1)
        btn_show_msg = tk.Button(window, command=self.__btn_show_msg_click, text="Show geographic information",
                                 height=1, borderwidth=0, cursor='heart', bg='#D3D3D3', activeforeground='#A9A9A9')
        btn_show_msg.grid(row=4, column=1, columnspan=1)

      

        canvas_foot = tk.Canvas(window, width=width,
                                height=height/3/4, bg='white')
        image_file_foot = tk.PhotoImage(file='images/canvas_foot.png')
        image_foot = canvas_foot.create_image(
            0, 0, anchor='nw', image=image_file_foot)
        canvas_foot.grid(row=15, column=0, columnspan=3)

        window.mainloop()
