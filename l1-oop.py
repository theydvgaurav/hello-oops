# Basic OOP in Python

class User:
    def __init__(self):
        self.__username = None
        self.__email = None
        self.__is_logged_in = False
        self.__status_map = {
            True: "Logged in",
            False: "Logged out"
        }

    def get_login_status(self):  # getter
        return self.__is_logged_in

    def set_login_status(self, status: bool):  # setter
        self.__is_logged_in = status

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def login(self):
        self.set_login_status(True)

    def logout(self):
        self.set_login_status(False)

    def __str__(self):
        return f"User(username='{self.get_username()}', email='{self.get_email()}')"

    def get_status(self):
        return self.__status_map.get(self.get_login_status())


g = User()
g.set_username("Gaurav")
g.set_email("gaurav@gmail.com")
print(g.get_status())  # should print "Logged out"
g.login()
print(g.get_status())  # should print "Logged in"
g.logout()
print(g.get_status())  # should print "Logged out"
