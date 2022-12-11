from PySide2 import QtWidgets

from plugin_framework.extension import Extension
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
from radni_prostor.dock_widget import DockWidget
from radni_prostor.treeView import TreeView
from PySide2 import QtCore
from rad_sa_celim_dokumentom.ui.tool_bar import ToolBar
from rad_sa_celim_dokumentom.ui.create_dialog import CreateDialog
from rad_sa_celim_dokumentom.ui.rename_dialog import RenameDialog
import json

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """

        # 
        super().__init__(specification, iface)
        self.layout = iface.layout
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        # self.dock = self.iface.findChildren(QtWidgets.QDockWidget)
        # self.dockWidget = self.dock[1].widget()
        # for d in self.dock:
        #      self.dock = d #vraca kontejner QDockWidget
        #      self.dockWidget = self.dock.widget()
        #      return self.dockWidget
        # self.dockWidget = self.dock.widget()
        # self.layout = self.dockWidget.findChildren(QtWidgets.QVBoxLayout) # vraca QVBoxLayout
        # self.treeView = self.layout.findChildren(QtWidgets.QTreeView)# vraca QTreeView

        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.toolbar = ToolBar()        
        self.iface.addToolBar(self.toolbar)
        self.toolbar.add_crud()
        self.toolbar.create_action.triggered.connect(self.show_create_dialog)
        self.toolbar.delete_action.triggered.connect(self.remove_document)
        self.toolbar.rename_action.triggered.connect(self.rename_document)
        self.layout.addWidget(self.tabWidget) 
        
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
            self.dockWidget = dock
        self.kontejner = self.dockWidget.widget()
        
        for dock1 in self.kontejner.findChildren(QtWidgets.QVBoxLayout):
            self.layout = dock1
        self.layout.insertWidget(0, self.toolbar)
        
        for dock2 in self.kontejner.findChildren(QtWidgets.QTreeView):
            self.tree_view = dock2
        # self.layout.treeView
        self.activated = True
        print("Activated")
        
        #TODO: dodati remove tabWidget 
    def deactivate(self):
        self.iface.removeToolBar(self.toolbar)
        print("Deactivated")
    
        
    def show_create_dialog(self):
        self.create_dialog = CreateDialog()
        self.create_dialog.show()

    def remove_document (self):
                for i in self.tree_view.selectedIndexes():
                    text = i.data()
                    print(text)
                    # return text
                    with open('radni_prostor/workspace.json' ) as data_file:  
                            data = json.load(data_file)
                    for i in data:
                            for j in data[i]:
                                    for z in data[i][j]:
                                            if z == text:
                                                    z = text
                                                    data[i][j].remove(z)
                                                    with open('radni_prostor/workspace.json', 'w' ) as data_ffile: 
                                                            data_json = json.dumps(data, sort_keys=True, indent=4)
                                                            data_ffile.write(str(data_json))
                                                    with open('rad_sa_celim_dokumentom/spec_ceoDokument.json') as doc_file:
                                                        document = json.load(doc_file)
                                                        del document[text]
                                                    with open('rad_sa_celim_dokumentom/spec_ceoDokument.json', 'w') as doc_ffile:
                                                        doc_json = json.dumps(document, sort_keys=True, indent=4)
                                                        doc_ffile.write(str(doc_json))
                                                    self.tree_view.kliknuto_update()  
    
    def rename_document (self):
                self.rename_dialog = RenameDialog()
                self.rename_dialog.show()
                self.rename_dialog.button_rename.clicked.connect(self.rename_dugme_kliknuto)

    def rename_dugme_kliknuto (self):
                self.rename_uneto = self.rename_dialog.rename_input.text()
                for i in self.tree_view.selectedIndexes():
                    text = i.data()
                    with open('radni_prostor/workspace.json' ) as data_file:  
                            data = json.load(data_file)
                    for i in data:
                            for j in data[i]:
                                    for z in data[i][j]:
                                            if z == text:
                                                z = text
                                                y = self.rename_uneto
                                                print(data[i][j])
                                                print(z)
                                                print(y)
                                                data[i][j][data[i][j].index(z)] = y
                                                with open('radni_prostor/workspace.json', 'w' ) as data_ffile: 
                                                    data_json = json.dumps(data, sort_keys=True, indent=4)
                                                    data_ffile.write(str(data_json))
                                                with open('rad_sa_celim_dokumentom/spec_ceoDokument.json') as doc_file:
                                                    document = json.load(doc_file)
                                                    document[self.rename_uneto] = document.pop(text)
                                                    print(document)
                                                with open('rad_sa_celim_dokumentom/spec_ceoDokument.json', 'w') as doc_ffile:
                                                    doc_json = json.dumps(document, sort_keys=True, indent=4)
                                                    doc_ffile.write(str(doc_json))

                                                # data[i][j].insert(data[i][j].index(z), y )
                                                print(data)
                                                break
