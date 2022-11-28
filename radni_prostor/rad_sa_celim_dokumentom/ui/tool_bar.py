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
        

    # def add_filter(self):
    #     self.filter_action = self.addAction(QtGui.QIcon("icons/filter.png"), "Filter")
    #     self.edit_filter_action = self.addAction(QtGui.QIcon("icons/settings.png"), "Edit filter")
 
    # def add_split_merge(self):
    #     self.addSeparator()
    #     self.split_action = self.addAction(QtGui.QIcon("icons/split.png"), "Split")
    #     self.merge_action = self.addAction(QtGui.QIcon("icons/merge.png"), "Merge")

    # def add_navigation(self):
    #     self.addSeparator()
    #     self.parent_action = self.addAction(QtGui.QIcon("icons/up.png"), "Parent")
    #     self.child_action = self.addAction(QtGui.QIcon("icons/down.png"), "Child")

    # def set_filter_icon(self, filtered):
    #     icon_name = "filter_enabled.png" if filtered else "filter.png"
    #     self.filter_action.setIcon(QtGui.QIcon(f"icons/{icon_name}"))
    
    def create_document (self):
        pass
        