from PySide2 import QtWidgets

class MonotipTab(QtWidgets.QTabWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.label = QtWidgets.QLabel()
        self.label.setText("ovo je test")
        self.addTab(self.label, "test")

    

    def textEditor(self, textEditor):
        self.addTab(textEditor, "Text Editor")
