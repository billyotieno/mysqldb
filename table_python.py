class Table_python:
    user_count: int = 0
    __username = "John Doe"
    __password = "1234"
    __userrole = "normal_user"

    def __init__(self, name, passwd, role):
        """
        :rtype: object
        """
        self.__username = name
        self.__password = passwd
        self.__userrole = role

    def getUsername(self):
        return self.__username

    def setUsername(self, name):
        self.__username = name

    def getPassword(self):
        return self.__password

    def setPassword(self, passwd):
        self.__password = passwd

    def setUserrole(self, urole):
        self.__userrole = urole

    def getUserrole(self):
        return self.__userrole

    def __str__(self):
        message = "This is Table_python Class"
        return message

