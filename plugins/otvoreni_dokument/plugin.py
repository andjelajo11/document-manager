from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from plugins.otvoreni_dokument.treeWidget import TreeView

import json



from PySide2 import QtWidgets

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.mainLayout = QVBoxLayout() #gore i dole na main widgetu
         #levo i desno
        self.layoutH1 = QHBoxLayout()
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        self.mainWidget = QtWidgets.QWidget()


        
        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.tabWidget)

        self.dockWidget = QtWidgets.QDockWidget



        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        self.activated = True

        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)
        
        plugins["otvoreni_dokument"] = True

        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)
        
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
            self.dockWidget = dock

        self.treeView = self.dockWidget.widget()
        self.treeView.clicked.connect(self.onClicked)    
        self.iface.layout.addWidget(self.mainWidget)
        self.mainWidget.setLayout(self.mainLayout)
        

    def deactivate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)
        
        plugins["otvoreni_dokument"] = False

        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)
        print("Deactivated")
        self.activated = False  
        self.iface.layout.itemAt(0).widget().setParent(None)
        


    def delete_tab(self,index):
        self.tabWidget.removeTab(index)

        
    def onClicked(self):
        existing_page = None
        for i in range(self.tabWidget.count()):
            if self.tabWidget.tabText(i) == self.treeView.selectedIndexes()[0].data():
                existing_page = self.tabWidget.widget(i)
                break



        if existing_page == None:
            self.treeWidget = TreeView()
            
            
            with open('radni_prostor/dokumenti.json') as data_file:  
                data = json.load(data_file) 
            data_file.close()          

            self.page = self.tabWidget.currentWidget()
            self.layoutG = QGridLayout()
            
            self.page = QtWidgets.QWidget()      
            self.page.setLayout(self.layoutG)
            self.mainLayout.addWidget(self.tabWidget)

            for ix in self.treeView.selectedIndexes():
                text = ix.data()
                if "dokument" in text:
                    for i in data:
                        if text == i:
                            
                            self.tabWidget.addTab(self.page,"" + text)
                            self.tabWidget.setCurrentWidget(self.page)
                            self.layoutG.addWidget(self.treeWidget,0,0)
                            self.treeWidget.populate(text)

                       

        
                        
                            
                         


    

    



   
