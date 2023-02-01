from PySide2.QtWidgets import QTreeView, QMenu, QAction, QMessageBox, QAbstractItemView
from PySide2.QtCore import QEvent, Qt
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
                        with open('workspaces/' + file + ".wsp") as data_file:
                                data = json.load(data_file)
                
                for workspace in data:
                        workspace1 = StandardItem(workspace)
                        self.rootNode.appendRow(workspace1)  

                        for collection in data[workspace]:
                                kolekcija = StandardItem(collection)
                                workspace1.appendRow(kolekcija) 

                                for document in data[workspace][collection]:
                                        dokument = StandardItem(document)
                                        kolekcija.appendRow(dokument)



                self.setModel(self.model)  


        def kliknuto_update (self, file):
                self.model.clear()
                self.rootNode = self.model.invisibleRootItem()
                self.setHeaderHidden(True)
                if "workspaces/" in file:
                        with open(file) as data_file:  
                                data = json.load(data_file)
                        data_file.close()
                else:
                        with open('workspaces/' + file + ".wsp") as data_file:
                                data = json.load(data_file)
                                
                
                for workspace in data:
                        workspace1 = StandardItem(workspace)
                        
                        self.rootNode.appendRow(workspace1) 

                        for collection in data[workspace]:
                                kolekcija = StandardItem(collection)
                                workspace1.appendRow(kolekcija)  

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
                with open('workspaces/'+ parent.data() + '.wsp', 'r') as f:
                        data = json.load(f)
                for workspace in data:
                        if workspace == parent.data():
                                for collection in data[workspace]:
                                        if collection == text:
                                                data[workspace].pop(collection)
                                                with open('workspaces/'+ parent.data() + '.wsp', 'w') as data_file:
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
                        x = i.parent()                
                        parent = x.data()
                if parent is not None:
                        with open('workspaces/'+ parent + '.wsp') as data_file:  
                                data = json.load(data_file)
                        data_file.close()

                        num_collections = len(data[parent])
                        print(len(data[parent]))

                        new_collection_name = "kolekcija" + str(num_collections + 1)

                        data[parent][new_collection_name] = []

                        with open('workspaces/'+ parent + '.wsp', 'w') as data_file:  
                                json.dump(data, data_file, indent=4)
                        data_file.close()
                        self.model.clear()

                        self.populate(parent)
                else:
                        with open('workspaces/'+ text + '.wsp') as data_file:  
                                data = json.load(data_file)
                        data_file.close()

                        num_collections = len(data[text])
                        print(len(data[text]))

                        new_collection_name = "kolekcija" + str(num_collections + 1)
                        print(new_collection_name)
                        data[text][new_collection_name] = []

                        with open('workspaces/'+ text + '.wsp', 'w') as data_file:  
                                json.dump(data, data_file, indent=4)
                        data_file.close()
                        self.model.clear()

                        self.populate(text)
        
        def drag_and_drop(self):
                self.setDragEnabled(True)
                self.setAcceptDrops(True)
                self.setDropIndicatorShown(True)
                self.setDragDropMode(QAbstractItemView.InternalMove)
                
                self.dragEnterEvent = self.drag_enter_event
                self.dragMoveEvent = self.drag_move_event
                self.dropEvent = self.drop_event

        def drag_enter_event(self, event):
                selected_item = self.selectedIndexes()[0]
                if event.mimeData().hasText() and selected_item.data() == "dokument": 
                        event.accept()

        def drag_move_event(self, event):
                index = self.indexAt(event.pos())
                if index.isValid() and self.model().itemFromIndex(index).data() == "kolekcija":
                        event.setDropAction(Qt.CopyAction)
                        event.accept()
                else:
                        event.ignore()


        def drop_event(self, event):
                if event.mimeData().hasUrls():
                        
                                drop_index = self.indexAt(event.pos())
                                
                                urls = event.mimeData().urls()
                                
                                target_index = self.indexAt(event.pos())
                                
                                target_item = self.model.itemFromIndex(target_index)

                                if target_item.text() == "kolekcija":
                                        for url in urls:
                                                file_path = url.toLocalFile()

                                        self.add_to_treeview(file_path, target_item)

                                        event.accept()
                                else:
                                        event.ignore()
                else:
                        event.ignore()
                        
