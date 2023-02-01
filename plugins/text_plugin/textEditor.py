from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QKeySequence, QFont, QIcon, QFontDatabase

class TextEditor(QtWidgets.QWidget):
    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.text_edit = QtWidgets.QTextEdit(self)
        self.path = path
        text = open(path).read()
        self.text_edit.setText(text)
        self.text_edit.setFontPointSize(12)
        self.toolbar = QtWidgets.QToolBar()
        

        self.save_action = QtWidgets.QAction(QIcon("resources/icons/text-save.png"), "Save", self)
        self.save_action.setShortcut(QKeySequence.Save)
        self.toolbar.addAction(self.save_action)


        self.bold_action = QtWidgets.QAction(QIcon("resources/icons/text-bold.png"),"Bold", self)
        self.bold_action.setCheckable(True)
        self.toolbar.addAction(self.bold_action)


        self.italic_action = QtWidgets.QAction(QIcon("resources/icons/text-italic.png"),"Italic", self)
        self.italic_action.setCheckable(True)
        self.toolbar.addAction(self.italic_action)


        self.bold_action.toggled.connect(self.set_bold)
        self.italic_action.toggled.connect(self.set_italic)

        self.font_size_dropdown = QtWidgets.QComboBox(self)

        self.font_size_dropdown.addItems(["8", "10", "12", "14", "16", "18", "20"])


        self.font_size_dropdown.setCurrentIndex(2)
        self.toolbar.addWidget(self.font_size_dropdown)


        font_db = QFontDatabase()
        fonts = font_db.families()

        self.fontBox = QtWidgets.QComboBox()
        self.fontBox.addItems(fonts)

        self.font_action = QtWidgets.QAction("Font", self)
        self.toolbar.addWidget(self.fontBox)
        
        self.mainLayout.addWidget(self.toolbar)
        self.mainLayout.addWidget(self.text_edit)
        self.font_size_dropdown.currentIndexChanged.connect(self.selectFontSize)
        self.fontBox.currentIndexChanged.connect(self.selectFont)



        self.left_align_action = QtWidgets.QAction(QIcon("resources/icons/text-align-left.png"), "Left Align", self)
        self.left_align_action.setCheckable(True)
        self.toolbar.addAction(self.left_align_action)


        self.center_align_action = QtWidgets.QAction(QIcon("resources/icons/text-align-center.png"), "Center Align", self)
        self.center_align_action.setCheckable(True)
        self.toolbar.addAction(self.center_align_action)

        self.right_align_action = QtWidgets.QAction(QIcon("resources/icons/text-align-right.png"), "Right Align", self)
        self.right_align_action.setCheckable(True)
        self.toolbar.addAction(self.right_align_action)

        self.undo_action = QtWidgets.QAction(QIcon("resources/icons/text-undo.png"), "Undo", self)
        self.undo_action.setShortcut(QKeySequence.Undo)
        self.undo_action.triggered.connect(self.text_edit.undo)
        self.toolbar.addAction(self.undo_action)


        self.redo_action = QtWidgets.QAction(QIcon("resources/icons/text-redo.png"), "Undo", self)
        self.redo_action.setShortcut(QKeySequence.Redo)
        self.redo_action.triggered.connect(self.text_edit.redo)
        self.toolbar.addAction(self.redo_action)



        self.align_group = QtWidgets.QActionGroup(self)
        self.left_align_action.setCheckable(True)
        self.align_group.addAction(self.left_align_action)
        self.right_align_action.setCheckable(True)
        self.align_group.addAction(self.right_align_action)
        self.center_align_action.setCheckable(True)
        self.align_group.addAction(self.center_align_action)


        self.left_align_action.triggered.connect(self.set_left_align)
        self.right_align_action.triggered.connect(self.set_right_align)
        self.center_align_action.triggered.connect(self.set_center_align)
        self.save_action.triggered.connect(self.save_file)

    def set_bold(self, checked):
        if checked:
            self.text_edit.setFontWeight(QFont.Bold)
        else:
            self.text_edit.setFontWeight(QFont.Normal)

    def set_italic(self, checked):
        self.text_edit.setFontItalic(checked)

    def selectFont(self):
        selected_font = self.fontBox.currentText()
        self.text_edit.setFontFamily(selected_font)
    
    def selectFontSize(self):
        selected_size = int(self.font_size_dropdown.currentText())
        self.text_edit.setFontPointSize(selected_size)


    def set_left_align(self):
        self.text_edit.setAlignment(QtCore.Qt.AlignLeft)

    def set_right_align(self):
        self.text_edit.setAlignment(QtCore.Qt.AlignRight)

    def set_center_align(self):
        self.text_edit.setAlignment(QtCore.Qt.AlignCenter)

    def save_file(self):
        text = self.text_edit.toPlainText()
        with open(self.path, "w") as f:
            f.write(text)

    def undo(self):
        self.text_edit.undo()
    
    def redo(self):
        self.text_edit.redo()