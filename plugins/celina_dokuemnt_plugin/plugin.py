from PySide2 import QtWidgets

from plugin_framework.extension import Extension
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
from radni_prostor.dock_widget import DockWidget
from radni_prostor.treeView import TreeView
from PySide2 import QtCore
from rad_sa_celim_dokumentom.ui.tool_bar import ToolBar
from rad_sa_celim_dokumentom.ui.create_dialog import CreateDialog
from rad_sa_celim_dokumentom.ui.rename_dialog import RenameDialog
from rad_sa_celim_dokumentom.ui.info_dijalog import InfoDijalog
from rad_sa_celim_dokumentom.ui.alert_dialog import AlertDialog


import json

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """

        # 
        super().__init__(specification, iface)
        self.layout = iface.layout
        # self.tabWidget = QtWidgets.QTabWidget()
        # self.tabWidget.setTabsClosable(True)
        
             

        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        
        self.toolbar = ToolBar()
        self.toolbar.add_crud()
        self.toolbar.create_action.triggered.connect(self.show_create_dialog)
        self.toolbar.delete_action.triggered.connect(self.before_remowe)
        self.toolbar.rename_action.triggered.connect(self.rename_document)
        self.rename_dialog = RenameDialog(self.iface)
        self.rename_dialog.button_rename.clicked.connect(self.rename_dugme_kliknuto)
        self.info_dijalog = InfoDijalog(self.iface)
        
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
            self.dockWidget = dock
        self.kontejner = self.dockWidget.widget()
        self.kontejner.layout().insertWidget(0, self.toolbar)
        

        
        # self.layout.treeView
        self.activated = True
        print("Activated")
        
        #TODO: dodati remove tabWidget 
    def deactivate(self):
        self.iface.removeToolBar(self.toolbar)
        print("Deactivated")
    
        
    def show_create_dialog(self):
        self.create_dialog = CreateDialog(self.iface)
        self.create_dialog.show()
        self.create_dialog.button_create.clicked.connect(self.create_refresh)


    
    def create_refresh (self):
        self.tabWidget = self.kontejner.layout().itemAt(1).widget()
        self.tree_view = self.tabWidget.currentWidget()
        self.create_dialog.dugme_kliknuto()
        self.tree_view.kliknuto_update(self.create_dialog.workspace_uneto)  

    #pre nego sto korisnik obrise dokument iskace dijalog za potvrdu
    def before_remowe (self):
        self.alert_dialog = AlertDialog(self.iface)
        self.alert_dialog.button_potvrdi.clicked.connect(self.remove_document)
        self.alert_dialog.button_cancle.clicked.connect(self.alert_dialog.reject)
        self.alert_dialog.setModal(True)
        self.alert_dialog.show()
    
    def remove_document (self):
        self.tabWidget = self.kontejner.layout().itemAt(1).widget()
        self.tree_view = self.tabWidget.currentWidget()
        with open('rad_sa_celim_dokumentom/otvoreniDokumenti.json') as data_file: 
            data_check = json.load(data_file)               
        for y in self.tree_view.selectedIndexes():
            dokument = y.data()
            print("Dokument: " + dokument)
        for i in self.tree_view.selectedIndexes():
            x = i.parent()
            kolekcija = i.parent().data()
            print("Kolekcija: " + kolekcija)
            workspace = x.parent().data()
            for y in self.tree_view.selectedIndexes():
                text = workspace + '/' + y.data()
            if text in data_check:
                self.info_dijalog.show()
            #TODO: napraviti dijalog za ovu poruku
                print("Prvo zatvorite dokument") 
            else:
                with open('workspaces/' + workspace + '.json' ) as data_file:  
                        data = json.load(data_file)
                data[workspace][kolekcija].remove(dokument)
                with open('workspaces/' + workspace + '.json', 'w') as f:
                    json.dump(data, f, indent=2)


                with open('dokumenti/' + workspace + '.json' ) as data_file:  
                    data = json.load(data_file)

                del data[dokument]
                
                with open('dokumenti/' + workspace + '.json', 'w') as f:
                    json.dump(data, f, indent=2)
                    
                self.tree_view.kliknuto_update(workspace)  

    def rename_document (self):
        self.tabWidget = self.kontejner.layout().itemAt(1).widget()
        self.tree_view = self.tabWidget.currentWidget()
        with open('rad_sa_celim_dokumentom/otvoreniDokumenti.json') as data_file: 
            data_check = json.load(data_file) 
            for i in self.tree_view.selectedIndexes():
                x = i.parent()
                workspace = x.parent().data()
            for y in self.tree_view.selectedIndexes():
                        text = workspace + '/' + y.data()
                        print(text)
                        if text in data_check:
                            self.info_dijalog.show()
                        #TODO: napraviti dijalog za ovu poruku
                            print("Prvo zatvorite dokument") 
                        else:
                            self.rename_dialog.show()

    def rename_dugme_kliknuto (self):
        self.tabWidget = self.kontejner.layout().itemAt(1).widget()
        self.tree_view = self.tabWidget.currentWidget()
        for y in self.tree_view.selectedIndexes():
            dokument = y.data()
            print("Dokument: " + dokument)
        for i in self.tree_view.selectedIndexes():
            x = i.parent()
            kolekcija = i.parent().data()
            print("Kolekcija: " + kolekcija)
            workspace = x.parent().data()
        self.rename_uneto = self.rename_dialog.rename_input.text()


        with open('workspaces/' + workspace + '.json' ) as data_file:  
            data = json.load(data_file)

        data[workspace][kolekcija][data[workspace][kolekcija].index(dokument)] = self.rename_uneto
                
        with open('workspaces/' + workspace + '.json', 'w') as f:
            json.dump(data, f, indent=2)
        with open('dokumenti/' + workspace + '.json' ) as data_file:  
            data = json.load(data_file)

        data[dokument][0]["naziv"] = self.rename_uneto
        data[self.rename_uneto] = data.pop(dokument)
                
        with open('dokumenti/' + workspace + '.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        self.tree_view.kliknuto_update(workspace)  
