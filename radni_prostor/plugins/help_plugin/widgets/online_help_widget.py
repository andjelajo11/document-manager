from PySide2 import QtWidgets
from PySide2 import QtGui
#from 

class OnlineHelpWidget(QtWidgets.QMessageBox):
    # FIXME: postaviti relativnu putanju
    config_path = "configuration.json"
    def __init__(self, parent=None):
        super().__init__(parent)

        self._icon = QtWidgets.QMessageBox.Information

        #self.my_icon = QtGui.QPixmap("resources/icons/puzzle.png")
        

        self._populate_dialog()


    def _populate_dialog(self):
        self.setWindowTitle("Online uputstvo")
        self.setText("Online uputstvo za koriscenje programa ce biti dostupno u narednom perioud")
        self.setIcon(self._icon)
        #self.setIconPixmap(self.my_icon)
