from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QToolBar, QAction, QGridLayout, QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
import json



from PySide2 import QtWidgets

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.mainLayoutV = QVBoxLayout() #gore i dole na main widgetu
        self.mainWidget = QtWidgets.QWidget()

        toolbar = QToolBar()   
        left = QAction(QIcon("resources/icons/arrow-left.png"),"left",self.mainLayoutV)
        right = QAction(QIcon("resources/icons/arrow-right.png"),"right",self.mainLayoutV)
        up = QAction(QIcon("resources/icons/arrow-up.png"),"up",self.mainLayoutV)
        down = QAction(QIcon("resources/icons/arrow-down.png"),"down",self.mainLayoutV)
        delete = QAction(QIcon("resources/icons/kanta.png"),"delete",self.mainLayoutV)
        
        self.mainWidget.setLayout(self.mainLayoutV)
        self.mainLayoutV.addWidget(toolbar)

        self.dockWidget = QtWidgets.QDockWidget
        
        toolbar.addAction(left)
        toolbar.addAction(right)
        toolbar.addAction(up)
        toolbar.addAction(down)
        toolbar.addAction(delete)

        down.triggered.connect(self.down)
        right.triggered.connect(self.right)
        left.triggered.connect(self.left)
        up.triggered.connect(self.up)
        delete.triggered.connect(self.delete)

        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        self.activated = True
        
        
        
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
            self.dockWidget = dock
        self.treeView1 = self.dockWidget.widget()
        
        
        
        
        self.treeView1.clicked.connect(self.mainTreeClicked)  
        
    

    def mainTreeClicked(self):

        self.mainWidget1 = self.iface.layout.itemAt(0).widget()
        print(type(self.mainWidget1))
        self.tab = self.mainWidget1.layout().itemAt(0).widget()
        print(type(self.tab))
        
        self.stranica = self.tab.currentWidget()
        print(type(self.stranica))
        self.treeView = self.stranica.layout().itemAt(0).widget()
        self.treeView.clicked.connect(self.onClicked) 
    

    def deactivate(self):
        print("Deactivated")
        self.activated = False  
        self.iface.layout.itemAt(0).widget().setParent(None)


    def delete_tab(self,index):
        self.tabWidget.removeTab(index)

        
    def onClicked(self):

        for ix in self.treeView.selectedIndexes():
            text = ix.data()  
            if "stranica" in text:
                self.iface.layout.addWidget(self.mainWidget)
                
                self.grid = QGridLayout()
                
                self.page = QtWidgets.QWidget()
                
                
                self.page.setLayout(self.grid)


                self.tester = 1
                self.row = self.grid.rowCount() - 1
                self.column = self.grid.columnCount() - 1

                self.label = QLabel()
                self.label.setText("Slot" + str(self.tester))        
                self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
                self.label.setLineWidth(1)
                self.label.setFocusPolicy(Qt.StrongFocus)
            
                

                
                print(text)          
                self.mainLayoutV.addWidget(self.page)
                self.grid.addWidget(self.label, 0, 0)


                print("row:")
                print(self.row)
                print("column:")
                print(self.column)
                       

        
                        
                            
                         


    def addLabel(self):
        self.label = QLabel()
        self.label.setText("Slot")        
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label.setLineWidth(1)

        if self.page.layout().itemAtPosition(self.row, self.column) is None:
            self.page.layout().addWidget(self.label, self.row, self.column)

        self.label.setFocusPolicy(Qt.StrongFocus)    


    def down(self):
        self.row += 1
        print("row:")
        print(self.row)
        print("column:")
        print(self.column)
        self.addLabel()
    
    def up(self):
        self.row -=1
        self.addLabel()
        

    def right(self):    
        self.row = 0
        self.column += 1    
        self.addLabel()        
        print("row:")
        print(self.row)
        print("column:")
        print(self.column)

    def left(self):
        self.row = 0
        if self.column > 0:
            self.column -= 1
        self.addLabel()
    

    def delete(self):
        focused_widget = QApplication.focusWidget()
        if focused_widget is not None:
            self.page.layout().removeWidget(focused_widget)
            focused_widget.deleteLater()
            

        


        

        


                 


    



   
