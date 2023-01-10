from PySide2 import QtWidgets, QtCore
from radni_prostor import treeView

class DockWidget(QtWidgets.QDockWidget):

    clicked = QtCore.Signal(str, str)
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        
        # self.button_update = QtWidgets.QPushButton("Refresh workspace")
        # self.button_update.clicked.connect(self.kliknuto_update)
        
        

    # def kliknuto_update (self):
            
            


    
    # def refresh_workspace(self):
        
    #     self.button_update = QtWidgets.QPushButton("Refresh workspace")
     
