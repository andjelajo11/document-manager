from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PySide2.QtCore import QSize, Qt
from plugins.otvoreni_dokument.treeWidget import TreeView
from plugins.otvoreni_dokument.thumbnail_widget import ThumbnailWidget

import json

from PySide2 import QtWidgets

class Plugin(Extension):
    id = 0
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
        
        self.recnik = {}
        

        
        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.tabWidget)



        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.activated = True
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["otvoreni_dokument"] = True
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)        


    def checkForWorkspace(self):
        
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
                treeView = dock.widget().layout().itemAt(0).widget()
                self.recnik[self.id] = treeView
                self.id += 1
        for index, treeView in self.recnik.items():
            treeView.clicked.connect(lambda: self.onClicked(index))
        

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
        #zatvaranje taba brise naziv dokumenta iz json fajla -> dokument je zatvoren
        with open('rad_sa_celim_dokumentom/otvoreniDokumenti.json') as data_file: 
            data = json.load(data_file)
        tab_text = self.tabWidget.tabText(index)
        if tab_text in data:
            print("1")
            data.remove(tab_text)
            print("2")
            print(data)
            print("3")
            with open('rad_sa_celim_dokumentom/otvoreniDokumenti.json', 'w') as data_ffile: 
                    print("4")
                    data_json = json.dumps(data, sort_keys=True, indent=4)
                    print("5")
                    data_ffile.write(str(data_json))
                    print("6")
        self.tabWidget.removeTab(index)

        
        
    def onClicked(self, index):
        self.treeView = self.recnik[index]
        self.iface.layout.addWidget(self.mainWidget)
        self.mainWidget.setLayout(self.mainLayout)
        parent_size = self.iface.size()
        new_size = QSize(parent_size.width() / 2, parent_size.height() / 2)
        self.mainWidget.resize(new_size)
        self.iface.layout.setAlignment(self.mainWidget, Qt.AlignLeft)
        #upisivanje dokumenta u json file kada je kliknut da se otvori -> dokument je otvoren
        # for y in self.treeView.selectedIndexes():
        #         text = y.data()
        # with open('rad_sa_celim_dokumentom/otvoreniDokumenti.json') as data_ffile: 
        #     data_list = json.load(data_ffile)
        # #provera da li je dokument vec upisan u json 
        # if text in data_list:
        #     print("dokument je vec upisan")
        # else:
        #     data_list.append(text) 
        #     # for i in data_list:
        #     #     for j in data_list[i]:
        #     #         data_list[i].append(text) 
        #     #         print(data_list)
        #     #         break
        #     with open('rad_sa_celim_dokumentom/otvoreniDokumenti.json', 'w') as doc_file: 
        #         data_json = json.dumps(data_list, sort_keys=True, indent=4)
        #         doc_file.write(str(data_json))
            
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
                print(text)
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

                       

        
                        
                            
                         


    

    



   
