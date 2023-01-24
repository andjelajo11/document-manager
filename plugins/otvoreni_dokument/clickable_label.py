from PySide2 import QtWidgets, QtCore, QtGui
import json

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, workspace, dokument, stranica, parent=None):
        super().__init__(parent)
        print(workspace)
        print(dokument)
        print(stranica)

        self.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Plain)
        self.setLineWidth(1)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        with open("dokumenti/" + workspace + ".json", "r") as file:
            json_data = json.load(file)


        stranica1_data = json_data[dokument][0][stranica][0]


        slots_data = [stranica1_data[slot] for slot in stranica1_data]
        print(slots_data)
        # count the number of slots in stranica1 of dokument1
        num_slots = len(json_data[dokument][0][stranica][0])
        print(num_slots)
        pixmapWidth = 180
        pixmapHeight = 130
        pixmap = QtGui.QPixmap(pixmapWidth, pixmapHeight)
        pixmap.fill(QtCore.Qt.white)
        pen = QtGui.QPen()
        pen.setWidth(2)
        pen.setColor(QtCore.Qt.black)
        pen.setStyle(QtCore.Qt.SolidLine)
        


        painter = QtGui.QPainter(pixmap)
        painter.setPen(pen)
        
        painter.setFont(QtGui.QFont("Arial", 5))
        painter.begin(pixmap)
        width = 40
        height = 40
        x = 10
        y = 20
        for i in range(num_slots):  
            if ".txt" in slots_data[i]:     
                rect = QtCore.QRect(x, y, width, height)
                image = QtGui.QImage("resources/icons/txt.png")           
                painter.drawRect(x, y, width, height)
                painter.drawImage(rect, image)
                x += width
            elif ".png" in slots_data[i]:
                rect = QtCore.QRect(x, y, width, height)
                image = QtGui.QImage("resources/icons/jpg.png")           
                painter.drawRect(x, y, width, height)
                painter.drawImage(rect, image)
                x += width
            elif ".jpg" in slots_data[i]:
                rect = QtCore.QRect(x, y, width, height)
                image = QtGui.QImage("resources/icons/jpg.png")           
                painter.drawRect(x, y, width, height)
                painter.drawImage(rect, image)
                x += width
            elif ".mp4" in slots_data[i]:
                rect = QtCore.QRect(x, y, width, height)
                image = QtGui.QImage("resources/icons/mp4.png")           
                painter.drawRect(x, y, width, height)
                painter.drawImage(rect, image)
                x += width
            elif ".svg" in slots_data[i]:
                rect = QtCore.QRect(x, y, width, height)
                image = QtGui.QImage("resources/icons/svg.png")           
                painter.drawRect(x, y, width, height)
                painter.drawImage(rect, image)
                x += width
            elif ".mp3" in slots_data[i]:
                rect = QtCore.QRect(x, y, width, height)
                image = QtGui.QImage("resources/icons/mp3.png")           
                painter.drawRect(x, y, width, height)
                painter.drawImage(rect, image)
                x += width
            else:
                painter.drawRect(x, y, width, height)
                painter.drawText(x, y, width, height, QtCore.Qt.AlignCenter, "slot" + str(i+ 1))
                x += width
            if (i+1) %3 == 0: #if 6 squares have been drawn in a row
                x = 10
                y += height

        
        painter.end()

        self.setPixmap(pixmap)
