import os.path
import sys

import tkinter as tk
from tkinter import ttk

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

LARGE_FONT = ("Ubuntu", 12)
VERY_LARGE_FONT = ("Ubuntu", 15)

# Define Functions
def documentation():
    print("access the documentation in html and pdf format !!!")

def onExit(self):
        self.quit()

class ERIN(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, "icons/favicon/favicon.ico")
        tk.Tk.wm_title(self, "ERIN")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    # ***** Main Menu *****

        menubar = Menu(container)
        #self.parent.config(menu=menubar)
        
        # ***** File Menu *****
        
        fileMenu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=fileMenu)
        
        newFileMenu = Menu(fileMenu, tearoff = False)
        fileMenu.add_cascade(label='New', menu=newFileMenu, underline = 0)
        newFileMenu.add_command(label='New File')
        newFileMenu.add_command(label='New Project')

        openFileMenu = Menu(fileMenu, tearoff = False)
        fileMenu.add_cascade(label='Open', menu=openFileMenu, underline = 0)
        openFileMenu.add_command(label='Open File')
        openFileMenu.add_command(label='Open Project')

        openFileMenuRecent = Menu(openFileMenu, tearoff = False)
        openFileMenu.add_cascade(label='Open recent', menu = openFileMenuRecent, underline = 0)
        openFileMenuRecent.add_command(label='File')
        openFileMenuRecent.add_command(label='Project')

        fileMenu.add_command(label='Save')
        fileMenu.add_command(label='Save As ...')
        fileMenu.add_command(label='Import Data')
        fileMenu.add_command(label='Export Data')
        
        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", command=self.onExit)

        # ***** View Menu *****

        viewMenu = Menu(menubar, tearoff=False)        
        menubar.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_separator()
        viewMenu.add_command(label="Settings")

        # ***** Solver Menu *****
        
        solverMenu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Solver", menu=solverMenu)
        solverMenu.add_command(label='D-Wave')
        solverMenu.add_command(label='SU2')

        # ***** Tools Menu *****

        toolsMenu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Tools", menu=toolsMenu)
        macrosToolsMenu = Menu(toolsMenu, tearoff = False)
        toolsMenu.add_cascade(label='Macros', menu = macrosToolsMenu, underline = 0)
        macrosToolsMenu.add_command(label='Import macros in Python 3')

        # ***** Help Menu *****

        helpMenu = Menu(menubar, tearoff = False)
        menubar.add_cascade(label="Help", menu=helpMenu)

        helpMenu.add_command(label="Help Index")

        helpMenu.add_separator()

        submenuHelp = Menu(helpMenu, tearoff = False)
        helpMenu.add_cascade(label="Documentation", menu = submenuHelp, underline = 0)
        submenuHelp.add_command(label="HTML ...", command=documentation)
        submenuHelp.add_command(label="pdf ...", command=documentation)

        tk.Tk.config(self, menu=menubar)

        # Toolbars 
        toolbar = Frame(self)

        self.img = Image.open("icons/wolf.png")
        eimg = ImageTk.PhotoImage(self.img)

        exitButton = Button(toolbar, image=eimg, command=self.quit)
        exitButton.image = eimg
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        # self.parent.config(menu=menubar)
        # self.pack()

        self.centerWindow()

        self.frames = {}

        for F in (ERIN, StartPage, Start):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def centerWindow(self):

        w = 1280
        h = 720

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
   
    def onExit(self):
        self.quit()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text=("""\nERIN\n\n Enclosed inteRdIsciplinary simulatioNs.\nWe are not holding any LEGALLY responsibility on how you are using the information contained in the software.\nAll what you receive and give further is made on your own responsability. \nWe are not warranty that the software will work properlly on your PC.\n"""),
                       font=VERY_LARGE_FONT, justify=CENTER, foreground='red', relief=RIDGE, borderwidth=5)
        label1.pack(pady=89, side=TOP)

        button1 = ttk.Button(self, text="Agree", state=RAISED,   
                             command=lambda: controller.show_frame(Start))
        button1.pack(pady=21, side=TOP, anchor=CENTER)

        button2 = ttk.Button(self, text="Disagree", state=RAISED, 
                             command=self.onExit)
        button2.pack(side=TOP, anchor=CENTER)

    def onExit(self):
        self.quit()

class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=("\n ~ ERIN ~ \n Enclosed inteRdIsciplinary simulatioNs"), font=VERY_LARGE_FONT,
                          justify=CENTER, relief=GROOVE, borderwidth=3)
        label.pack(side=TOP, pady=89, anchor=CENTER)

        button1 = ttk.Button(self, text="Leave App", command=self.onExit)
        button1.pack(side=TOP, anchor=CENTER)

        btn1 = ttk.Button(self, text="D-Wave",
                          command=lambda: controller.show_frame(StartPage))
        btn2 = ttk.Button(self, text="SU2")
        btn3 = ttk.Button(self, text="ParaView")

        btn1.pack(side=LEFT, fill=X, expand=YES, padx=55)
        btn2.pack(side=LEFT, fill=X, expand=YES, padx=55)
        btn3.pack(side=LEFT, fill=X, expand=YES, padx=55)

    def onExit(self):
        self.quit()

app = ERIN()
app.mainloop()
