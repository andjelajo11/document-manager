from PySide2.QtWidgets import QLabel, QFileDialog
from PySide2.QtCore import Qt
import json



class DoubleClickLabel(QLabel):
    def __init__(self, workspace, dokument, stranica, slot):
        super().__init__()
        self.workspace = workspace
        self.dokument = dokument
        self.stranica = stranica
        self.slot = slot

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            path = ''
            dialog = QFileDialog()
            dialog.setDirectory(path)
            file_name, _ = dialog.getOpenFileName()

            with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)


            data[self.dokument][0][self.stranica][0][self.slot] = file_name

            with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                json.dump(data, f, indent=2)