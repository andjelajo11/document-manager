from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QLabel, QFrame, QToolBar, QAction, QGridLayout, QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from plugins.stranica_plugin.clickableLabel import DoubleClickLabel
from plugins.text_plugin.plugin import Plugin as textEditorPlugin
from monotip_handler.monotip_tab import MonotipTab
import json



from PySide2 import QtWidgets

class Plugin(Extension):
    id = 0
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)

        
        self.monotipTab = MonotipTab()
        self.textPlugin = textEditorPlugin(specification, iface)
        self.recnik = {}
        self.row = 10
        self.column = 10
        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        self.activated = True
      
    

    def deactivate(self):
        print("Deactivated")
        self.activated = False  
        self.iface.layout.itemAt(0).widget().setParent(None)


    def delete_tab(self,index):
        self.tabWidget.removeTab(index)

        
    def onClicked(self, dokument, workspace, strana, thumbnailWidget):
        self.dokument = dokument
        self.workspace = workspace
        self.strana = strana
        self.thumbnail = thumbnailWidget
        if "stranica" in strana:          

            self.mainLayoutV = QVBoxLayout()
            self.main = QtWidgets.QWidget()
            self.main.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.main.setLayout(self.mainLayoutV)
        
            self.left = QAction(QIcon("resources/icons/arrow-left.png"),"left",self.mainLayoutV)
            self.right = QAction(QIcon("resources/icons/arrow-right.png"),"right",self.mainLayoutV)
            self.up = QAction(QIcon("resources/icons/arrow-up.png"),"up",self.mainLayoutV)
            self.down = QAction(QIcon("resources/icons/arrow-down.png"),"down",self.mainLayoutV)
            self.delete = QAction(QIcon("resources/icons/kanta.png"),"delete",self.mainLayoutV)



            #kreiramo novi toolbar i njegove akcije, zatim ih postavljamo na main widget
            toolbar = QToolBar()              
            toolbar.addAction(self.left)
            toolbar.addAction(self.right)
            toolbar.addAction(self.up)
            toolbar.addAction(self.down)
            toolbar.addAction(self.delete)

            self.down.triggered.connect(self.addDown)
            self.right.triggered.connect(self.addRight)
            self.left.triggered.connect(self.addLeft)
            self.up.triggered.connect(self.addUp)
            self.delete.triggered.connect(self.deleteLabel)
            
            self.mainLayoutV.addWidget(toolbar)

            
            #kreiramo page widget, kojem dodlejujemo grid layout
            
            self.grid = QGridLayout()            
            self.page = QtWidgets.QWidget()
            self.mainLayoutV.addWidget(self.page)
            
            self.page.setLayout(self.grid)
            self.tester = 1
            
            #prebrojavamo koliko ima slotova u odabranoj stranici, zatim ih postavljamo na page widget preko grid layout-a

            with open('dokumenti/' + workspace + ".json", "r") as data_file:  
                data = json.load(data_file) 
            data_file.close()   

            slots = data[dokument][0][strana][0]
            self.tester = 0
            x = 9
            y = 9
            for slot in slots:
                self.label = DoubleClickLabel(self.workspace, self.dokument, self.strana, slot, self.textPlugin)
                print(self.workspace)
                print(self.dokument)
                print(self.strana)
                print(slot)
                self.label.setText(slot)        
                self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
                self.label.setLineWidth(1)
                self.label.setFocusPolicy(Qt.StrongFocus)
                self.grid.addWidget(self.label, x, y)
                self.tester += 1
                y += 1
                if y % 3 == 0:
                    y = 9
                    x += 1


                #dohvtimo stranicu i doajemo joj main widget
            self.mainWidget1 = self.iface.layout.itemAt(0).widget()
            self.mainWidget1.layout().addWidget(self.monotipTab)
            self.tab = self.mainWidget1.layout().itemAt(0).widget()      
            self.index = self.tab.currentIndex()  
            self.stranica = self.tab.widget(self.index)
            if self.stranica.layout().itemAt(2) is not None:
                self.stranica.layout().itemAt(2).widget().setParent(None)
            self.stranica.layout().addWidget(self.main, 0, 1, 0, 1)
                    

        
                        
                            
                         


    def addLabel(self, row, col, itemCount):

        self.page = self.main.layout().itemAt(1).widget()
        self.activeLayout = self.page.layout()
        
        
        

        self.label = QLabel()
           
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label.setLineWidth(1)
        

        if self.page.layout().itemAtPosition(row, col) is None:            
            self.label.setText("slot" + str(self.tester))     
            self.activeWidget.layout().addWidget(self.label, row, col,itemCount, 1)


            self.label.setFocusPolicy(Qt.StrongFocus)

            
            with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)


            data[self.dokument][0][self.strana][0]["slot" + str(self.tester)] = ""

            with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                json.dump(data, f, indent=2)
            
            self.thumbnail.pokreni()


    def addDown(self):
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        itemCount = 1
        if i > 1:
            self.activeWidget.layout().removeWidget(focused_widget)
            focused_widget.deleteLater()
            t = 0
            while t < i:                
                self.addLabel(row, col, itemCount)
                row += 1
                t +=1
                self.tester += 1
        else:
            row += 1
            self.tester += 1
            self.addLabel(row, col, itemCount)
            
    
    def addUp(self):
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        itemCount = 1
        row -= 1
        self.tester += 1
        self.addLabel(row, col, itemCount)
        
        

    def addRight(self):    
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        itemCount = int(self.grid.rowCount()) -10

        num = 0
        for rows in range(self.grid.rowCount()):
            if self.grid.itemAtPosition(rows, col) is not None:
                num += 1


        col += 1
        self.tester += 1
        self.addLabel(row, col, num)

    def addLeft(self):
        focused_widget = QApplication.focusWidget()
        self.activeWidget = self.main.layout().itemAt(1).widget()
        idx = self.activeWidget.layout().indexOf(focused_widget)
        row, col, i, x = self.grid.getItemPosition(idx)
        num = 0
        for rows in range(self.grid.rowCount()):
            if self.grid.itemAtPosition(rows, col) is not None:
                num += 1     
        col -= 1
        self.tester += 1
        self.addLabel(row, col, num)
    

    def deleteLabel(self):
       
        self.activeWidget = self.main.layout().itemAt(1).widget()
        focused_widget = QApplication.focusWidget()
        if focused_widget is not None:
            text = focused_widget.text()
            self.activeWidget.layout().removeWidget(focused_widget)
            focused_widget.deleteLater()
            self.tester -= 1
            with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)


            del data[self.dokument][0][self.strana][0][text]

            with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                json.dump(data, f, indent=2)
            self.thumbnail.pokreni()


            
            

        


        

        


                 


    



   
