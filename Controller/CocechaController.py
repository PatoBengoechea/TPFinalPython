from DataModel.CosechaDataBase import  CosechaData
from Model.Cosecha import Cosecha


class CosechaController:

    def createCocecha(self, id, cereal, cantidad, inicio, fin, productor ):
        dbCosecha = CosechaData()
        nuevaCosecha = Cosecha(id, cereal, cantidad, inicio, fin, productor)
        response = dbCosecha.addCosecha(nuevaCosecha)
        if(response):
            return nuevaCosecha
        else:
            return False


    def getCocecha(self):

