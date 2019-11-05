from DataModel.Database import Database
from Model.Cosecha import Cosecha
from Model.User import User
from bson import ObjectId

class CosechaData:
    def getCosechas(self):
        db = Database()
        cursor = db.main()
        cosechas = []
        try:
            data = cursor.cosecha.find()
            for i in data:
                nc = Cosecha()
                nc.cereal = i["cereal"]
                nc.cantidadProduccion = i["cantidadProduccion"]
                nc.inicio = i["inicio"]
                nc.fin = i["fin"]
                user = i["productor"]
                productorJSON = cursor.usuario.find_one({"user": user})
                productor = User()
                productor.parse(productorJSON)
                nc.productor = productor
                cosechas.append(nc)
            return cosechas
        except:
            return None


    def addCosecha(self, cosecha):
        db = Database()
        cursor = db.main()
        newCosecha = {
            'cereal' : cosecha.cereal,
            'cantidadProduccion' : cosecha.cantidadProduccion,
            'inicio' : cosecha.inicio,
            'fin' : cosecha.fin,
            'productor' : cosecha.productor.user
        }
        try:
            cursor.cosecha.insert_one(newCosecha)
            print("OK")
            return True
        except:
            print("wrong")
            return False




