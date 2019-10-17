from TPFinalPython.DataModel.UserData import UserData


class UserController:

    def createUser(self, name, surname, user, password, wallet):
        dbUser = UserData()
        dbUser.createUser(name, surname, user, password, wallet)
        print("se creo un usuario")



