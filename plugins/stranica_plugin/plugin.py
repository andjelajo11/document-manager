from plugin_framework.extension import Extension
from PySide2.QtWidgets import QVBoxLayout, QLabel, QFrame, QToolBar, QAction, QGridLayout, QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from plugins.stranica_plugin.clickableLabel import DoubleClickLabel
from plugins.text_plugin.plugin import Plugin as textEditorPlugin
from plugins.vektorska_slika_plugin.plugin import Plugin as vectorPlugin
from plugins.rasterska_slika_plugin.plugin import Plugin as rasterPlugin
from plugins.video_plugin.plugin import Plugin as videoPlugin
from plugins.audio_plugin.plugin import Plugin as audioPlugin
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
        self.vectorPlugin = vectorPlugin(specification, iface)
        self.rasterPlugin = rasterPlugin(specification, iface)
        self.videoPlugin = videoPlugin(specification, iface)
        self.audioPlugin = audioPlugin(specification,iface)
        self.recnik = {}
        self.row = 10
        self.column = 10
        

    # FIXME: implementacija apstraktnih metoda
    def activate(self):


        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["stranica_plugin"] = True
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)   
    
        print("Activated")
        self.activated = True
      
    

    def deactivate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["stranica_plugin"] = False
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)   

        print("Deactivated")
        self.activated = False  
        self.iface.layout.itemAt(0).widget().setParent(None)


    def delete_tab(self,index):
        self.tabWidget.removeTab(index)

        
    def onClicked(self, dokument, workspace, strana, thumbnailWidget, treeWidget):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        activated = plugins["stranica_plugin"]

        if activated == True:
            self.dokument = dokument
            self.workspace = workspace
            self.strana = strana
            self.thumbnail = thumbnailWidget
            self.treeWidget = treeWidget
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
                self.new = QAction(QIcon("resources/icons/new-page.png"),"new",self.mainLayoutV)



                #kreiramo novi toolbar i njegove akcije, zatim ih postavljamo na main widget
                toolbar = QToolBar()              
                toolbar.addAction(self.left)
                toolbar.addAction(self.right)
                toolbar.addAction(self.up)
                toolbar.addAction(self.down)
                toolbar.addAction(self.delete)
                toolbar.addAction(self.new)

                self.down.triggered.connect(self.addDown)
                self.right.triggered.connect(self.addRight)
                self.left.triggered.connect(self.addLeft)
                self.up.triggered.connect(self.addUp)
                self.delete.triggered.connect(self.deleteLabel)
                self.new.triggered.connect(self.newPage)
                
                self.mainLayoutV.addWidget(toolbar)

                self.new.setEnabled(False)
                #kreiramo page widget, kojem dodlejujemo grid layout
                
                self.grid = QGridLayout()            
                self.page = QtWidgets.QWidget()
                self.mainLayoutV.addWidget(self.page)
                
                self.page.setLayout(self.grid)
                self.tester = 0
                
                #prebrojavamo koliko ima slotova u odabranoj stranici, zatim ih postavljamo na page widget preko grid layout-a

                with open('dokumenti/' + workspace + ".json", "r") as data_file:  
                    data = json.load(data_file) 
                data_file.close()   

                slots = data[dokument][0][strana][0]
                if len(slots) == 0:
                    self.new.setEnabled(True)

                x = 8
                y = 8
                colCount = 1
                rowCount = 1
                counter = 0
                for slot in slots:
                    counter += 1
                    if counter == len(slots) and counter % 4 != 0:
                        if len(slots) % 5 == 0:
                            colCount = 4
                        elif len(slots) % 6 == 0:
                            colCount = 3
                        elif len(slots) % 7 == 0:
                            colCount = 2
                    self.label = DoubleClickLabel(self.workspace, self.dokument, self.strana, slot, self.textPlugin, self.vectorPlugin, self.rasterPlugin, self.videoPlugin, self.thumbnail, self.audioPlugin)
                    self.label.setText(slot)        
                    self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
                    self.label.setLineWidth(1)
                    self.label.setFocusPolicy(Qt.StrongFocus)
                    self.grid.addWidget(self.label, x, y, rowCount, colCount)
                    y += 1
                    
                    
                    if y % 4 == 0:
                        y = 8
                        x += 1



                self.mainWidget1 = self.iface.layout.itemAt(0).widget()
                self.mainWidget1.layout().addWidget(self.monotipTab)
                self.tab = self.mainWidget1.layout().itemAt(0).widget()      
                self.index = self.tab.currentIndex()  
                self.stranica = self.tab.widget(self.index)
                if self.stranica.layout().itemAt(2) is not None:
                    self.stranica.layout().itemAt(2).widget().setParent(None)
                self.stranica.layout().addWidget(self.main, 0, 1, 0, 1)
                
                    

        
                        
                            
                         


    def addLabel(self, row, col, rowCount, columnCount):

        self.page = self.main.layout().itemAt(1).widget()
        self.activeLayout = self.page.layout()
        
        with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)

        slot_num = len(data[self.dokument][0][self.strana][0])
        



        data[self.dokument][0][self.strana][0]["slot" + str(slot_num + 1)] = ""
        

        

        slot = "slot" + str(slot_num + 1)
        self.label = DoubleClickLabel(self.workspace, self.dokument, self.strana, slot, self.textPlugin, self.vectorPlugin, self.rasterPlugin, self.videoPlugin, self.thumbnail, self.audioPlugin)
           
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label.setLineWidth(1)
        

        if self.page.layout().itemAtPosition(row, col) is None:            
            self.label.setText("slot" + str(slot_num + 1))     
            self.activeWidget.layout().addWidget(self.label, row, col,rowCount, columnCount)
            self.label.setFocusPolicy(Qt.StrongFocus)       
            
            with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                json.dump(data, f, indent=2)
            self.treeWidget.populate(self.dokument, self.workspace)
            self.thumbnail.pokreni()


    def addDown(self):
        focused_widget = QApplication.focusWidget()
        self.tester = 0
        if isinstance(focused_widget, DoubleClickLabel):
            self.activeWidget = self.main.layout().itemAt(1).widget()
            idx = self.activeWidget.layout().indexOf(focused_widget)
            row, col, i, x = self.grid.getItemPosition(idx)
            rowCount = 1
            if i > 1:
                self.activeWidget.layout().removeWidget(focused_widget)
                focused_widget.deleteLater()
                t = 0
                while t < i:       
                    self.addLabel(row, col, rowCount, columnCount = 1)
                    row += 1
                    t +=1
                    
            else:                
                columnCount = 0
                rowCount = 1
                for columns in range(self.grid.columnCount()):
                    if self.grid.itemAtPosition(row, columns) is not None:
                        if self.grid.itemAtPosition(row+1, columns) is None:
                            if self.grid.itemAtPosition(row+1, 8) is None:
                                col = 8
                                columnCount += 1
                            else:
                                col = 9
                                columnCount += 1
                row += 1
                self.addLabel(row, col, rowCount, columnCount)
        else:
            print("Not an instance of DoubleClickLabel")
            
    
    def addUp(self):
        columnCount = 1
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, DoubleClickLabel):
            self.activeWidget = self.main.layout().itemAt(1).widget()
            idx = self.activeWidget.layout().indexOf(focused_widget)
            row, col, i, x = self.grid.getItemPosition(idx)
            rowCount = 1
            row -= 1
            self.addLabel(row, col, rowCount, columnCount)
        
        
 
    def addRight(self):    
        focused_widget = QApplication.focusWidget()
        columnCount = 1
        if isinstance(focused_widget, DoubleClickLabel):
            self.activeWidget = self.main.layout().itemAt(1).widget()
            idx = self.activeWidget.layout().indexOf(focused_widget)
            row, col, rowCount, columnCount = self.grid.getItemPosition(idx)

            num = 0
            if self.grid.itemAtPosition(8, col + columnCount +1) is None:
                row = 8
                col = col + columnCount 
                rowCount = self.grid.rowCount() - 8
                columnCount = 1
                
            else:
                if self.grid.itemAtPosition(row, col+1) is None:
                    col +=1
                    rowCount = 1
            self.addLabel(row, col, rowCount, columnCount)

    def addLeft(self):
        columnCount = 1
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, DoubleClickLabel):
            self.activeWidget = self.main.layout().itemAt(1).widget()
            idx = self.activeWidget.layout().indexOf(focused_widget)
            row, col, i, x = self.grid.getItemPosition(idx)
            num = 0
            for rows in range(self.grid.rowCount()):
                if self.grid.itemAtPosition(rows, col) is not None:
                    if self.grid.itemAtPosition(rows, col-1) is None:
                        if self.grid.itemAtPosition(8, col-1) is None:
                            row = 8
                            num += 1
                        else:
                            row = 9
                            num += 1  
            col -= 1
            self.addLabel(row, col, num, columnCount)
    

    def deleteLabel(self):
       
        self.activeWidget = self.main.layout().itemAt(1).widget()
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, DoubleClickLabel):
            text = focused_widget.text()
            self.activeWidget.layout().removeWidget(focused_widget)
            focused_widget.deleteLater()
            with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)

            del data[self.dokument][0][self.strana][0][text]

            with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                json.dump(data, f, indent=2)
            self.thumbnail.pokreni()
            self.treeWidget.populate(self.dokument, self.workspace)
    
    def newPage(self):
        col = 8
        row = 8
        rowCount = 1
        colCount = 1
        slot = "slot1"
        self.label = DoubleClickLabel(self.workspace, self.dokument, self.strana, slot, self.textPlugin, self.vectorPlugin, self.rasterPlugin, self.videoPlugin, self.thumbnail, self.audioPlugin)
        self.label.setText(slot)        
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setFocusPolicy(Qt.StrongFocus)
        self.grid.addWidget(self.label, row, col, rowCount, colCount)

        with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)

        data[self.dokument][0][self.strana][0]["slot1"] = ""

        with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                json.dump(data, f, indent=2)
        
        self.new.setEnabled(False)
        self.treeWidget.populate(self.dokument, self.workspace)
        self.thumbnail.pokreni()