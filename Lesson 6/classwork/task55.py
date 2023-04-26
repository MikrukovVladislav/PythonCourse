# # Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"

from abc import ABC

class LoginNotFound(ValueError):
    pass
class IncorrectPassword(ValueError):
    pass
class LengthError(ValueError):
    pass
class Abstract(ABC):
    def login(self):
        pass
    def check_password(self, pwd):
        pass
    def check_login(self, log):
        pass

class LoginClass(Abstract):
    correct_login="test"
    correct_password="123"
    def check_password(self, pwd):
        if(len(pwd) > 8):
            raise LengthError
        else:
            if(pwd != self.correct_password):
                raise IncorrectPassword

    def check_login(self, log):
        if(log != self.correct_login):
            raise LoginNotFound

    def login(self):
        self.check_login(str(input("Введите логин: ")))
        self.check_password(str(input("Введите пароль: ")))
        print("Login success")

a=LoginClass()

a.login()