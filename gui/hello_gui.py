#!/usr/bin/env python3 

#-*-coding:utf-8-*-

from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        #Frame.__init__(self,master)
        super(Application,self).__init__(master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

#app=Application()
#app.master.title('Hello World')
#app.mainloop()


import tkinter.messagebox as messagebox

class NewApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app1=NewApplication()
app1.master.title('Hello World')
app1.mainloop()



