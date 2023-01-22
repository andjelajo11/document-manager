from PySide2.QtCore import Qt
from PySide2.QtGui import QTransform, QPixmap, QPainter
from PySide2.QtWidgets import QLabel, QWidget, QAction, QToolBar, QVBoxLayout, QGraphicsView, QGraphicsScene




class imageWidget(QWidget):
    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.path = path
        self.view = QGraphicsView(self)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.pixmap = QPixmap(self.path)
        self.scene.clear()
        self.scene.addPixmap(self.pixmap)


        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create toolbar
        self.toolbar = QToolBar(self)
        self.layout.addWidget(self.toolbar)

        # Add actions to toolbar
        self.rotate_left_action = QAction("Rotate Left", self)
        self.rotate_left_action.triggered.connect(self.rotate_left)
        self.toolbar.addAction(self.rotate_left_action)

        self.rotate_right_action = QAction("Rotate Right", self)
        self.rotate_right_action.triggered.connect(self.rotate_right)
        self.toolbar.addAction(self.rotate_right_action)

        self.flip_horizontal_action = QAction("Flip Horizontal", self)
        self.flip_horizontal_action.triggered.connect(self.flip_horizontal)
        self.toolbar.addAction(self.flip_horizontal_action)

        self.flip_vertical_action = QAction("Flip Vertical", self)
        self.flip_vertical_action.triggered.connect(self.flip_vertical)
        self.toolbar.addAction(self.flip_vertical_action)

        self.zoom_in_action = QAction("Zoom In", self)
        self.zoom_in_action.triggered.connect(self.zoom_in)
        self.toolbar.addAction(self.zoom_in_action)

        self.zoom_out_action = QAction("Zoom Out", self)
        self.zoom_out_action.triggered.connect(self.zoom_out)
        self.toolbar.addAction(self.zoom_out_action)
        
        self.layout.addWidget(self.view)


    def load_image(self):
        self.scene.clear()
        self.scene.addPixmap(self.pixmap)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def rotate_left(self):
        self.rotate_image(-90)

    def rotate_right(self):
        self.rotate_image(90)

    def rotate_image(self, angle):
        self.pixmap = self.pixmap.transformed(QTransform().rotate(angle))
        self.load_image
        

    def flip_horizontal(self):
        self.flip_image(x = -1, y = 1)

    def flip_vertical(self):
        self.flip_image(x = 1, y = -1)

    def flip_image(self, x,y):
        self.pixmap = self.pixmap.transformed(QTransform().scale(x, y))
        self.load_image

    def zoom_in(self):
        self.pixmap = self.pixmap.scaled(self.pixmap.width() * 1.2, self.pixmap.height() * 1.2)
        self.load_image
        

    def zoom_out(self):
        self.pixmap = self.pixmap.scaled(self.pixmap.width() * 0.8, self.pixmap.height() * 0.8)
        self.load_image
        