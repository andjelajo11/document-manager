from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PySide2.QtCore import QSize, Qt
from plugins.otvoreni_dokument.treeWidget import TreeView
from plugins.otvoreni_dokument.thumbnail_widget import ThumbnailWidget

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
      
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        

        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        


        
        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.tabWidget)



        

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
        parent_size = self.iface.size()
        new_size = QSize(parent_size.width() / 2, parent_size.height() / 2)
        self.mainWidget.resize(new_size)
                
        self.iface.layout.setAlignment(self.mainWidget, Qt.AlignLeft)

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
            self.innerTabWidget = QtWidgets.QTabWidget()
            self.innerTabWidget.setTabsClosable(False)
            self.treeWidget = TreeView()
            
            with open('radni_prostor/dokumenti.json') as data_file:  
                data = json.load(data_file) 
            data_file.close()          

            self.page = self.innerTabWidget.currentWidget()
            self.layoutG = QGridLayout()
            self.layoutH1 = QHBoxLayout()

            self.page = QtWidgets.QWidget()
            self.newWidget = self.tabWidget.currentWidget()
            self.mainLayout.addWidget(self.tabWidget)
            self.newWidget = QtWidgets.QWidget()
            

            self.newWidget.setLayout(self.layoutH1)
            self.layoutH1.addWidget(self.innerTabWidget)
            
            self.page.setLayout(self.layoutG)
            self.layoutG.addWidget(self.treeWidget)


            for ix in self.treeView.selectedIndexes():
                text = ix.data()
                if "dokument" in text:
                    for i in data:
                        if text == i:
                            self.thumbnail = ThumbnailWidget(text)
                            
                            self.tabWidget.addTab(self.newWidget,"" + text)
                            self.tabWidget.setCurrentWidget(self.newWidget)
                            self.innerTabWidget.addTab(self.thumbnail, "Thumbnail")
                            self.innerTabWidget.addTab(self.page, "Bookmark")
                            self.innerTabWidget.setCurrentWidget(self.page)
                            self.layoutG.addWidget(self.treeWidget,0,0)
                            self.treeWidget.populate(text)
                       

        
                        
                            
                         


    

    



   
