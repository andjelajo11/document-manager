from PySide2.QtWidgets import QLabel, QTextEdit, QVBoxLayout


class Label(QLabel):
    layout = QVBoxLayout()
    def __init__(self):
        super().__init__()

    def mouseDoubleClickEvent(self, event):
        self.editText = QTextEdit()
        self.editText.setText(self.text())
        self.tab_widget = self.layout.itemAt(1).widget() 
        self.tab_widget.addTab(self.editText, "Dokument")
        # print("pos: ", event.pos())
        # do something