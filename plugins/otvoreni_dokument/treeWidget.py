from PySide2.QtWidgets import QTreeView, QMenu, QAction
from PySide2.QtGui import QStandardItemModel
from integrativna_komponenta.ui.standard_item import StandardItem
from PySide2.QtCore import QEvent
import json




class TreeView(QTreeView):
    def __init__(self):
        super().__init__()
        self.model = QStandardItemModel()
        self.delete = QAction("Delete", self)
        self.newPage = QAction("Nova Stranica", self)
        self.newMono = QAction("Novi monotip", self)
        self.installEventFilter(self)

    def populate(self, dokument):
        self.dokument = dokument
        self.rootNode = self.model.invisibleRootItem()
        self.setHeaderHidden(True)
        with open('radni_prostor/dokumenti.json') as data_file:  
                data = json.load(data_file)
        data_file.close()


        counter = 1

        for i in data[dokument]:
            naziv = StandardItem(i["naziv"])
            self.rootNode.appendRow(naziv)
            for y in i:
                if "hyperlink" + str(counter) in y:     
                    hiperlinkovi = StandardItem(y)  
                    naziv.appendRow(hiperlinkovi)          
                    for x in i.values():
                        # print(x)
                        for z in x:
                            # print(z)
                            for j in z:
                                if "hyperlink" + str(counter) in j:
                                    hiperlink = StandardItem(j)
                                    hiperlinkovi.appendRow(hiperlink)
                    counter +=1  
                elif "hyperlink" + str(counter + 1) in y:
                    hiperlinkovi = StandardItem(y)  
                    naziv.appendRow(hiperlinkovi)          
                    for x in i.values():
                        # print(x)
                        for z in x:
                            # print(z)
                            for j in z:
                                if "hyperlink" + str(counter + 1) in j:
                                    hiperlink = StandardItem(j)
                                    hiperlinkovi.appendRow(hiperlink)
                    counter +=1 
    


        

        self.expandAll()

        self.setModel(self.model)  


    
    def eventFilter(self, source, event):
        for ix in self.selectedIndexes():
            self.text = ix.data()            
            if event.type() == QEvent.ContextMenu and source is self:
                menu = QMenu()
                menu.addAction(self.delete)
                menu.addAction(self.newPage)
                
                                
                menu.triggered[QAction].connect(self.on_menu_triggered)
                menu.exec_(event.globalPos())  
                    
                    
                    
            return True
            
        return super().eventFilter(source, event)
        
    def on_menu_triggered(self, action):
        if action == self.delete:
            self.obrisi()
            print("test")
        elif action == self.newPage:
            self.dodajStranicu()

    
    def obrisi(self):

        hiperlink = self.text

        with open('radni_prostor/dokumenti.json', "r") as f:
            data = json.load(f)

        for i in data[self.dokument]:
            if hiperlink in i:
                print(i[hiperlink])
                del i[hiperlink]
                break
            for j in i[hiperlink.split(".", 1)[0]]:
                if hiperlink in j:
                    print(j[hiperlink])
                    del j[hiperlink]
                break
            else:
                continue

            
        # Save the modified data back to the file
        with open('radni_prostor/dokumenti.json', "w") as f:
            json.dump(data, f)  

        self.model.clear()

        self.populate(self.dokument)



              
    def dodajStranicu(self):

        with open("radni_prostor/dokumenti.json", "r") as json_file:
            json_object = json.load(json_file)

        lista = []
        for x in json_object[self.dokument][0]:
            if "hyperlink" in x:
                lista.append(x)
        json_object[self.dokument][0].update({"hyperlink" + str(len(lista) + 1) : [{}]})


        with open("radni_prostor/dokumenti.json", "w") as json_file:
            json.dump(json_object, json_file)
        
        self.model.clear()

        self.populate(self.dokument)