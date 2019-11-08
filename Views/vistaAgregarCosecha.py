from tkinter import ttk
from tkinter import *

class Ventana6:

    def __init__(self,master):
        self.master = master
        self.master.title('Panel Principal')
        self.master.geometry('1400x500+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.user = StringVar()
        self.password = StringVar()
        self.name = StringVar()
        self.surname = StringVar()

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

        self.respuesta = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.respuesta.grid(row=8, column=1)


        #======================================Labels and Entries=================================================================
        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        self.datoOp = Label(self.createUsuarioL, text='Usuario: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.createUsuarioE, textvariable=self.user)
        self.usuario.grid(row= 0, column=0)

        self.datoOp = Label(self.createPassL, text='Contraseña: ')
        self.datoOp.grid(row= 0, column=0)

        self.password = Entry(self.createPassE, textvariable=self.password, show='*')
        self.password.grid(row= 0, column=0)

        self.datoOp = Label(self.createNameL, text='Nombre: ')
        self.datoOp.grid(row= 0, column=0)

        self.name = Entry(self.createNameE, textvariable=self.name)
        self.name.grid(row= 0, column=0)

        self.datoOp = Label(self.createSurnameL, text='Apellido: ')
        self.datoOp.grid(row= 0, column=0)

        self.apellido = Entry(self.createSurnameE, textvariable=self.surname)
        self.apellido.grid(row= 0, column=0)

        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        #=======================================Botones================================================================
        self.btnCrear = Button(self.botones, text='Agregar', background= 'pale green', command = lambda: self.agregarCosecha())
        self.btnCrear.grid(row=0, column= 1)

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

        #=====================================Etiquetas==========================================================

    def agregarCosecha(self):
        pass
