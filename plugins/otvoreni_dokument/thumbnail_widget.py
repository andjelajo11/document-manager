from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QPixmap
from plugins.otvoreni_dokument.clickable_label import ClickableLabel

class ThumbnailWidget(QtWidgets.QScrollArea):

    def __init__(self):
        super().__init__()

        label_width = 200
        label_height = 150

        


        self.glavni = QtWidgets.QWidget()
        self.preview_label = ClickableLabel()
        self.preview_label.setScaledContents(True)

        

        self.preview_label.setFixedSize(label_width, label_height)
        
        image1 = QPixmap('resources/icons/plaza.jpg')
        scaled_image = image1.scaledToWidth(label_width)
        layout = QtWidgets.QVBoxLayout()

        self.glavni.setLayout(layout)

        self.preview_label.setPixmap(scaled_image)
        layout.addWidget(self.preview_label)



        self.setWidget(self.glavni)

