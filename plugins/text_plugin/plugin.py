from PySide2 import QtWidgets
from integrativna_komponenta.main_window import MainWindow
from integrativna_komponenta.ui.label import Label
from plugin_framework.extension import Extension



class Plugin(Extension):

    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        
        """ 
        super().__init__(specification, iface)
        self.layout = MainWindow.layout
        self.layout1 = Label.layout
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget1 = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        self.tabWidget.setFixedWidth(500)
        self.tabWidget.setFixedHeight(250)

        self.tabWidget1.setTabsClosable(True)
        self.tabWidget1.tabCloseRequested.connect(self.delete_tab1)
        self.tabWidget1.setFixedWidth(500)
        self.layout1.addWidget(self.tabWidget)
        self.layout1.addWidget(self.tabWidget1)
        self.tabWidget1.setFixedHeight(250)

        self.widget = QtWidgets.QWidget()

        self.widget.setLayout(self.layout1)
        



    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.layout.addWidget(self.widget) 
        self.activated = True
        print("Activated")

    def deactivate(self):
        self.layout.itemAt(0).widget().setParent(None)
        self.activated = False

        print("Deactivated")

    def delete_tab(self,index):
        self.tabWidget.removeTab(index)
    
    def delete_tab1(self,index):
        self.tabWidget.removeTab(index)