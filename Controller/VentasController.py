from DataModel.VentaDataBase import VentaDataBase
from DataModel.CosechaDataBase import CosechaData
from Model.Venta import Venta

class VentasController:

    def addVenta(self, cosecha, precioUnitario, cantidad):
        DB = VentaDataBase()
        if cosecha.cantidadParcial > cantidad:
            try:
                DB.addVenta(cosecha, precioUnitario, cantidad)
                return True
            except NameError:
                print(NameError)
                return False

    def getVentas(self, cosecha):
        db = VentaDataBase()
        return db.getVentas(cosecha)
