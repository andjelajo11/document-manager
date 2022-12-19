from PySide2 import QtCore
from PySide2 import QtCore, QtGui, QtWidgets
from rad_sa_celim_dokumentom.interfejsi.extension_dok_celina import ExtensionDokument
import json
import radni_prostor

class CreateDialog(QtWidgets.QDialog):
    created = QtCore.Signal()

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Create")
        self._layout = QtWidgets.QGridLayout()
        self.setLayout(self._layout)
        # self._layout1 = QtWidgets.QGridLayout()
        # self._layout2 = QtWidgets.QGridLayout()
        # self._layout3 = QtWidgets.QGridLayout()

        self._workspace = QtWidgets.QLabel("Radni prostor:")
        self._kolekcija = QtWidgets.QLabel("Kolekcija:")
        self._dokument = QtWidgets.QLabel("Naziv novog dokumenta:")
        
        self._workspace_input = QtWidgets.QLineEdit()
        self._kolekcija_input = QtWidgets.QLineEdit()
        self._dokument_input = QtWidgets.QLineEdit()
        

        
        self.populate_dialog()


        self.resize(300, 300)
    
    def populate_dialog(self):
        self._layout.addWidget(self._workspace) 
        self._layout.addWidget(self._workspace_input) 

        self._layout.addWidget(self._kolekcija) 
        self._layout.addWidget(self._kolekcija_input) 
       
        self._layout.addWidget(self._dokument)        
        self._layout.addWidget(self._dokument_input) 
        
        self.button_create = QtWidgets.QPushButton("Dodaj Dokument")
        self.button_create.clicked.connect(self.dugme_kliknuto)

        self._layout.addWidget(self.button_create)     
        self.button_create.clicked.connect(self.dugme_kliknuto)
   
    def dugme_kliknuto(self):
        self.workspace_uneto = self._workspace_input.text()
        self.kolekcija_uneto = self._kolekcija_input.text()
        self.dokument_uneto = self._dokument_input.text()
        
        
        with open('radni_prostor/workspace.json' ) as data_file:  
            data = json.load(data_file)
            print("dokument je unet")
            print ( "da vidjemo:")
            print(self.workspace_uneto)
            print(".")
        for i in data:
                print("dokument je unet2")
                if i == self.workspace_uneto:
                    print("dokument je unet3")
                    i = self.workspace_uneto
                    print("dokument je unet4")
                    for j in data[i]:
                        print("dokument je unet5")
                        if j == self.kolekcija_uneto:
                            print("dokument je unet6")
                            j = self.kolekcija_uneto
                            print("dokument je unet7")
                            for z in data[i][j]:
                                print("dokument je unet8")
                                if self.dokument_uneto not in data[i][j]:
                                    print("dokument je unet9")
                                    z == self.dokument_uneto
                                    z = self.dokument_uneto
                                    print("dokument je unet10")
                                    data[i][j].append(z)
                                    with open('radni_prostor/workspace.json', 'w' ) as data_ffile:  
                                        # data_file.write(str(data))
                                        data_json = json.dumps(data, sort_keys=True, indent=4)
                                    # data_file = data
                                        data_ffile.write(str(data_json))
                                    return data
                                    print("dokument je unet11")
                                    #return data #novi json sa dodatim dokumentom koji treba prikazati na workspace widgetu
                                else : print("Naziv dokumenta nije validan")                           

        




        
        
