import tkinter as tk
import os

class Botao(tk.Label):
    def __init__(self, mst, text='', colors=('gray30', 'gray50', 'gray30'), w= 15):
        super().__init__()
        self['text'] = text
        self['width'] = w
        self['height'] = 5
        self.colors = colors
        self['bg'] = self.colors[0]
        self['fg'] = 'white'
        
        self['font']= 'Arial 12 bold'
        self.bind('<Button-1>', self.click)
        self.bind('<Enter>', self.entrou)
        self.bind('<Leave>', self.saiu)
    def click(self, evt):

        self['bg'] = self.colors[2]
        txt = cont.get()
        c = str(self['text'])

        if c == '=':
        	#txt = txt.replace('/','//')
        	try: # syntax error
        		cont.set(eval(txt)) # execute expression and print result
        	except:
        		cont.set('Error') 
        else:   
            if(c != 'AC'): # clear screen
                cont.set(txt+c)
            else:
                cont.set('')
        

    def entrou(self, evt):
        self['bg'] = self.colors[1]
    def saiu(self, evt):
        self['bg'] = self.colors[0]

## WINDOW CONFIG ##
win = tk.Tk()
win.title('PyCalc')
file = 'icon.png'
win.iconphoto(False, tk.PhotoImage(file=file))
win.resizable(False,False)
win.config(bg='gray30')

## SCREEN ##
cont = tk.StringVar()
cont.set('')
tela = tk.Label(win, width=17, height=3, bg='gray20', textvariable=cont, anchor=tk.SE, fg='white', justify=tk.RIGHT)
tela['font']= 'Arial 44 bold'
tela.grid(columnspan=4)

##CLEAN SCREEN ##
Botao(win, 'AC', w=30).grid(column=0, row=1, columnspan=2)
## MOD
Botao(win, '%').grid(column=2, row=1)

### NUNBERS ###
n = 10
for i in range(2,6):
    for j in range(2,-1,-1):
            if n > 1:
               n-=1
               Botao(win, n).grid(row=i, column=j)
                
Botao(win, '0', w=30).grid(columnspan=2,column=0, row=5)


## POINT DECIMAL##
Botao(win, '.').grid(column=2,row=5)
op = '/*-+='

### OPERATORS ###
for i in range(1,6):                #orange scale
    t = Botao(win,op[i-1],('#FFA500', '#FF8C00', '#FF4500'))
    t.grid(column=3, row=i)

win.mainloop()
