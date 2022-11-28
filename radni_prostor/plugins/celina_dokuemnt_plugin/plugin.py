from PySide2 import QtWidgets
from plugin_framework.extension import Extension
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokCelina
from radni_prostor.dock_widget import DockWidget
from radni_prostor.treeView import TreeView
from PySide2 import QtCore
from rad_sa_celim_dokumentom.ui.tool_bar import ToolBar

class Plugin(Extension, ExtensionDokCelina):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """
        # 
        super().__init__(specification, iface)
        self.layout = iface.layout
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        #self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        self.tabWidget.setFixedWidth(500)

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.toolbar = ToolBar()        
        self.iface.addToolBar(self.toolbar)
        self.toolbar.add_crud()
        self.layout.addWidget(self.tabWidget) 
        self.activated = True
        self.tool_bar.create_action.triggered.connect(self.toolbar.create_document) #gde implementirati ovde metode u kojoj klasi
        self.tool_bar.update_action.triggered.connect(self.update_worspace) #gde implementirati ovde metode u kojoj klasi
        self.tool_bar.delete_action.triggered.connect(self.delete_document) #gde implementirati ovde metode u kojoj klasi


        # self.iface.setWidget(self.toolbar)
        self.activated = True
        print("Activated")
        

    def deactivate(self):
        self.iface.removeToolBar(self.toolbar)
        # self.dock_widget.setParent(None)
        # self.dock_widget.setWidget(None)
        # self.activated = False
        print("Deactivated")
    
    def delete_document (self):
        pass
        # getDocument() 
        # dialogWidget.show()
        # removeDocumentFromJson()
        # updateWorkspace()
        
        