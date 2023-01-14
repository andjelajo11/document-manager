from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PySide2.QtCore import QSize, Qt
from plugins.otvoreni_dokument.treeWidget import TreeView
from plugins.otvoreni_dokument.thumbnail_widget import ThumbnailWidget
from plugins.stranica_plugin.plugin import Plugin as Stranica_plugin
from PySide2.QtGui import QIcon

import json

from PySide2 import QtWidgets

class Plugin(Extension):
    id = 0
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.mainLayout = QVBoxLayout()
        
      
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        

        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.recnik = {}
        
        self.stranica_plugin = Stranica_plugin(specification, iface)

        
        self.mainLayout.addWidget(self.tabWidget)



        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["otvoreni_dokument"] = True
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)   
        self.activated = True


        

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
        tab_text_list = self.tabWidget.tabText(index).split('/')
        tab_text = tab_text_list[1]
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

        
        
    def onClicked(self, dokument, workspace):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        if plugins["otvoreni_dokument"] == True:
            self.toolBar = QtWidgets.QToolBar()

            self.up = QtWidgets.QAction(QIcon("resources/icons/up.png"),"Up",self.mainLayout)
            self.down = QtWidgets.QAction(QIcon("resources/icons/down.png"),"Down",self.mainLayout)
            self.top = QtWidgets.QAction(QIcon("resources/icons/top.png"),"First",self.mainLayout)
            self.bottom = QtWidgets.QAction(QIcon("resources/icons/bottom.png"),"Last",self.mainLayout)
            self.delete = QtWidgets.QAction(QIcon("resources/icons/kanta.png"),"Delete",self.mainLayout)
            self.new = QtWidgets.QAction(QIcon("resources/icons/new-page.png"),"New Page",self.mainLayout)

            self.toolBar.addAction(self.up)
            self.toolBar.addAction(self.down)
            self.toolBar.addAction(self.top)
            self.toolBar.addAction(self.bottom)
            self.toolBar.addAction(self.delete)
            self.toolBar.addAction(self.new)

            
            self.mainWidget.setLayout(self.mainLayout)
            parent_size = self.iface.size()
            new_size = QSize(parent_size.width() / 2, parent_size.height() / 2)
            self.mainWidget.resize(new_size)

            # # upisivanje dokumenta u json file kada je kliknut da se otvori -> dokument je otvoren
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
                

            self.innerTabWidget = QtWidgets.QTabWidget()
            self.innerTabWidget.setTabsClosable(False)
            self.treeWidget = TreeView() 

            self.page = self.innerTabWidget.currentWidget()
            self.layoutG = QGridLayout()
            self.layoutH1 = QGridLayout()

            self.page = QtWidgets.QWidget()
            self.newWidget = self.tabWidget.currentWidget()
            
            self.mainLayout.addWidget(self.tabWidget)
            self.newWidget = QtWidgets.QWidget()
            

            self.newWidget.setLayout(self.layoutH1)
            self.layoutH1.addWidget(self.toolBar, 0, 0)
            self.layoutH1.addWidget(self.innerTabWidget, 1, 0)
            
            self.page.setLayout(self.layoutG)
            self.layoutG.addWidget(self.treeWidget)




        
        

            if "dokument" in dokument:        
                self.thumbnail = ThumbnailWidget(dokument, workspace, self.stranica_plugin)
                self.down.triggered.connect(self.thumbnail.down)
                self.up.triggered.connect(self.thumbnail.up)
                self.top.triggered.connect(self.thumbnail.top)
                self.bottom.triggered.connect(self.thumbnail.bottom)
                self.delete.triggered.connect(self.thumbnail.delete)
                self.new.triggered.connect(self.thumbnail.newPage)

                self.tabWidget.addTab(self.newWidget,"" + workspace + "/" + dokument)
                self.tabWidget.setCurrentWidget(self.newWidget)
                self.innerTabWidget.addTab(self.thumbnail, "Thumbnail")   
                self.innerTabWidget.addTab(self.page, "Bookmark")                         
                self.innerTabWidget.setCurrentWidget(self.thumbnail)
                self.layoutG.addWidget(self.treeWidget,0,0)
                self.treeWidget.populate(dokument,workspace)
                self.iface.layout.addWidget(self.mainWidget)
                
                self.newWidget.layout().setAlignment(self.innerTabWidget, Qt.AlignLeft)
                self.dokument = dokument
                self.workspace = workspace



                self.recnik[self.id] = self.treeWidget
                self.id += 1
        for index, treeView in self.recnik.items():
            treeView.clicked.connect(lambda: self.treeClicked(index))
        
                

        

        
    def treeClicked(self, index):
        tree = self.recnik[index]
        for i in tree.selectedIndexes():
            stranica = i.data()   
        dokument = self.dokument
        workspace = self.workspace  
        self.stranica_plugin.onClicked(dokument, workspace, stranica)
        tree.clearSelection()



                       

        
                        
                            
                         


    

    



   
