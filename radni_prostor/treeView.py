from PySide2.QtWidgets import QTreeView, QMenu, QAction, QMessageBox
from PySide2.QtCore import QEvent
from PySide2.QtGui import QStandardItemModel
from integrativna_komponenta.ui.standard_item import StandardItem
import json




class TreeView(QTreeView):
        def __init__(self):
                super().__init__()
                self.model = QStandardItemModel()       




                self.newCollection = QAction("Nova Kolekcija", self)
                self.deleteCollection = QAction("Obrisi Kolekciju", self)
                self.installEventFilter(self)

                self.doubleClicked.connect(self.onClicked)


        def onClicked(self):
                with open("plugin_framework/plugins.json", "r") as json_file:
                        plugins = json.load(json_file)

                
                for ix in self.selectedIndexes():
                        text = ix.data()
                if "dokument" in text:
                        if plugins["otvoreni_dokument"] == False:
                                message_box = QMessageBox()
                                message_box.setWindowTitle("Notification")
                                message_box.setText("Nije aktivirana komponenta za rad sa otvorenim dokumentima.")
                                message_box.exec_()


        def populate(self, file):
                self.rootNode = self.model.invisibleRootItem()
                self.setHeaderHidden(True)
                if "workspaces/" in file:
                        with open(file) as data_file:  
                                data = json.load(data_file)
                        data_file.close()
                else:
                        with open('workspaces/' + file + ".json") as data_file:
                                data = json.load(data_file)
                
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
                                menu.addAction(self.newCollection)
                                menu.addAction(self.deleteCollection)
                                
                                                
                                menu.triggered[QAction].connect(self.on_menu_triggered)
                                menu.exec_(event.globalPos())  
                                
                                
                                
                                return True
                        
                return super().eventFilter(source, event)
                
        def on_menu_triggered(self, action):
                if action == self.newCollection:
                        self.novaKolekcija()
                elif action == self.deleteCollection:
                        self.obrisiKolekciju()

        

        
        def obrisiKolekciju(self):
                for i in self.selectedIndexes():
                    text = i.data()

                for i in self.selectedIndexes():
                        parent = i.parent()

                print(text)
                print(parent.data())
                work = parent.data()
                with open('workspaces/'+ parent.data() + '.json', 'r') as f:
                        data = json.load(f)
                for workspace in data:
                        if workspace == parent.data():
                                for collection in data[workspace]:
                                        if collection == text:
                                                data[workspace].pop(collection)
                                                with open('workspaces/'+ parent.data() + '.json', 'w') as data_file:
                                                        json.dump(data, data_file, sort_keys=True, indent=4)
                                                break


                data_file.close()
                self.model.clear()
                
                print(work)
                self.populate(work)
                
              
        
        def novaKolekcija(self):
                for i in self.selectedIndexes():
                    text = i.data()


                for i in self.selectedIndexes():
                        parent = i.parent()
                
                parent = parent.data()
                with open('workspaces/'+ parent + '.json') as data_file:  
                        data = json.load(data_file)
                data_file.close()

                num_collections = len(data[parent])
                print(len(data[parent]))

                new_collection_name = "kolekcija" + str(num_collections + 1)

                # Add the new collection to the workspace in the JSON data
                data[parent][new_collection_name] = []

                # Save the updated JSON data to the file
                with open('workspaces/'+ parent + '.json', 'w') as data_file:  
                        json.dump(data, data_file, indent=4)
                data_file.close()
                self.model.clear()

                self.populate(parent)
        
