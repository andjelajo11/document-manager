from PySide2 import QtWidgets, QtCore

class DockWidget(QtWidgets.QDockWidget):

    clicked = QtCore.Signal(str, str)
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)