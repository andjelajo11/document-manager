from PySide2 import QtWidgets
from PySide2 import QtGui
#from 

class OflineHelpWidget(QtWidgets.QMessageBox):
    # FIXME: postaviti relativnu putanju
    config_path = "configuration.json"
    def __init__(self, parent=None):
        super().__init__(parent)

        self._icon = QtWidgets.QMessageBox.Information

        #self.my_icon = QtGui.QPixmap("resources/icons/puzzle.png")
        

        self._populate_dialog()


    def _populate_dialog(self):
        self.setWindowTitle("Dokumentovano uputstvo")
        self.setText("Dokumentovano uputstvo za koriscenje programa ce biti dostupno u narednom periodu")
        self.setIcon(self._icon)
        #self.setIconPixmap(self.my_icon)
