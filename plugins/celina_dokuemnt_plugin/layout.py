from PySide2 import QtWidgets


class TextEdit(QtWidgets.QWidget):
    widget_for = 123456789
    def __init__(self, parent):
        super().__init__(parent)
        self._layout = QtWidgets.QVBoxLayout()
        self.text_edit = QtWidgets.QTextEdit(self)
        self.tool_bar = QtWidgets.QToolBar("Naslov", self)

        self._layout.addWidget(self.tool_bar)
        self._layout.addWidget(self.text_edit)
        self._layout.stretch(1)
        
        self.setLayout(self._layout)
