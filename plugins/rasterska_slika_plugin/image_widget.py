from PySide2.QtCore import Qt, QEvent, QPoint, QRect, QSize, QRectF
from PySide2.QtGui import QTransform, QPixmap, QPainter
from PySide2.QtWidgets import QLabel, QWidget, QAction, QToolBar, QVBoxLayout, QGraphicsView, QGraphicsScene, QRubberBand




class imageWidget(QWidget):
    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.path = path
        self.view = QGraphicsView(self)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)



        self.view.setSceneRect(QRectF(self.view.sceneRect()))
        self.view.setScene(self.scene)
        self.view.installEventFilter(self)
        self.view.viewport().installEventFilter(self)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.setRenderHint(QPainter.HighQualityAntialiasing)
        self.view.setRenderHint(QPainter.NonCosmeticDefaultPen)
        self.view.setRenderHint(QPainter.TextAntialiasing)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self.view)
        self.origin = QPoint()
        self.is_selecting = False
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


        self.crop = QAction("Crop", self)
        self.crop.triggered.connect(self.crop_image)
        self.toolbar.addAction(self.crop)

        self.cancel_button = QAction("Cancel", self)
        self.cancel_button.triggered.connect(self.cancel)
        self.toolbar.addAction(self.cancel_button)

        self.undo_button = QAction("Undo Crop", self)
        self.undo_button.triggered.connect(self.undo_crop)
        self.undo_button.setEnabled(True)
        self.toolbar.addAction(self.undo_button)
        
        
        self.layout.addWidget(self.view)
        self.image_history = []



    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress and source is self.view.viewport():
            self.origin = QPoint(event.pos())
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()
            self.is_selecting = True
            return True
        elif event.type() == QEvent.MouseMove and source is self.view.viewport() and self.is_selecting:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
            return True
        return super().eventFilter(source, event)

    def crop_image(self):
        # Check if an area is selected
        if not self.is_selecting:
            return
        # store current version of the image
        self.image_history.append(self.pixmap)
        self.undo_button.setEnabled(True)

        # Get the selected area as a QRect
        selected_area = self.rubberBand.geometry()

        # Convert the QRect to a QRectF
        selected_area_f = QRectF(selected_area)

        # Get the selected area in scene coordinates
        scene_selected_area = self.view.mapToScene(selected_area).boundingRect()

        # Create a new pixmap with the selected area
        self.pixmap = self.pixmap.copy(scene_selected_area.toRect())

        self.rubberBand.hide()
        self.origin = QPoint()
        self.is_selecting = False

        # Add the cropped pixmap to the scene
        self.scene.clear()
        self.scene.addPixmap(self.pixmap)

        # Fit the view to the scene
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
    
    def cancel(self):
        # Clear the rubber band and reset the origin point
        self.rubberBand.hide()
        self.origin = QPoint()
        self.is_selecting = False

    def undo_crop(self):
        # Check if there's a previous version of the image
        if len(self.image_history) > 0:
            # Get the previous version of the image
            previous_image = self.image_history.pop()
            # Clear the current image
            self.pixmap = previous_image
            self.scene.clear()
            self.scene.addPixmap(previous_image)
            self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
            # Disable the undo button if there's no previous version of the image
            if len(self.image_history) == 0:
                self.undo_button.setEnabled(False)

    def rotate_left(self):
        self.rotate_image(-90)

    def rotate_right(self):
        self.rotate_image(90)

    def rotate_image(self, angle):
        self.view.rotate(angle)

    def flip_horizontal(self):
        self.flip_image(horizontal=True)

    def flip_vertical(self):
        self.flip_image(vertical=True)

    def flip_image(self, horizontal=False, vertical=False):
        if horizontal:
            self.view.scale(-1, 1)
        if vertical:
            self.view.scale(1, -1)

    def zoom_in(self):
        self.view.scale(1.2, 1.2)

    def zoom_out(self):
        self.view.scale(0.8, 0.8)
        