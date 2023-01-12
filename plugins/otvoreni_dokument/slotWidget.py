from PySide2 import QtGui, QtCore
from PySide2 import QtWidgets

class FourSquaresWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setPalette(QtGui.QPalette(QtCore.Qt.white))
        self.pixmap = QtGui.QPixmap(self.size())
        self.pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(self.pixmap)
        painter.fillRect(10, 10, 20, 20, QtCore.Qt.black)
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)
