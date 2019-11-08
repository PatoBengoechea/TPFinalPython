from tkinter import ttk
from tkinter import *

from Controller.prueba import armarListadoDeTrades #borrar
from Controller.CosechaControler import CosechaController

from Controller.controladorPrecios import controladorPrecios

from Views.vistaOp import Ventana5

class Ventana3:

    def __init__(self, master, user, name, surname):

        self.master = master
        self.master.title('Panel Principal')
        self.master.geometry('1200x500+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.user = user
        self.name = name
        self.surname = surname

        self.cosechasControlador = CosechaController()

        self.cosechas = self.cosechasControlador.getCocecha(self.user)

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

        self.frameEtiquetaLista = Frame(self.frame, width= 300, height= 50)
        self.frameEtiquetaLista.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.tvw = Frame(self.frame, width= 300, height= 50)
        self.tvw.grid(row=ubF, column=0)

        self.tvw2 = Frame(self.frame, width= 300, height= 50) #test
        self.tvw2.grid(row=ubF, column=1)

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

        self.titleLista = Label(self.frameEtiquetaLista, text="Listado de Cosechas", background= 'deep sky blue')
        self.titleLista.grid(row= 0, column=0)


        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.tvw)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two","three","four","five")
        #reveer
        vsb = ttk.Scrollbar(self.tvw2, orient="vertical", command=self.tv.yview)
        #vsb.place(x=30+455+2, y=20, height=200)
        vsb.grid(row= 0, column= 0)

        #====================================TVColums==============================================================
        anchoCol = 150

        self.tv.column("one", width=anchoCol)
        self.tv.column("two", width=anchoCol)
        self.tv.column("three", width=anchoCol)
        self.tv.column("four", width=anchoCol)
        self.tv.column("five", width=anchoCol)


        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="Cereal")
        self.tv.heading("two", text="Cantidad")
        self.tv.heading("three", text="Inicio")
        self.tv.heading("four", text="Fin")
        self.tv.heading("four", text="Cotizacion")


        #===============================Prueba de insertar datos================================================

        self.listar()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        #===========================================Botones============================================================

        ubBot = 1

        self.btnOperaciones = Button(self.botones, text='Agregar Cosecha', background= 'aquamarine', command = "")
        self.btnOperaciones.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn = Label(self.botones)
        self.spaceBtn.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnCocechas = Button(self.botones, text='Ver Cotizaciones', background= 'medium aquamarine', command = lambda: self.verCotizaciones())
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

        print(self.cosechas)

        if(self.cosechas != None):
            for cosecha in self.cosechas:
                precio = self.buscarMejorPrecio(cosecha.cereal)
                self.tv.insert("" , 0, values=(cosecha.cereal, cosecha.cantidadProduccion, cosecha.inicio, cosecha.fin, precio))

        self.tv.pack()

    def new_window(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana5(self.newWindow)

    def verCotizaciones(self):
        self.new_window()

    def buscarMejorPrecio(self, cosecha):
        a = controladorPrecios(cosecha)









