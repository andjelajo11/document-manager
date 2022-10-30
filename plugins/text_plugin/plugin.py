from PySide2 import QtWidgets
from integrativna_komponenta.main_window import MainWindow
from plugin_framework.extension import Extension



class Plugin(Extension):

    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        
        """ 
        super().__init__(specification, iface)
        self.layout = MainWindow.layout
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        self.tabWidget.setFixedWidth(500)



    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.layout.addWidget(self.tabWidget) 
        self.activated = True
        print("Activated")

    def deactivate(self):
        self.layout.itemAt(0).widget().setParent(None)
        self.activated = False

        print("Deactivated")

    def delete_tab(self,index):
        self.tabWidget.removeTab(index)
