from PySide2 import QtCore 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialogButtonBox
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
import json

class AlertDialog(QtWidgets.QDialog):
    created = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Alert")
        self.setWindowIcon(QtGui.QIcon("resources/icons/trash-bin-document.png"))
        self._layout = QtWidgets.QGridLayout()
        self.setLayout(self._layout)

        self.tekst = QtWidgets.QLabel("Da li ste sigurni da želite da izbrišete ovaj dokument?")
        
        self.button_cancle = QtWidgets.QPushButton("Otkaži")
        self.button_cancle.setFixedSize(QtCore.QSize(100, 25))
        self.button_potvrdi = QtWidgets.QPushButton("DA")
        self.button_potvrdi.setFixedSize(QtCore.QSize(100, 25))

        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.populate_dialog()

    def populate_dialog(self):
        # self._layout.addItem(self.spacer)
        self._layout.addWidget(self.tekst) 
        self._layout.addItem(self.spacer)
        # self.rename_uneto = self.rename_input.text()
        self._layout.addWidget(self.button_cancle, 1, 0, 1, 2,  QtCore.Qt.AlignCenter )     
        self._layout.addWidget(self.button_potvrdi, 2, 0, 1, 2,  QtCore.Qt.AlignCenter)     
