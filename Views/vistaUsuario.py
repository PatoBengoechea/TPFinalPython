from tkinter import ttk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

def main():

    root = Tk()
    app = Ventana1(root)

class Ventana1:

    def __init__(self, master):

        self.master = master
        self.master.title('Ingreso de Usuario')
        self.master.geometry('700x200+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        user = StringVar()
        password = StringVar()



        #====================================Variables===========================================================



        #=====================================Frames================================================================

        self.buscador = Frame(self.frame, width= 300, height= 50)
        self.buscador.grid(row=0, column=1)

        self.loginUsuarioL = Frame(self.frame, width= 300, height= 50)
        self.loginUsuarioL.grid(row=1, column=1)

        self.loginUsuarioE = Frame(self.frame, width= 300, height= 50)
        self.loginUsuarioE.grid(row=1, column=2)

        self.loginPassL = Frame(self.frame, width= 300, height= 50)
        self.loginPassL.grid(row=2, column=1)

        self.loginPassE = Frame(self.frame, width= 300, height= 50)
        self.loginPassE.grid(row=2, column=2)

        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=5, column=1)

        #======================================Labels and Entries=================================================================
        self.datoOp = Label(self.loginUsuarioL, text='Usuario: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.loginUsuarioE, textvariable=user)
        self.usuario.grid(row= 0, column=0)

        self.datoOp = Label(self.loginPassL, text='Contraseña: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.loginPassE, textvariable=password, show='*')
        self.usuario.grid(row= 0, column=0)

        #===========================================Botones============================================================

        self.btnDetalles = Button(self.botones, text='Ingresar', command = lambda: self.ingresar())
        self.btnDetalles.grid(row=1, column= 1)

        self.btnGraficar = Button(self.botones, text='Nuevo', command = lambda: self.nuevoUsuario())
        self.btnGraficar.grid(row=1, column= 2)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 3)

        #=====================================Buscador===========================================================


        self.master.mainloop()

    def ingresar(self):
        pass

    def nuevoUsuario(self):
        pass


main()
