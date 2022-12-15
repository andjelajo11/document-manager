from PySide2.QtWidgets import QTreeView, QMenu, QAction
from PySide2.QtCore import QEvent
from PySide2.QtGui import QStandardItemModel
from integrativna_komponenta.ui.standard_item import StandardItem
import json




class TreeView(QTreeView):
        def __init__(self):
                super().__init__()
                self.model = QStandardItemModel()       




                self.newWorkspace = QAction("Novi Workspace", self)
                self.newCollection = QAction("Nova Kolekcija", self)
                self.deleteWorksace = QAction("Obrisi Workspace", self)
                self.deleteCollection = QAction("Obrisi Kolekciju", self)
                self.installEventFilter(self)


        def populate(self):
                self.rootNode = self.model.invisibleRootItem()
                self.setHeaderHidden(True)
                with open('radni_prostor/workspace.json') as data_file:  
                        data = json.load(data_file)
                data_file.close()
                for workspace in data:
                        workspace1 = StandardItem(workspace)
                        self.rootNode.appendRow(workspace1)  # Print the workspace name

                        # Loop through the collections in the workspace
                        for collection in data[workspace]:
                                kolekcija = StandardItem(collection)
                                workspace1.appendRow(kolekcija)  # Print the collection name

                                # Loop through the documents in the collection
                                for document in data[workspace][collection]:
                                        dokument = StandardItem(document)
                                        kolekcija.appendRow(dokument)



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


        def eventFilter(self, source, event):
                for ix in self.selectedIndexes():
                        self.text = ix.data()            
                        if event.type() == QEvent.ContextMenu and source is self:
                                menu = QMenu()
                                menu.addAction(self.newWorkspace)
                                menu.addAction(self.newCollection)
                                menu.addAction(self.deleteWorksace)
                                menu.addAction(self.deleteCollection)
                                
                                                
                                menu.triggered[QAction].connect(self.on_menu_triggered)
                                menu.exec_(event.globalPos())  
                                
                                
                                
                                return True
                        
                return super().eventFilter(source, event)
                
        def on_menu_triggered(self, action):
                if action == self.newWorkspace:
                        self.noviWorkspace()
                elif action == self.newCollection:
                        self.novaKolekcija()
                elif action == self.deleteCollection:
                        self.obrisiKolekciju()
                elif action == self.deleteWorksace:
                        self.obrisiWorkspace()

        
        def obrisiWorkspace(self):
                for i in self.selectedIndexes():
                    text = i.data()
                
                if "workspace" in text:
                        with open('radni_prostor/workspace.json', 'r') as f:
                                data = json.load(f)
                                
                        del data[text]
                        
                        with open('radni_prostor/workspace.json', 'w') as f:
                                json.dump(data, f)
                self.model.clear()

                self.populate()
        
        def obrisiKolekciju(self):
                for i in self.selectedIndexes():
                    text = i.data()

                for i in self.selectedIndexes():
                        parent = i.parent()

                print(text)
                print(parent.data())

                with open('radni_prostor/workspace.json', 'r') as f:
                        data = json.load(f)
                for workspace in data:
                        if workspace == parent.data():
                                for collection in data[workspace]:
                                        if collection == text:
                                        # Delete the collection from the JSON file
                                                data[workspace].pop(collection)
                                        # Save the updated data to the JSON file
                                                with open('radni_prostor/workspace.json', 'w') as data_file:
                                                        json.dump(data, data_file, sort_keys=True, indent=4)
                                                break

                # Close the JSON file
                data_file.close()
                self.model.clear()

                self.populate()
                
              



        
        def noviWorkspace(self):
                with open('radni_prostor/workspace.json', 'r') as f:
                        data = json.load(f)
                        
                max_workspace_num = 0
                for workspace_name in data:
                        workspace_num = int(workspace_name.split('workspace')[1])
                        if workspace_num > max_workspace_num:
                                max_workspace_num = workspace_num
                        
                new_workspace_num = max_workspace_num + 1
                new_workspace_name = f'workspace{new_workspace_num}'
                
                data[new_workspace_name] = {}
                
                with open('radni_prostor/workspace.json', 'w') as f:
                        json.dump(data, f)
                
                self.model.clear()

                self.populate()
        
        def novaKolekcija(self):
                for i in self.selectedIndexes():
                    text = i.data()
                with open('radni_prostor/workspace.json') as data_file:  
                        data = json.load(data_file)
                data_file.close()

                # Get the number of collections in the workspace
                num_collections = len(data[text])

                # Create a new collection name by appending the number of collections to "kolekcija"
                new_collection_name = "kolekcija" + str(num_collections + 1)

                # Add the new collection to the workspace in the JSON data
                data[text][new_collection_name] = []

                # Save the updated JSON data to the file
                with open('radni_prostor/workspace.json', 'w') as data_file:  
                        json.dump(data, data_file, indent=4)
                data_file.close()
                self.model.clear()

                self.populate()
        
