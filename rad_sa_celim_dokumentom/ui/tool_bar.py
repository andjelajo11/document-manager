from PySide2.QtWidgets import QToolBar
from PySide2 import QtGui, QtWidgets


class ToolBar (QToolBar):
    def __init__(self):
        super().__init__()
        
        
    # def akcije(self):     
        # self.dodaj = QtWidgets.QAction(QtGui.QIcon("resources/icons/prohibition-button.png"),"Dodavanje u tabelu", self)
        # self.addAction(self.dodaj)

    def add_crud(self):
        self.create_action = self.addAction(QtGui.QIcon("resources/icons/create-new-document.png"), "Create Document")
        # self.update_action = self.addAction(QtGui.QIcon("resources/icons/Save-icon.png"), "Update")
        self.delete_action = self.addAction(QtGui.QIcon("resources/icons/trash-bin-document.png"), "Delete Document")
        self.save_action = self.addAction(QtGui.QIcon("resources/icons/save.png"), "Save")
            
    def create_document (self):
        pass
        