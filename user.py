class User:
    def __init__(self, username, password, id = None):
        self.username = username
        self.password = password
        self.id = id

    def __eq__(self, vlaue):
        return self.__dict__ == value.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.user}, {self.password})"
