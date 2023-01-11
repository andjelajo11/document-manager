from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QToolBar, QAction, QGridLayout, QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, QSize
import json



from PySide2 import QtWidgets

class Plugin(Extension):
    id = 0
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        
        self.recnik = {}
        self.row = 10
        self.column = 10
        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        self.activated = True
        
        

    

    def checkForWorkspace(self):
        
        for dock in self.iface.findChildren(QtWidgets.QDockWidget):
                treeView = dock.widget().layout().itemAt(0).widget()
                self.recnik[self.id] = treeView
                self.id += 1
        for index, treeView in self.recnik.items():
            treeView.clicked.connect(lambda: self.mainTreeClicked(index))
    

    def mainTreeClicked(self, index):

        self.mainWidget1 = self.iface.layout.itemAt(0).widget()
        print(type(self.mainWidget1))
        self.tab = self.mainWidget1.layout().itemAt(0).widget()
        print(type(self.tab))
        
        self.stranica = self.tab.currentWidget()
        print(type(self.stranica))
        self.innerTab = self.stranica.layout().itemAt(1).widget()
        self.widget = self.innerTab.widget(0)
        self.treeView = self.widget.layout().itemAt(0).widget()
        self.treeView.clicked.connect(self.onClicked) 
    

    def deactivate(self):
        print("Deactivated")
        self.activated = False  
        self.iface.layout.itemAt(0).widget().setParent(None)


    def delete_tab(self,index):
        self.tabWidget.removeTab(index)

        
    def onClicked(self):
        print("dohvatili treeview")

        for ix in self.treeView.selectedIndexes():
            text = ix.data()  
            if "stranica" in text:

                self.mainLayoutV = QVBoxLayout() #gore i dole 
                self.layoutH = QHBoxLayout() #levo i desno
                self.layoutH1 = QHBoxLayout()
                
                self. innerWidgetList = []
                toolbar = QToolBar()   
                left = QAction(QIcon("resources/icons/arrow-left.png"),"left",self.mainLayoutV)
                right = QAction(QIcon("resources/icons/arrow-right.png"),"right",self.mainLayoutV)
                up = QAction(QIcon("resources/icons/arrow-up.png"),"up",self.mainLayoutV)
                down = QAction(QIcon("resources/icons/arrow-down.png"),"down",self.mainLayoutV)
                delete = QAction(QIcon("resources/icons/kanta.png"),"delete",self.mainLayoutV)
                self.main = QtWidgets.QWidget()
                self.main.setLayout(self.mainLayoutV)
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
                self.stranica.layout().addWidget(self.main, 0, 1, 2, 2)

                self.main.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

                with open('radni_prostor/dokumenti.json') as data_file:  
                    data = json.load(data_file) 
                data_file.close()   


                
                self.grid = QGridLayout()

                
                
                self.page = QtWidgets.QWidget()
                self.mainLayoutV.addWidget(self.page)
                
                self.page.setLayout(self.grid)
                self.tester = 1
                

                self.label = QLabel()
                self.label.setText("Slot" + str(self.tester))        
                self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
                self.label.setLineWidth(1)
                self.label.setFocusPolicy(Qt.StrongFocus)
            
                

                
                print(text)
                self.grid.addWidget(self.label, 10, 10)


                print("row:")
                print(self.row)
                print("column:")
                print(self.column)
                       

        
                        
                            
                         


    def addLabel(self, row, col):
        
        self.page = self.main.layout().itemAt(1).widget()
        self.activeLayout = self.page.layout()
        
        
        

        self.label = QLabel()
           
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label.setLineWidth(1)
        

        if self.page.layout().itemAtPosition(row, col) is None:
            self.tester += 1
            self.label.setText("Slot" + str(self.tester))     
            self.activeWidget.layout().addWidget(self.label, row, col)


        self.label.setFocusPolicy(Qt.StrongFocus)    


    def down(self):
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        print(row)
        print(col)
        row += 1
        self.addLabel(row, col)
    
    def up(self):
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        print(row)
        print(col)
        row -= 1
        self.addLabel(row, col)
        

    def right(self):    
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        print(row)
        print(col)
        col += 1
        self.addLabel(row, col)

    def left(self):
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        print(row)
        print(col)
        col -= 1
        self.addLabel(row, col)
    

    def delete(self):
       
        self.activeWidget = self.main.layout().itemAt(1).widget()
        focused_widget = QApplication.focusWidget()
        if focused_widget is not None:
            self.activeWidget.layout().removeWidget(focused_widget)
            focused_widget.deleteLater()
            

        


        

        


                 


    



   
