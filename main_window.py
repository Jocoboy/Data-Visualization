import tkinter as tk
from tkinter import Entry
from openpyxl.styles.fonts import Font

class MainWindow:
    __width = 800
    __height = 600
    __root = tk.Tk()

    def __init__(self):

        window = self.__root
        width = self.__width
        height = self.__height

        # Cofigure some basic information for the main window.
        window.title("Geographic Information System")
        window.geometry("%sx%s" % (width, height))
        window.resizable(width=True, height=True)

        # Let the window to be displayed in the center of screen.
        x = int((window.winfo_screenwidth()-width)/2)
        y = int((window.winfo_screenheight()-height)/2)
        window.geometry("%sx%s+%s+%s" % (width, height, x, y))

        # Set the icon for the application.
        window.iconbitmap("images/favicon.ico")

        # Set the canvas for main window.
        canvas = tk.Canvas(window, width=width, height=height/3, bg='white')
        image_file = tk.PhotoImage(file='images/canvas.png')
        image = canvas.create_image(0, 0, anchor='nw', image=image_file)
        # canvas.pack(side='top')
        canvas.grid(row=0,column=0,columnspan=3)


        tk.Label(window, text="Input your IP:").grid(row=1, column=0,pady=5)
        tk.Label(window, text="Input your MEDIA_ROOT:").grid(row=2, column=0,pady=5)
        tk.Entry(window).grid(row=1, column=1,columnspan=2,sticky='w'+'e',padx=30)
        tk.Entry(window).grid(row=2, column=1,columnspan=1,sticky='w'+'e',padx=30)

        #font_style = Font(name='Times New Roman', size=11, italic=False, color='FF000000', bold=False)
        btn_source_manager = tk.Button(window,text="Open resource manager",height=1,borderwidth=0,cursor='mouse',bg='#D3D3D3',activeforeground='#A9A9A9')
        btn_source_manager.grid(row=2,column=2,columnspan=1)
        btn_web_browser = tk.Button(window,text="Open in web browser",height=1,borderwidth=0,cursor='target',bg='#D3D3D3',activeforeground='#A9A9A9')
        btn_web_browser.grid(row=3,column=2,columnspan=1)
        btn_show_msg = tk.Button(window,text="Show geographic information",height=1,borderwidth=0,cursor='heart',bg='#D3D3D3',activeforeground='#A9A9A9')
        btn_show_msg.grid(row=3,column=1,columnspan=1)

        text = tk.Text(window,height=100)
        text.grid(row=4,column=0,columnspan=3,pady=30,ipady=30,sticky='n')

        window.mainloop()
