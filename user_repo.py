from user import User

class UserRepo:
    def __init__(self, connection):
         self.connection = connection

    def create(self, user):
        self.connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [user.username, user.password])
        return None

    def all(self):
        rows = self.connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            item = User(row["username"], row["password"], row["id"])