from plugin_framework.extension import Extension
from radni_prostor.dock_widget import DockWidget
from radni_prostor.treeView import TreeView
from plugins.stranica_plugin import plugin
from PySide2 import QtCore
from PySide2 import QtWidgets, QtCore
from rad_sa_celim_dokumentom.ui.tool_bar import ToolBar
import json


class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije

        """
        # 
        super().__init__(specification, iface)
       
        # self.button_update = QtWidgets.QPushButton("Refresh workspace")
        # self.layout_button = QtWidgets.QGridLayout()
        self.kontejner = QtWidgets.QWidget()
        # self._layout = QtWidgets.QHBoxLayout(self.kontejner)
        self._layout = QtWidgets.QVBoxLayout()

        

        


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.treeView = TreeView()
        self.dock_widget = DockWidget("Workspace", self.iface)
        self.iface.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_widget)
        self.dock_widget.setWidget(self.kontejner)
        self.kontejner.setLayout(self._layout)
        # self._layout.addWidget(self.button_update)
        self._layout.addWidget(self.treeView)
        
        # self.button_update.clicked.connect(self.treeView.kliknuto_update)

        self.activated = True
        print("Activated")
        

    def deactivate(self):
        self.iface.removeDockWidget(self.dock_widget)
        self.treeView.deleteLater()
        self.activated = False
        print("Deactivated")
    
    def update_radni_prostor(self):
        self.dock_widget
    
    def remove_document (self):
                for i in self.treeView.selectedIndexes():
                    text = i.data()
                    print("FDsjbhs")
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

