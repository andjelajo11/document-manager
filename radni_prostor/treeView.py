from PySide2.QtWidgets import QTreeView
from PySide2.QtGui import QStandardItemModel
from integrativna_komponenta.ui.standard_item import StandardItem
import json




class TreeView(QTreeView):
        def __init__(self):
                super().__init__()
                self.model = QStandardItemModel()
                rootNode = self.model.invisibleRootItem()
                self.setHeaderHidden(True)
                with open('radni_prostor/workspace.json') as data_file:  
                        data = json.load(data_file)
                data_file.close()
                count = 1
                for i in data:
                        workspace = StandardItem(i)
                        rootNode.appendRow(workspace)
                        for v in data["workspace"]:
                                print(v)
                                kolekcija = StandardItem(v)
                                workspace.appendRow(kolekcija)
                                for x in data.values():
                                        if "kolekcija" + str(count) in x:
                                                for y in x["kolekcija" + str(count)]:
                                                        dokument = StandardItem(y)
                                                        kolekcija.appendRow(dokument)
                                        count +=1
                self.expandAll()

                self.setModel(self.model)    
