from PySide2 import QtWidgets


class CentralWidget(QtWidgets.QTabWidget):

    def __init__(self, parent=None): #da li treba atribut parent=None???
        super().__init__(parent)

        self.tab0=QtWidgets.QTextEdit()

        self.tab1 = QtWidgets.QTextEdit()

        self.addTab(self.tab0, "Pocetni prozor")
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.delete_tab)

    def add_widget(self):
        self.addTab(self.tab1, "text editor" )
        self.tab1.insertPlainText("Text editor je aktiviran!")
        
    def delete_tab(self,index):
        self.removeTab(index)

