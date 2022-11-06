from PySide2.QtWidgets import QFileSystemModel, QTreeView




class TreeView(QTreeView):
        def __init__(self):
                super().__init__()
                self.model = QFileSystemModel()
                
                self.model.setRootPath('C:\\')
                self.setModel(self.model)
                self.hideColumn(1)
                self.hideColumn(2)
                self.hideColumn(3)         
