from tkinter import *

tk=Tk()
#标签控件，显示文本和位图，展示在第一行
Label(tk,text="First").grid(row=0)
Label(tk,text="Second").grid(row=1)#第二行

#输入控件
Entry(tk).grid(row=0,column=1)
Entry(tk).grid(row=1,column=1)


#主事件循环
mainloop()