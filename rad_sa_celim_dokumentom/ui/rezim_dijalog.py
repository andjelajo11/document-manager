from PySide2 import QtCore 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialogButtonBox
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
import json

class RezimDialog(QtWidgets.QDialog):
    created = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Share Document")
        self.setWindowIcon(QtGui.QIcon("resources/icons/document share.png"))
        self._layout = QtWidgets.QGridLayout()
        self.setLayout(self._layout)

        self.tekst = QtWidgets.QLabel("Sada ste u režimu deljenja. Prevlačenjem mozete deliti dokumenta izmedju kolekcija u ovom radnom prostoru.")
        
        self.button_cancle = QtWidgets.QPushButton("Ok")
        self.button_cancle.setFixedSize(QtCore.QSize(100, 25))
        self.button_cancle.clicked.connect(self.reject)
        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.populate_dialog()

    def populate_dialog(self):
        self._layout.addWidget(self.tekst) 
        self._layout.addItem(self.spacer)
        self._layout.addWidget(self.button_cancle, 1, 0, 1, 2,  QtCore.Qt.AlignCenter )     
