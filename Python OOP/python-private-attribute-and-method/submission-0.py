class PasswordManager:
    def __init__(self, password: str):
        self.__password = password

    def verify_password(self, input_password: str) -> bool:
        return self.__password == input_password


# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))  # Should print: False
