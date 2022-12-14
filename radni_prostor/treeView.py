from PySide2.QtWidgets import QTreeView
from PySide2.QtGui import QStandardItemModel
from integrativna_komponenta.ui.standard_item import StandardItem
import json




class TreeView(QTreeView):
        def __init__(self):
                super().__init__()
                self.model = QStandardItemModel()
                self.rootNode = self.model.invisibleRootItem()
                self.setHeaderHidden(True)
                with open('radni_prostor/workspace.json') as data_file:  
                        data = json.load(data_file)
                data_file.close()
                count = 1
                for i in data:
                        workspace = StandardItem(i)
                        self.rootNode.appendRow(workspace)
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

        def kliknuto_update (self):
                self.model.clear()
                self.model = QStandardItemModel()
                self.rootNode = self.model.invisibleRootItem()
                self.setHeaderHidden(True)
                with open('radni_prostor/workspace.json') as data_file:  
                        data = json.load(data_file)
                data_file.close()
                count = 1
                for i in data:
                        workspace = StandardItem(i)
                        self.rootNode.appendRow(workspace)
                        for v in data["workspace"]:
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
        
        def delete_selcted_item (self):
                for i in self.selectedIndexes():
                    text = i.data()
                    return text
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


                #     if "dokument" in text:
                #         print(text)