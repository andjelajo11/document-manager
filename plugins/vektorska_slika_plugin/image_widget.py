from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QTransform, QPainter
from PySide2.QtSvg import QGraphicsSvgItem
from PySide2.QtWidgets import QDialog, QLabel,QGraphicsView, QGraphicsScene, QHBoxLayout, QVBoxLayout, QPushButton, QWidget




class imageWidget(QWidget):
    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.path = path
        self.view = QGraphicsView()
        scene = QGraphicsScene()
        self.view.setScene(scene)
        self.view.setRubberBandSelectionMode(Qt.IntersectsItemShape)

        self.svg_item = QGraphicsSvgItem(path)

        scene.addItem(self.svg_item)        


        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.fitInView(self.svg_item, Qt.KeepAspectRatio)
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.setRenderHint(QPainter.HighQualityAntialiasing)
        self.view.setRenderHint(QPainter.TextAntialiasing)
        self.view.setRenderHint(QPainter.NonCosmeticDefaultPen)
        self.view.setRenderHint(QPainter.Qt4CompatiblePainting)
        self.view.viewport().installEventFilter(self)
        self.view.resetTransform()
        self.zoom_in_button = QPushButton("Zoom In")
        self.zoom_out_button = QPushButton("Zoom Out")
        self.rotate_left_button = QPushButton("Rotate Left")
        self.rotate_right_button = QPushButton("Rotate Right")
        self.flip_horizontal_button = QPushButton("Flip Horizontal")
        self.flip_vertical_button = QPushButton("Flip Vertical")
        self.crop_button = QPushButton("Crop")
        self.clear_button = QPushButton("Clear")
        self.paint_button = QPushButton("Crtanje")

        self.zoom_in_button.clicked.connect(lambda: self.view.scale(1.2, 1.2))
        self.zoom_out_button.clicked.connect(lambda: self.view.scale(1 / 1.2, 1 / 1.2))
        self.rotate_left_button.clicked.connect(lambda: self.svg_item.setRotation(self.svg_item.rotation() - 90))
        self.rotate_right_button.clicked.connect(lambda: self.svg_item.setRotation(self.svg_item.rotation() + 90))
        self.flip_horizontal_button.clicked.connect(lambda: self.svg_item.setTransform(QTransform().scale(-1, 1), True))
        self.flip_vertical_button.clicked.connect(lambda: self.svg_item.setTransform(QTransform().scale(1, -1), True))
        self.crop_button.clicked.connect(self.crop_image)
        self.paint_button.clicked.connect(self.crtanje)
        self.clear_button.clicked.connect(self.reset_image)
        

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.zoom_in_button)
        self.button_layout.addWidget(self.zoom_out_button)
        self.button_layout.addWidget(self.paint_button)
        self.button_layout.addWidget(self.rotate_left_button)
        self.button_layout.addWidget(self.rotate_right_button)
        self.button_layout.addWidget(self.flip_horizontal_button)
        self.button_layout.addWidget(self.flip_vertical_button)
        self.button_layout.addWidget(self.crop_button)
        self.button_layout.addWidget(self.clear_button)
        

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.view)
        main_layout.addLayout(self.button_layout)     

        self.setLayout(main_layout)

    def crop_image(self):
        for i in reversed(range(self.button_layout.count())): 
            self.button_layout.itemAt(i).widget().setParent(None)

        crop_button = QPushButton("Crop")
        cancel_button = QPushButton("Cancel")

        crop_button.clicked.connect(self.do_crop)
        cancel_button.clicked.connect(self.cancel_crop)

        self.button_layout.addWidget(crop_button)
        self.button_layout.addWidget(cancel_button)

    def do_crop(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Error")
        label = QLabel("Ova aktivnost nije omogucena")
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(dialog.accept)
        layout = QVBoxLayout()
        layout.addWidget(label)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        layout.addLayout(button_layout)
        dialog.setLayout(layout)
        dialog.exec_()

    def crtanje(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Error")
        label = QLabel("Ova aktivnost nije omogucena")
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(dialog.accept)
        layout = QVBoxLayout()
        layout.addWidget(label)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        layout.addLayout(button_layout)
        dialog.setLayout(layout)
        dialog.exec_()

    def cancel_crop(self):
        for i in reversed(range(self.button_layout.count())): 
            self.button_layout.itemAt(i).widget().setParent(None)

        self.button_layout.addWidget(self.zoom_in_button)
        self.button_layout.addWidget(self.zoom_out_button)
        self.button_layout.addWidget(self.rotate_left_button)
        self.button_layout.addWidget(self.rotate_right_button)
        self.button_layout.addWidget(self.flip_horizontal_button)
        self.button_layout.addWidget(self.flip_vertical_button)
        self.button_layout.addWidget(self.crop_button)
        self.button_layout.addWidget(self.clear_button)
    
    def reset_image(self):
        self.svg_item.setTransform(QTransform())
        self.svg_item.setRotation(0)
        self.view.resetTransform()
        self.view.fitInView(self.svg_item, Qt.KeepAspectRatio)

    def eventFilter(self, object, event):
        if object == self.view.viewport() and event.type() == QEvent.MouseButtonDblClick:
            self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
            self.view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
            self.view.scale(1.2, 1.2)
            return True
        return False