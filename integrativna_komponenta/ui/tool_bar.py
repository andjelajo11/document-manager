from PySide2 import QtWidgets


class ToolBar(QtWidgets.QToolBar):

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
