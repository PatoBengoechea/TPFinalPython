from tkinter import ttk
from tkinter import *
from Controller.UserController import UserController
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
from Views.vistaNuevoUsuario import Ventana2

from Views.prueba import armarListadoDeTrades #borrar

class Ventana3:

    def __init__(self, master, user, name, surname):

        self.master = master
        self.master.title('Panel Principal')
        self.master.geometry('1000x500+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.user = user
        self.name = name
        self.surname = surname

        self.mercado = 'DODic19' #borrar
        self.trades = armarListadoDeTrades(self.mercado) #borrar


        #=====================================Frames================================================================
        ubF = 0

        self.buscador = Frame(self.frame, width= 300, height= 50)
        self.buscador.grid(row=ubF, column=1)

        ubF = ubF + 1

        self.UsuarioL = Frame(self.frame, width= 300, height= 50)
        self.UsuarioL.grid(row=ubF, column=4)

        ubF = ubF + 1

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.tvw = Frame(self.frame, width= 300, height= 50)
        self.tvw.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.spaceF2 = Frame(self.frame, width= 300, height= 50)
        self.spaceF2.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=ubF, column=1)


        #======================================Labels and Entries=================================================================
        self.datoOp = Label(self.UsuarioL, text=(self.name + ' ' + self.surname), background= 'pale green')
        self.datoOp.grid(row= 0, column=0)


        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)


        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.tvw)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two","three","four")

        vsb = ttk.Scrollbar(self.tv, orient="vertical", command=self.tv.yview)
        vsb.place(x=30+355+2, y=20, height=200)

        #====================================TVColums==============================================================
        self.tv.column("one", width=200 )
        self.tv.column("two", width=100, anchor="e")
        self.tv.column("three", width=100)
        self.tv.column("four", width=100)

        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="Fecha")
        self.tv.heading("two", text="Precio")
        self.tv.heading("three", text="Apellido")
        self.tv.heading("four", text="DNI")

        #===============================Prueba de insertar datos================================================

        self.listar()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        #===========================================Botones============================================================

        ubBot = 1

        self.btnOperaciones = Button(self.botones, text='Operaciones', background= 'aquamarine', command = "")
        self.btnOperaciones.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn = Label(self.botones)
        self.spaceBtn.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnCocechas = Button(self.botones, text='Cocechas', background= 'medium aquamarine', command ="")
        self.btnCocechas.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn2 = Label(self.botones)
        self.spaceBtn2.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= ubBot)

        #=====================================Buscador===========================================================


        self.master.mainloop()

    def listar(self):

        self.tv.delete(*self.tv.get_children())

        print(self.trades)

        for t in self.trades['trades']:
            self.tv.insert("" , 0, values=(t['datetime'],t['price']))

        self.tv.pack()



