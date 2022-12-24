from PySide2 import QtWidgets, QtCore

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Plain)
        self.setLineWidth(1)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def mousePressEvent(self, event):
        # Check if the left mouse button was clicked
        focused_widget = QtWidgets.QApplication.focusWidget()
        if focused_widget is not None:
            if event.button() == QtCore.Qt.LeftButton:                
                print("test")