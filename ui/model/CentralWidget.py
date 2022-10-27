from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QHBoxLayout, QFileSystemModel, QTreeView


class CentralWidget(QWidget):

    layout = QHBoxLayout()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.treeView =  QTreeView()
        self.model = QFileSystemModel()
        
        self.model.setRootPath('C:\\')
        self.treeView.setModel(self.model)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        
        
        
        self.layout.addWidget(self.treeView)        
        self.treeView.clicked.connect(self.onClicked)

        

        # obavezno dati layout uvezujemo na widget (CentralWidget)
        self.setLayout(self.layout)
        

        
    def onClicked(self, index):
        
        path = self.sender().model().filePath(index)
        if ".txt" in path:
            text = open(path).read()
            if self.layout.itemAt(1) is not None:
                label = self.layout.itemAt(1).widget()
                label.setText(text)
    

    
        


