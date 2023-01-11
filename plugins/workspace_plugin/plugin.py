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
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """
        super().__init__(specification, iface)
        self.otvoreni_plugin = otvoreni.Plugin(specification, iface)
        self.stranica_plugin = stranica.Plugin(specification, iface)
        self.open = QtWidgets.QAction(QtGui.QIcon("resources/icons/new-workspace.png"),"Open Workspace")
        self.open.triggered.connect(self.izaberiWorkspace)

        self.new = QtWidgets.QAction(QtGui.QIcon("resources/icons/new-workspace.png"),"New Workspace")
        self.new.triggered.connect(self.noviWorkspace)

        self.delete = QtWidgets.QAction(QtGui.QIcon("resources/icons/delete-workspace.png"),"Delete Workspace")
        self.delete.triggered.connect(self.izbrisiworkspace)

    def activate(self):
        self.iface.add_menu_action("&File", self.open)
        self.iface.add_menu_action("&File", self.new)
        self.iface.add_menu_action("&File", self.delete)
        self.file_names = []
        

        

        self.activated = True
        print("Activated")
        

    def deactivate(self):
        self.iface.removeDockWidget(self.dock_widget)
        self.treeView.deleteLater()
        self.activated = False
        print("Deactivated")

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
            self.dock_widget = DockWidget("Workspace", self.iface)
            self.iface.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_widget)
            self.dock_widget.setWidget(self.kontejner)
            self.kontejner.setLayout(self._layout)
            self._layout.addWidget(self.treeView)
            
            self.treeView.populate(file_name)
            self.otvoreni_plugin.checkForWorkspace()
            self.stranica_plugin.checkForWorkspace()

            self.file_names.append(file_name)

        
    
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

    