from PySide2.QtWidgets import QTreeView, QMessageBox
from PySide2.QtGui import QStandardItemModel, QPixmap
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

                self.clicked.connect(self.onClicked)


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




        

