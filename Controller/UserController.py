from DataModel.UserData import  UserData


class UserController:

    def createUser(self, name, surname, user, password, wallet):
        dbuser = UserData()
        dbuser.createUser(name, surname, user, password, wallet)
        print("se creo un usuario")

    def validateUser(self, user, password):
        dbUser = UserData()
        logUser = dbUser.getUser(user, password)
        print(logUser.name)
        return logUser

