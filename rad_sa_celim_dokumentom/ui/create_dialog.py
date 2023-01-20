from PySide2 import QtCore
from PySide2 import QtCore, QtGui, QtWidgets
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
from radni_prostor.treeView import TreeView
import json
import radni_prostor

class CreateDialog(QtWidgets.QDialog):
    created = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Create")
        self.setWindowIcon(QtGui.QIcon("resources/icons/create-new-document.png"))
        self._layout = QtWidgets.QGridLayout()
        self.setLayout(self._layout)
        # self._layout1 = QtWidgets.QGridLayout()
        # self._layout2 = QtWidgets.QGridLayout()
        # self._layout3 = QtWidgets.QGridLayout()

        self._workspace = QtWidgets.QLabel("Radni prostor:")
        self._kolekcija = QtWidgets.QLabel("Kolekcija:")
        self._dokument = QtWidgets.QLabel("Naziv novog dokumenta:")
        
        self.workspace_menu = QtWidgets.QComboBox()
        self.kolekcija_menu = QtWidgets.QComboBox()

        self._workspace_input = QtWidgets.QLineEdit()
        self._kolekcija_input = QtWidgets.QLineEdit()
        self._dokument_input = QtWidgets.QLineEdit()
        
        with open('rad_sa_celim_dokumentom/workspace_otvoreni.json') as data_file:  
            self.data_workspace = json.load(data_file)
            
        self.populate_dialog()

        self.resize(300, 300)
        
        self.tree_view1 = TreeView()
        

        
    def kolekcija_podatci (self):
            self.workspace_var = self.workspace_menu.currentText()
            with open('workspaces/' + self.workspace_var + '.json') as data_file:  
                data= json.load(data_file)
                # print(self.workspace_uneto)     
                self.kolekcije = []
                
                for i in data:
                    i = self.workspace_var
                    for key in data[i].keys():
                        self.kolekcije.append(key) 
                    return (self.kolekcije)        
                print("kolekcije:")
                # print(kole)
                print(self.kolekcije)

                
    
    def update_kolekcija_combo(self):   
        self.kolekcija_menu.clear()
        self.kolekcija_menu.insertItems(0, self.kolekcija_podatci())


    def populate_dialog(self):      
        #provera koji su radni prostori otvoreni:
        
        
        
        self._layout.addWidget(self._workspace)
        self.workspace_menu.insertItems(0, self.data_workspace)
        self._layout.addWidget(self.workspace_menu) 
        # self._layout.addWidget(self._workspace_input) 

        self.kolekcija_podatci() 
        self.workspace_menu.currentTextChanged.connect(self.update_kolekcija_combo)
        
        self._layout.addWidget(self._kolekcija) 
        self.kolekcija_menu.insertItems(1, self.kolekcije)
        self._layout.addWidget(self.kolekcija_menu) 
        print(self.kolekcije)
        # self._layout.addWidget(self._kolekcija_input) 
       
        self._layout.addWidget(self._dokument)        
        self._layout.addWidget(self._dokument_input) 
        
        self.button_create = QtWidgets.QPushButton("Dodaj Dokument")
        # self.button_create.clicked.connect(self.dugme_kliknuto)

        self._layout.addWidget(self.button_create)     
        # self.button_create.clicked.connect(self.dugme_kliknuto)
        
        
    def dugme_kliknuto(self):
        self.workspace_uneto = self.workspace_menu.currentText()
        self.kolekcija_uneto = self.kolekcija_menu.currentText()
        self.dokument_uneto = self._dokument_input.text()

        print(self.workspace_uneto)
        print(self.kolekcija_uneto)
        print(self.dokument_uneto)
        
        
        with open('workspaces/' + self.workspace_uneto + '.json') as data_file:  
            data = json.load(data_file)
        if self.dokument_uneto not in data:
            data[self.workspace_uneto][self.kolekcija_uneto].append(self.dokument_uneto)
        
            with open('workspaces/' + self.workspace_uneto + '.json', 'w') as f:
                json.dump(data, f, indent=2)

        

        with open('dokumenti/' + self.workspace_uneto + '.json') as data_file:  
            data = json.load(data_file)

        if self.dokument_uneto not in data:
            data[self.dokument_uneto] = [{
      "naziv": self.dokument_uneto,
      "thumbnails": [{}]}]
        
            with open('dokumenti/' + self.workspace_uneto + '.json', 'w') as f:
                json.dump(data, f, indent=2)
        
        # with open('radni_prostor/workspace.json' ) as data_file:  
        #         data = json.load(data_file)
        #         for i in data:
        #                 print("1")
        #                 i = self.workspace_uneto
        #                 print("2")
        #                 for j in data[i]:
        #                     print("3")
        #                     if j == self.kolekcija_uneto:
        #                         print("4")
        #                         j = self.kolekcija_uneto
        #                         print("5")
        #                         if not data[i][j]: #provera da li je kolekcija prazna ako je prazna onda se izvrasava sledece
        #                             data[i][j].append(self.dokument_uneto)
        #                             print("9")
        #                             with open('radni_prostor/workspace.json', 'w' ) as data_ffile: 
        #                                 print("10")
        #                                 data_json = json.dumps(data, sort_keys=True, indent=4)
        #                                 print("11")
        #                                 data_ffile.write(str(data_json))
        #                                 print("12")
        #                             #dodavanje u json sa listom dokumenata, stranica i slotova
        #                             with open('radni_prostor/dokumenti.json') as doc_file:
        #                                 print("13")
        #                                 document = json.load(doc_file)
        #                                 print("14")
        #                                 document[self.dokument_uneto]=[{"naziv": self.dokument_uneto, "thumbnail": "slikaPath"}]
        #                                 print("15")
        #                             with open('radni_prostor/dokumenti.json', 'w') as doc_ffile:
        #                                 print("16")
        #                                 doc_json = json.dumps(document, sort_keys=True, indent=4)
        #                                 print("17")
        #                                 doc_ffile.write(str(doc_json))
        #                                 print("18")
        #                             return data
        #                         else: #ako kolekcija nije prazna
        #                             data[i][j]  
        #                             for z in data[i][j]:
        #                                 print("6")
        #                                 if self.dokument_uneto not in data[i][j]:
        #                                     print("7")
        #                                     # z == self.dokument_uneto
        #                                     z = self.dokument_uneto
        #                                     print("8")
        #                                     data[i][j].append(z)
        #                                     print("9")
        #                                     with open('radni_prostor/workspace.json', 'w' ) as data_ffile: 
        #                                         print("10")
        #                                         data_json = json.dumps(data, sort_keys=True, indent=4)
        #                                         print("11")
        #                                         data_ffile.write(str(data_json))
        #                                         print("12")
        #                                     #dodavanje u json sa listom dokumenata, stranica i slotova
        #                                     with open('radni_prostor/dokumenti.json') as doc_file:
        #                                         print("13")
        #                                         document = json.load(doc_file)
        #                                         print("14")
        #                                         document[self.dokument_uneto]=[{"naziv": z, "thumbnails": [{}]}]
        #                                         print("15")
        #                                     with open('radni_prostor/dokumenti.json', 'w') as doc_ffile:
        #                                         print("16")
        #                                         doc_json = json.dumps(document, sort_keys=True, indent=4)
        #                                         print("17")
        #                                         doc_ffile.write(str(doc_json))
        #                                         print("18")
        #                                     return data
                                            
        #                     else : print("Naziv dokumenta nije validan")
        #                 break                   
        # print(data)                            




        
        
