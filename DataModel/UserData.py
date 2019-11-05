from DataModel.Database import Database
from Model.User import User

class UserData:

    def createUser(self, name, surname, user, password, wallet):
        db = Database()
        cursor = db.main()
        newUser = {
            'name': name,
            'surname': surname,
            'user': user,
            'password': password,
            'wallet': wallet
        }
        print(newUser)
        cursor.usuario.insert_one(newUser)


    def getUser(self, user, password):

        #Hacer try catch, que pasa si no encuentra un usuario?
        db = Database()
        cursor = db.main()
        logUserJSON = cursor.usuario.find_one({"user": user, "password": password})
        if logUserJSON != None:
            logUserModel = User()
            logUserModel.user = logUserJSON["user"]
            logUserModel.password = logUserJSON["password"]
            logUserModel.surname = logUserJSON["surname"]
            logUserModel.wallet = logUserJSON["wallet"]
            logUserModel.name = logUserJSON["name"]
            return logUserModel
        else:
            return None
