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
        self.layout = QtWidgets.QGridLayout()

        self.overlay = QtWidgets.QLabel()
        self.overlay.setAlignment(QtCore.Qt.AlignCenter)
        self.overlay.setStyleSheet("background-color: rgba(128, 128, 128, 0.5); border: 2px solid white")
        self.newLayout = QtWidgets.QHBoxLayout()
        self.newLayout.setContentsMargins(0,0,0,0)
        self.glavni = QtWidgets.QWidget()
        
        with open("dokumenti/workspace1.json", "r") as f:
            json_data = f.read()

        data = json.loads(json_data)

        document = data[dokument]
        print(document[0]["thumbnails"][0].keys())

        thumbnails = document[0].get("thumbnails", [])
        id = 0
        print(thumbnails)
        if len(thumbnails) != 0:
            self.keys = document[0]["thumbnails"][0].keys()
            print(list(self.keys)[0])
            self.stranice = thumbnails[id]

            # Initialize the row and col variables
            row = 0
            col = 0

            for stranica in self.stranice:
                image1 = QPixmap(self.stranice[stranica])    
                self.preview_label = ClickableLabel()
                self.preview_label.setScaledContents(True)
                self.preview_label.mousePressEvent = self.labelClicked
                self.preview_label.setFixedSize(label_width, label_height)
                scaled_image = image1.scaledToWidth(label_width)
                self.preview_label.setPixmap(scaled_image)
                

                self.layout.addWidget(self.preview_label, row, col)
                row += 1


            self.glavni.setLayout(self.layout)

            self.setWidget(self.glavni)

            if id < len(thumbnails):
                id += 1


    def labelClicked(self, event):
        focused_widget = QtWidgets.QApplication.focusWidget()
        if focused_widget is not None:
            if event.button() == QtCore.Qt.LeftButton:                
                index = self.glavni.layout().indexOf(focused_widget)
                
                self.overlay.setText(list(self.keys)[index])
                focused_widget.setLayout(self.newLayout)
                self.newLayout.addWidget(self.overlay)
                self.overlay.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                parent_size = focused_widget.size()
                new_size = QtCore.QSize(parent_size.width(), parent_size.height())
                self.overlay.resize(new_size)