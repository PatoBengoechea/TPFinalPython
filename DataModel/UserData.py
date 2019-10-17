from TPFinalPython.DataModel.Database import Database
from TPFinalPython.Model.User import User

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
        cursor.usuario.insert_one(newUser)


    def getUser(self, user, password):

        #Hacer try catch, que pasa si no encuentra un usuario?
        db = Database()
        cursor = db.main()
        logUserJSON = cursor.usuario.find_one({"user": user})
        logUserModel = User()
        logUserModel.user = logUserJSON["user"]

        print(logUserModel.user)

a = UserData()
a.getUser('pb', 112)
