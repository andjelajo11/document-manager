from PySide2 import QtWidgets

class MonotipTab(QtWidgets.QTabWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        # self.tabWidget.setTabsClosable(True)
        # self.tabWidget.tabCloseRequested.connect(self.delete_tab)

    

    def textEditor(self, textEditor):
        self.addTab(textEditor, "Text Editor")
    
    # def delete_tab(self,index):
    #     self.removeTab(index)
