from PySide2.QtGui import QStandardItem




class StandardItem(QStandardItem):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.setEditable(False)
        self.setText(text)