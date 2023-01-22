from PySide2 import QtWidgets

class MonotipTab(QtWidgets.QTabWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.delete_tab)

    

    def textEditor(self, textEditor):
        self.addTab(textEditor, "Text Editor")
    
    def vectorImage(self, image):
        self.addTab(image, "Vector")
    
    def rasterImage(self, image):
        self.addTab(image, "Raster")

    def delete_tab(self,index):
        self.removeTab(index)
