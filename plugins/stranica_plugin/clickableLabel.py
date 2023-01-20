from PySide2.QtWidgets import QLabel, QFileDialog
from PySide2.QtCore import Qt

import json



class DoubleClickLabel(QLabel):
    def __init__(self, workspace, dokument, stranica, slot, textPlugin, vectorPlugin):
        super().__init__()
        self.workspace = workspace
        self.dokument = dokument
        self.stranica = stranica
        self.slot = slot
        self.textPlugin = textPlugin
        self.vectorPLugin = vectorPlugin
        

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)
            text = data[self.dokument][0][self.stranica][0][self.slot]
            if text == "":

                path = ''
                dialog = QFileDialog()
                dialog.setDirectory(path)
                file_name, _ = dialog.getOpenFileName()

                


                data[self.dokument][0][self.stranica][0][self.slot] = file_name

                with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                    json.dump(data, f, indent=2)
                if ".txt" in file_name:
                    self.textPlugin.slotSelected(file_name)
                elif ".svg" in file_name:
                    self.vectorPLugin.slotSelected(file_name)
            else:
                if ".txt" in text:
                    self.textPlugin.slotSelected(text)
                elif ".svg" in text:
                    self.vectorPLugin.slotSelected(text)