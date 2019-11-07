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


    def getCocecha(self, productorActual):
        dbCosecha = CosechaData()
        cosechas = dbCosecha.getCosechas(productorActual)
        if(cosechas != None):
            return cosechas
        else:
            return None

#borrar all
a = CosechaController()
b = a.getCocecha('juunchy')
print(b[0].cereal)
