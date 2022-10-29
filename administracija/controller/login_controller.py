from csv import DictReader

from pip import main
from ui.main_window import MainWindow


class LoginController:
    def __init__(self):
        pass

    def login(self, model):
        # preuzmemo podatke sa forme za prijavu
        # ucitamo datoteku da proverimo da li postoji takav kao iz forme
        # FIXME: ovaj deo obrade datoteke (provere korisnika) izvuce u
        # drugi python file koji je file handler
        # FIXME: kasnije ce se podaci ucitavati iz baze podataka a ne datoteke
        with open("data/users.csv", "r", encoding="utf-8") as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                if row["user_id"] == model.user_id and row["user_password"] == model.user_password:
        # u zavisnosti od rezultata proslediti rezultat dijalogu
                    return True
        return False
        
        # TODO: ako je prijava uspesna pozvati sopstvenu metodu start_app

    def password_change(self, new_password):
        ...

    def quit(self):
        ...

    def start_app(self, model=None):
        main_window = MainWindow()
        main_window.show()