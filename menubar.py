import tkinter as tk

class Menubar(tk.Menu):
    def __init__(self, mst):
        super().__init__()
        self['bg'] = 'gray30'
        self['fg'] = '#ffffff'
        self['font'] = 'Arial 10 bold'
        self.__create_optmenu(mst)
        mst.config(menu=self)

    def __create_optmenu(self, mst):
        optmenu = tk.Menu(self, tearoff=0, bg='gray30', fg='#ffffff', font='Arial 10 bold')
        optmenu.add_command(label='Help')
        optmenu.add_separator()
        optmenu.add_command(label='Exit',command=mst.quit)
        self.add_cascade(label='Option', menu=optmenu)