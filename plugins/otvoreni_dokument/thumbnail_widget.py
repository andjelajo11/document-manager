from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QPixmap
from plugins.otvoreni_dokument.clickable_label import ClickableLabel
import json

class ThumbnailWidget(QtWidgets.QScrollArea):

    def __init__(self, text):
        super().__init__()
        dokument = text
        label_width = 200
        label_height = 150

        layout = QtWidgets.QVBoxLayout()


        self.glavni = QtWidgets.QWidget()
        

        

        

        with open("radni_prostor/dokumenti.json", "r") as f:
            json_data = f.read()

        data = json.loads(json_data)

        document = data[dokument]

        thumbnails = document[0].get("thumbnails", [])

        stranice = thumbnails[0]

        i = len(stranice)


        while i > 0:
            stranica = stranice["stranica"+ str(i)]
            i -= 1
        
            image1 = QPixmap(stranica)
            
            self.preview_label = ClickableLabel()
            self.preview_label.setScaledContents(True)
            self.preview_label.setFixedSize(label_width, label_height)
            scaled_image = image1.scaledToWidth(label_width)
            self.preview_label.setPixmap(scaled_image)
            layout.addWidget(self.preview_label)
        

        self.glavni.setLayout(layout)

        



        self.setWidget(self.glavni)

