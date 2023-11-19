class User:
    def __init__(self, name: str, surname: str, address: str, email: str, password: str):
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email
        self.password = password

    def show_users(self) -> str:
        return f'{self.name} {self.surname}'

users: list[User] = []
