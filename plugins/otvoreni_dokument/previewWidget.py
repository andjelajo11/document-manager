from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QPen
from PySide2.QtWidgets import QWidget

class PreviewWidget(QWidget):

    def __init__(self, slots):
        super().__init__()
        self.slots = slots
        
        self.is_painted = False

    def paintEvent(self, event):
        if not self.is_painted:
            painter = QPainter(self)
            pen = QPen()
            pen.setWidth(2)
            pen.setColor(Qt.blue)
            pen.setStyle(Qt.SolidLine)
            painter.setPen(pen)
            self.x, self.y = 10, 10
            for _ in range(self.slots):
                painter.drawRect(self.x, self.y, 20, 20)
                self.x += 30
                self.y += 30
                print("works" + str(self.x) + " " + str(self.y))    
            self.is_painted = True

    def set_slots(self, slots):
        self.is_painted = False
        self.slots = slots
        self.update()