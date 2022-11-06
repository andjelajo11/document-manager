from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit
from administracija.model.login_model import LoginModel


class LoginDialog(QDialog):
    def __init__(self, parent=None, model=None, controller=None):
        super().__init__(parent)
        self.setWindowTitle("Prijava na sistem")
        self.setWindowIcon(QIcon("resources/icons/lock.png"))
        self.resize(300, 100)
        # Model treba da bude tipa LoginModel
        if model is None:
            model = LoginModel()
        self.login_model = model
        self.login_controller = controller

        # Username: [               ]
        # Password: [               ]
        self.form_layout = QFormLayout(self)
        self.username_label = QLabel("Username:")
        self.password_label = QLabel("Password:")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # popunjavanje forme spram modela
        if model.user_id is not None:
            self.username_input.setText(model.user_id)
        if model.user_password is not None:
            self.password_input.setText(model.user_password)

        self.password_input.setEchoMode(QLineEdit.Password)
        # popunjavanje layout-a
        self.form_layout.addRow(self.username_label, self.username_input)
        self.form_layout.addRow(self.password_label, self.password_input)
        #  dodati dugmice
        self.form_layout.addRow(self.button_box)
        # uvezati akcije na dugmice
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject) # zatvara dijalog

        # postavljamo layout dijaloga
        self.setLayout(self.form_layout)


    # Redefinisati accept metodu
    def accept(self):
        # pokupimo podatke iz forme
        self.login_model.user_id = self.username_input.text()
        self.login_model.user_password = self.password_input.text()
        # prosledimo ih login kontroleru (poziv metode login)
        result = self.login_controller.login(self.login_model)
        # dobijeni rezultat iz login metode dalje iskroristiti za nastavak aplikacije
        # (u slučaju uspeha, pokretnuti aplikaciju (glavni prozor))
        if result:
            print("Prijava korisnika")
            return super().accept()
        # (u slučaju neuspeha, obrisati password polje)
        else:
            print("Prijava neuspesna")
            self.password_input.clear()
        
        

        
        

    