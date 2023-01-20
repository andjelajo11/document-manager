from PySide2 import QtWidgets, QtCore
from plugins.otvoreni_dokument.clickable_label import ClickableLabel
import json

class ThumbnailWidget(QtWidgets.QScrollArea):

    def __init__(self, dokument, workspace, stranica_plugin):
        super().__init__()
        self.stranica_plugin = stranica_plugin
        self.dokument = dokument
        self.workspace = workspace
        self.pokreni()


    def pokreni(self):
        label_width = 200
        label_height = 150
        
        self.layout = QtWidgets.QGridLayout()
        self.selected_label = None
        self.overlay = QtWidgets.QLabel()
        self.overlay.setAlignment(QtCore.Qt.AlignCenter)
        self.overlay.setStyleSheet("background-color: rgba(128, 128, 128, 0.5); border: 2px solid white")
        self.newLayout = QtWidgets.QHBoxLayout()
        self.newLayout.setContentsMargins(0,0,0,0)
        self.glavni = QtWidgets.QWidget()
        


        with open("dokumenti/" + self.workspace + ".json", "r") as f:
            json_data = f.read()

        data = json.loads(json_data)

        document = data[self.dokument]

        thumbnails = document[0].get("thumbnails", [])
        id = 0
        if len(thumbnails) != 0:
            self.keys = document[0]["thumbnails"][0].keys()
            self.stranice = thumbnails[id]

            row = 0
            col = 0

            for stranica in self.stranice:  
                self.preview_label = ClickableLabel(self.workspace, self.dokument, stranica)
                self.preview_label.setScaledContents(True)
                self.preview_label.mousePressEvent = self.labelClicked
                self.preview_label.setFixedSize(label_width, label_height)
                self.layout.addWidget(self.preview_label, row, col)
                row += 1


            self.glavni.setLayout(self.layout)

            self.setWidget(self.glavni)

            if id < len(thumbnails):
                id += 1


    def labelClicked(self, event):
        if self.overlay is None:
            self.overlay = QtWidgets.QLabel()
            self.overlay.setAlignment(QtCore.Qt.AlignCenter)
            self.overlay.setStyleSheet("background-color: rgba(128, 128, 128, 0.5); border: 2px solid white")
            focused_widget = QtWidgets.QApplication.focusWidget()
        elif self.newLayout is None:
            self.newLayout = QtWidgets.QHBoxLayout()
            self.newLayout.setContentsMargins(0,0,0,0)


        focused_widget = QtWidgets.QApplication.focusWidget()
        self.selected_label = focused_widget
        if focused_widget is not None:
            if event.button() == QtCore.Qt.LeftButton:                
                index = self.glavni.layout().indexOf(focused_widget)
                self.stranica = list(self.keys)[index]
                self.overlay.setText(list(self.keys)[index])
                focused_widget.setLayout(self.newLayout)
                self.newLayout.addWidget(self.overlay)
                self.overlay.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                parent_size = focused_widget.size()
                new_size = QtCore.QSize(parent_size.width(), parent_size.height())
                self.overlay.resize(new_size)
                self.stranica_plugin.onClicked(self.dokument, self.workspace, self.stranica)



    def down(self):
        if self.selected_label is None:
        # Select the first label if no label is currently selected
            current_index = 0
        else:
            current_index = self.glavni.layout().indexOf(self.selected_label)
        next_label = self.glavni.layout().itemAt(current_index + 1)
        if next_label is not None:
            self.selected_label = next_label.widget()
            self.overlay.setText(list(self.keys)[current_index + 1])
            self.selected_label.setLayout(self.newLayout)
            self.newLayout.addWidget(self.overlay)
            self.overlay.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            parent_size = self.selected_label.size()
            new_size = QtCore.QSize(parent_size.width(), parent_size.height())
            self.overlay.resize(new_size)

    def up(self):
        if self.selected_label is None:
            current_index = 0
        else:
            current_index = self.glavni.layout().indexOf(self.selected_label)
        if current_index != 0:
            next_label = self.glavni.layout().itemAt(current_index - 1)
            if next_label is not None:
                self.selected_label = next_label.widget()
                self.overlay.setText(list(self.keys)[current_index - 1])
                self.selected_label.setLayout(self.newLayout)
                self.newLayout.addWidget(self.overlay)
                self.overlay.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                parent_size = self.selected_label.size()
                new_size = QtCore.QSize(parent_size.width(), parent_size.height())
                self.overlay.resize(new_size)

    def top(self):
        current_index = 0
        next_label = self.glavni.layout().itemAt(current_index)
        if next_label is not None:
            self.selected_label = next_label.widget()
            self.overlay.setText(list(self.keys)[0])
            self.selected_label.setLayout(self.newLayout)
            self.newLayout.addWidget(self.overlay)
            self.overlay.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            parent_size = self.selected_label.size()
            new_size = QtCore.QSize(parent_size.width(), parent_size.height())
            self.overlay.resize(new_size)
    
    def bottom(self):
        current_index = self.glavni.layout().count() - 1

        # Select the last label in the layout
        last_label = self.glavni.layout().itemAt(current_index)
        if last_label is not None:
            self.selected_label = last_label.widget()
            self.overlay.setText(list(self.keys)[current_index])
            self.selected_label.setLayout(self.newLayout)
            self.newLayout.addWidget(self.overlay)
            self.overlay.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            parent_size = self.selected_label.size()
            new_size = QtCore.QSize(parent_size.width(), parent_size.height())
            self.overlay.resize(new_size)
    
    def delete(self):
        stranica = str(self.overlay.text())

        with open("dokumenti/" + self.workspace + ".json", "r") as f:
            data = json.load(f)
        del data[self.dokument][0][stranica]
        del data[self.dokument][0]["thumbnails"][0][stranica]

        with open("dokumenti/" + self.workspace + ".json", 'w') as f:
            json.dump(data, f, indent=2)
        

        if self.selected_label is not None:
            self.overlay.setParent(None)
            self.layout.removeWidget(self.selected_label)
            self.selected_label.setParent(None)
            self.pokreni() 
    

    def newPage(self):
        with open("dokumenti/" + self.workspace + ".json", "r") as f:
            data = json.load(f)
        brojStranica = len(data[self.dokument][0]["thumbnails"][0])


        data[self.dokument][0]['stranica' + str(brojStranica + 1)] = [{}]

        data[self.dokument][0]['thumbnails'][0]['stranica' + str(brojStranica + 1)] = "resources/icons/plaza.jpg"

        with open("dokumenti/" + self.workspace + ".json", 'w') as f:
            json.dump(data, f, indent=2)
        
        self.pokreni() 
        self.bottom()