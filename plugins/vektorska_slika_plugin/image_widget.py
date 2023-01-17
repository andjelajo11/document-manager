from PySide2.QtCore import Qt
from PySide2.QtGui import QTransform
from PySide2.QtSvg import QSvgRenderer, QGraphicsSvgItem
from PySide2.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsScene, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsEllipseItem, QWidget



class imageWidget(QWidget):
    def __init__(self, path, parent = None):
        super().__init__(parent)


        view = QGraphicsView()
        scene = QGraphicsScene()
        view.setScene(scene)

        # Create a QGraphicsEllipseItem
        renderer = QSvgRenderer(path)

# Create a QGraphicsSvgItem and set its renderer
        svg_item = QGraphicsSvgItem()
        svg_item.setSharedRenderer(renderer)

        # Add the QGraphicsSvgItem to the scene
        scene.addItem(svg_item)

        # Create buttons for the operations
        zoom_in_button = QPushButton("Zoom In")
        zoom_out_button = QPushButton("Zoom Out")
        rotate_left_button = QPushButton("Rotate Left")
        rotate_right_button = QPushButton("Rotate Right")
        flip_horizontal_button = QPushButton("Flip Horizontal")
        flip_vertical_button = QPushButton("Flip Vertical")

        # Connect the buttons to the corresponding operations
        zoom_in_button.clicked.connect(lambda: view.scale(1.2, 1.2))
        zoom_out_button.clicked.connect(lambda: view.scale(1 / 1.2, 1 / 1.2))
        rotate_left_button.clicked.connect(lambda: renderer.setViewBox(QTransform().rotate(-90)))
        rotate_right_button.clicked.connect(lambda: renderer.setViewBox(QTransform().rotate(90)))
        flip_horizontal_button.clicked.connect(lambda: renderer.setViewBox(QTransform().scale(-1, 1)))
        flip_vertical_button.clicked.connect(lambda: renderer.setViewBox(QTransform().scale(1, -1)))

        # Create a layout to hold the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(zoom_in_button)
        button_layout.addWidget(zoom_out_button)
        button_layout.addWidget(rotate_left_button)
        button_layout.addWidget(rotate_right_button)
        button_layout.addWidget(flip_horizontal_button)
        button_layout.addWidget(flip_vertical_button)

        # Create a layout to hold the view and buttons
        main_layout = QVBoxLayout()
        main_layout.addWidget(view)
        main_layout.addLayout(button_layout)     

        self.setLayout(main_layout)   