from plugin_framework.extension import Extension
from radni_prostor.dock_widget import DockWidget
from radni_prostor.treeView import TreeView
from PySide2 import QtGui
from PySide2 import QtWidgets, QtCore
from plugins.otvoreni_dokument import plugin as otvoreni
from plugins.stranica_plugin import plugin as stranica
import json
import os

class Plugin(Extension):
    id = 0
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """
        super().__init__(specification, iface)
        self.otvoreni_plugin = otvoreni.Plugin(specification, iface)

        self.open = QtWidgets.QAction(QtGui.QIcon("resources/icons/new-workspace.png"),"Open Workspace")
        self.new = QtWidgets.QAction(QtGui.QIcon("resources/icons/new-workspace.png"),"New Workspace")
        self.delete = QtWidgets.QAction(QtGui.QIcon("resources/icons/delete-workspace.png"),"Delete Workspace")

        self.delete.triggered.connect(self.izbrisiworkspace)
        self.open.triggered.connect(self.izaberiWorkspace)
        self.new.triggered.connect(self.noviWorkspace)

    def activate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["workspace_plugin"] = True
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file, indent=2)   
            
        self.activated = True

        self.iface.add_menu_action("&File", self.open)
        self.iface.add_menu_action("&File", self.new)
        self.iface.add_menu_action("&File", self.delete)
        self.file_names = []
        self.recnik = {}

        self.kontejner = QtWidgets.QWidget()
        self._layout = QtWidgets.QVBoxLayout()

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)

        self.dock_widget = DockWidget("Workspace", self.iface)
        self.iface.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_widget)
        self.dock_widget.setWidget(self.kontejner)
        self.kontejner.setLayout(self._layout)
        self._layout.addWidget(self.tabWidget)
        

        

        self.activated = True
        print("Activated")
        

    def deactivate(self):
        self.iface.removeDockWidget(self.dock_widget)
        self.treeView.deleteLater()
        self.activated = False
        print("Deactivated")

    def delete_tab(self, index):
        #zatvaranje taba brise naziv workspace iz json fajla -> workspace je zatvoren
        with open('rad_sa_celim_dokumentom/workspace_otvoreni.json') as data_file: 
            data = json.load(data_file)
        tab_text = self.tabWidget.tabText(index)
        if tab_text in data:
            data.remove(tab_text)
            print(data)
            with open('rad_sa_celim_dokumentom/workspace_otvoreni.json', 'w') as data_ffile: 
                    data_json = json.dumps(data, sort_keys=True, indent=4)
                    data_ffile.write(str(data_json))        
        self.tabWidget.removeTab(index)
        
    def izaberiWorkspace(self):
        path = 'workspaces'
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(path)
        file_name, _ = dialog.getOpenFileName()
        print(file_name)
        self.kontejner = QtWidgets.QWidget()
        self._layout = QtWidgets.QVBoxLayout()


        if file_name != "":
            self.treeView = TreeView()
            newFile = file_name.split("/")[-1].split(".")[0]
            self.tabWidget.addTab(self.treeView, newFile)
            print(newFile)
            # workspace = file_name.split(".")[0]
            self.treeView.populate(file_name)
            

            self.file_names.append(file_name)

            with open("rad_sa_celim_dokumentom/workspace_otvoreni.json", "r") as json_file:
                kontekst_workspace = json.load(json_file)
            if newFile in kontekst_workspace:
                print("workspace je vec upisan")
            else:
                kontekst_workspace.append(newFile) 
                with open('rad_sa_celim_dokumentom/workspace_otvoreni.json', 'w') as doc_ffile:
                    json.dump(kontekst_workspace, doc_ffile, sort_keys=True, indent=4)
                    # doc_ffile.write(str(doc_json))
                                            


            self.recnik[self.id] = self.treeView
            self.id += 1
            for index, self.treeView in self.recnik.items():
                self.treeView.doubleClicked.connect(lambda: self.treeClicked(index))

        


        
    def treeClicked(self, index):
        treeView = self.recnik[index]
        for i in treeView.selectedIndexes():
            dokument = i.data()
        for i in treeView.selectedIndexes():
            kolekcija = i.parent()
            workspace = kolekcija.parent().data()
        self.otvoreni_plugin.onClicked(dokument, workspace)
        treeView.clearSelection()
        

    def izbrisiworkspace(self):
        path = 'workspaces'
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(path)
        file_name, _ = dialog.getOpenFileName()
        print(file_name)
        if file_name != "":
            if file_name not in self.file_names:
                os.remove(file_name)

    def noviWorkspace(self):
        workspace_name, ok = QtWidgets.QInputDialog.getText(self.iface, "Workspace Name", "Enter the name for the new workspace:")
        if ok:
            # Create the JSON data with the user-provided names
            data = {
                workspace_name: {
            }
            }
            # Write the JSON data to a file
            with open('workspaces/' + workspace_name + ".json", 'w') as data_file:
                data_json = json.dumps(data, sort_keys=True, indent=4)
                data_file.write(data_json)
        
        

    


    
    
    def remove_document (self):
                for i in self.treeView.selectedIndexes():
                    text = i.data()
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

    