from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2 import QtWidgets
import json
from PySide2.QtWidgets import  QLabel
from integrativna_komponenta.ui.layout import Layout
from PySide2.QtWidgets import QFrame, QToolBar, QAction
from PySide2.QtGui import QIcon


from PySide2 import QtWidgets

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.layoutV = QVBoxLayout() #gore i dole
        self.layoutH = QHBoxLayout() #levo i desno
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.delete_tab)
        self.widget = QtWidgets.QWidget()

        toolbar = QToolBar()   
        left = QAction(QIcon("resources/icons/arrow-left.png"),"left",self.layoutV)
        right = QAction(QIcon("resources/icons/arrow-right.png"),"right",self.layoutV)
        up = QAction(QIcon("resources/icons/arrow-up.png"),"up",self.layoutV)
        down = QAction(QIcon("resources/icons/arrow-down.png"),"down",self.layoutV)
        delete = QAction(QIcon("resources/icons/kanta.png"),"delete",self.layoutV)

        self.widget.setLayout(self.layoutV)
        self.layoutV.addWidget(toolbar)
        self.layoutV.addWidget(self.tabWidget)

        self.dockWidget = QtWidgets.QDockWidget
        
        toolbar.addAction(left)
        toolbar.addAction(right)
        toolbar.addAction(up)
        toolbar.addAction(down)
        toolbar.addAction(delete)

        up.triggered.connect(self.Up)


        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        self.activated = True
        self.iface.layout.addWidget(self.widget)
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
            self.dockWidget = dock


        self.treeView = self.dockWidget.widget()
        self.treeView.clicked.connect(self.onClicked)    
        

    def deactivate(self):
        print("Deactivated")
        self.activated = False  
        self.iface.layout.itemAt(0).widget().setParent(None)


    def delete_tab(self,index):
        self.tabWidget.removeTab(index)

        
    def onClicked(self):
        with open('radni_prostor/dokumenti.json') as data_file:  
            data = json.load(data_file) 
        data_file.close()

        

        self.widgetT = QtWidgets.QWidget() 
        
        self.label = QLabel()
        self.label.setText("ovo je test")
        
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label.setLineWidth(1)

        self.label1 = QLabel()
        self.label1.setText("ovo je test2")
        
        self.label1.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label1.setLineWidth(1)

        self.widgetT.setLayout(self.layoutH)
        self.layoutH.addWidget(self.label)
        self.layoutH.addWidget(self.label1)

        for ix in self.treeView.selectedIndexes():
            text = ix.data()
            if "dokument" in text:
                for i in data:
                    if text == i:
                        self.tabWidget.addTab(self.widgetT,"" + text)

                        

    def Up(self):
        print("radi")
        self.labelL = QLabel()
        self.labelL.setText("ovo je test")
        self.layoutV.addWidget(self.labelL)
        self.labelL.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.labelL.setLineWidth(1)
        self.layoutV.addWidget(self.label)

        self.widgetT.setLayout(self.layoutV)

        


                 


    



   
