from PySide2 import QtCore
from PySide2 import QtCore, QtGui, QtWidgets
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
import json
import radni_prostor

class RenameDialog(QtWidgets.QDialog):
    created = QtCore.Signal()

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Rename Document")
        self._layout = QtWidgets.QGridLayout()
        self.setLayout(self._layout)

        self.tekst = QtWidgets.QLabel("Novo ime za selektovani dokument:")
        
        self.button_rename = QtWidgets.QPushButton("Preimenuj Dokument")

        
        self.populate_dialog()

    def populate_dialog(self):
        self._layout.addWidget(self.tekst) 
        self.rename_input = QtWidgets.QLineEdit()
        self._layout.addWidget(self.rename_input)
        # self.rename_uneto = self.rename_input.text()
        self._layout.addWidget(self.button_rename)     
        # self.button_rename.clicked.connect(self.dugme_kliknuto)
