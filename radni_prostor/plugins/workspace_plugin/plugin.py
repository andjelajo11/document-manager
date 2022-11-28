from plugin_framework.extension import Extension
from radni_prostor.dock_widget import DockWidget
from radni_prostor.treeView import TreeView
from PySide2 import QtCore

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """
        # 
        super().__init__(specification, iface)
        
        

        


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.treeView = TreeView()
        self.dock_widget = DockWidget("Workspace", self.iface)
        self.iface.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_widget)
        self.dock_widget.setLayout(self.iface.layout)
        self.dock_widget.setWidget(self.treeView)
        self.activated = True
        print("Activated")
        

    def deactivate(self):
        self.iface.removeDockWidget(self.dock_widget)
        # self.dock_widget.setParent(None)
        # self.dock_widget.setWidget(None)
        # self.activated = False
        print("Deactivated")
        