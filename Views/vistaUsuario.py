from tkinter import ttk
from tkinter import *
#from Controller.UserController import UserController
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
        self.loginUsuarioL.grid(row=1, column=0)

        self.loginUsuarioE = Frame(self.frame, width= 300, height= 50)
        self.loginUsuarioE.grid(row=1, column=1)

        self.loginPassL = Frame(self.frame, width= 300, height= 50)
        self.loginPassL.grid(row=2, column=0)

        self.loginPassE = Frame(self.frame, width= 300, height= 50)
        self.loginPassE.grid(row=2, column=1)

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=4, column=0)

        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=5, column=1)

        #======================================Labels and Entries=================================================================
        self.datoOp = Label(self.loginUsuarioL, text='Usuario: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.loginUsuarioE, textvariable=user)
        self.usuario.grid(row= 0, column=0)

        self.datoOp = Label(self.loginPassL, text='Contraseña: ')
        self.datoOp.grid(row= 0, column=0)

        self.password = Entry(self.loginPassE, textvariable=password, show='*')
        self.password.grid(row= 0, column=0)

        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        #===========================================Botones============================================================

        self.btnIngresar = Button(self.botones, text='Ingresar', background= 'DeepSkyBlue2',command = lambda: self.ingresar())
        self.btnIngresar.grid(row=1, column= 1)

        self.btnNuevoUsuario = Button(self.botones, text='Nuevo', background= 'pale green',command = lambda: self.nuevoUsuario())
        self.btnNuevoUsuario.grid(row=1, column= 2)

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 3)

        #=====================================Buscador===========================================================


        self.master.mainloop()

    def ingresar(self):
        pass

    def new_window(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana2(self.newWindow)

    def nuevoUsuario(self):
        self.new_window()


class Ventana2:


    def __init__(self, master):

        self.master = master
        self.master.title('Nuevo Usuario')
        self.master.geometry('600x300+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        user = StringVar()
        password = StringVar()
        name = StringVar()
        surname = StringVar()

        #====================================Variables===========================================================

        #=====================================Frames================================================================

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=1, column=1)

        self.createUsuarioL = Frame(self.frame, width= 300, height= 50)
        self.createUsuarioL.grid(row=2, column=1)

        self.createUsuarioE = Frame(self.frame, width= 300, height= 50)
        self.createUsuarioE.grid(row=2, column=2)

        self.createPassL = Frame(self.frame, width= 300, height= 50)
        self.createPassL.grid(row=3, column=1)

        self.createPassE = Frame(self.frame, width= 300, height= 50)
        self.createPassE.grid(row=3, column=2)

        self.createNameL = Frame(self.frame, width= 300, height= 50)
        self.createNameL.grid(row=4, column=1)

        self.createNameE = Frame(self.frame, width= 300, height= 50)
        self.createNameE.grid(row=4, column=2)

        self.createSurnameL = Frame(self.frame, width= 300, height= 50)
        self.createSurnameL.grid(row=5, column=1)

        self.createSurnameE = Frame(self.frame, width= 300, height= 50)
        self.createSurnameE.grid(row=5, column=2)

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=6, column=2)

        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=7, column=2)

        #======================================Labels and Entries=================================================================
        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        self.datoOp = Label(self.createUsuarioL, text='Usuario: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.createUsuarioE, textvariable=user)
        self.usuario.grid(row= 0, column=0)

        self.datoOp = Label(self.createPassL, text='Contraseña: ')
        self.datoOp.grid(row= 0, column=0)

        self.password = Entry(self.createPassE, textvariable=password, show='*')
        self.password.grid(row= 0, column=0)

        self.datoOp = Label(self.createNameL, text='Nombre: ')
        self.datoOp.grid(row= 0, column=0)

        self.name = Entry(self.createNameE, textvariable=name)
        self.name.grid(row= 0, column=0)

        self.datoOp = Label(self.createSurnameL, text='Apellido: ')
        self.datoOp.grid(row= 0, column=0)

        self.apellido = Entry(self.createSurnameE, textvariable=surname)
        self.apellido.grid(row= 0, column=0)

        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        #=======================================Botones================================================================
        self.btnCrear = Button(self.botones, text='Crear', background= 'pale green', command = "")
        self.btnCrear.grid(row=0, column= 1)

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

        #=====================================Etiquetas==========================================================






main()
