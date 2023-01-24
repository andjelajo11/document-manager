from PySide2.QtWidgets import QLabel, QFileDialog
from PySide2.QtCore import Qt

import json



class DoubleClickLabel(QLabel):
    def __init__(self, workspace, dokument, stranica, slot, textPlugin, vectorPlugin, rasterPlugin, videoPlugin, thumbnail):
        super().__init__()
        self.workspace = workspace
        self.dokument = dokument
        self.stranica = stranica
        self.slot = slot
        self.textPlugin = textPlugin
        self.vectorPLugin = vectorPlugin
        self.rasterPlugin = rasterPlugin
        self.videoPlugin = videoPlugin
        self.thumbnail = thumbnail
        

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("slot double clicked")
            with open("dokumenti/" + self.workspace + ".json", "r") as f:
                data = json.load(f)
            text = data[self.dokument][0][self.stranica][0][self.slot]
            if text == "":
                print("tekst je prazan")
                path = ''
                dialog = QFileDialog()
                dialog.setDirectory(path)
                file_name, _ = dialog.getOpenFileName()

                    


                data[self.dokument][0][self.stranica][0][self.slot] = file_name
                

                with open("dokumenti/" + self.workspace + ".json", 'w') as f:
                    json.dump(data, f, indent=2)
                
                self.thumbnail.pokreni()
                if ".txt" in file_name:
                    self.textPlugin.slotSelected(file_name)
                elif ".svg" in file_name:
                    self.vectorPLugin.slotSelected(file_name)
                elif ".png" or ".jpg" in file_name:
                    self.rasterPlugin.slotSelected(file_name)
                elif ".mp" in file_name:
                    print("video")
                    self.videoPlugin.slotSelected(file_name)
            else:
                print("text nije prazan")
                print(text)
                if ".txt" in text:
                    self.textPlugin.slotSelected(text)
                elif ".svg" in text:
                    self.vectorPLugin.slotSelected(text)
                elif ".png" in text:
                    self.rasterPlugin.slotSelected(text)
                elif ".jpg" in text:
                    self.rasterPlugin.slotSelected(text)
                elif ".mp4" in text:
                    print("video1")
                    self.videoPlugin.slotSelected(text)
                    
