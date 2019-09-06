from Database import Database

class UserData:

    def createUser(self, name, surname, user, password, wallet):
        db = Database()
        cursor = db.main()
        newUser = {
            'user': name,
            'surname': surname,
            'user': user,
            'password': password,
            'wallet': wallet
        }
        cursor.usuario.insert(newUser)


ud = UserData()
ud.createUser("pato", "ben", "pb", "1995", 1000)
