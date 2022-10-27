from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import  QLabel
from PySide2 import QtCore

from .plugin_manager import PluginManager


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config

        self.setWindowTitle(self.config["title"])
        self.setWindowIcon(QtGui.QIcon(self.config["icon"]))
        self.resize(self.config["window_size"]["width"], self.config["window_size"]["height"])

        # self.slika = QtGui.QPictureIO("resources/icons/multimedia.png")
        # self.slika_layout = QtWidgets.QLayout(self.slika)

        #self.central_widget.show
        # registar plugin-ova
        self.plugin_registry = None
        #meni
        self.menu_bar = QtWidgets.QMenuBar(self)
        #toolbar
        self.tool_bar = QtWidgets.QToolBar("Toolbar",self)
        #statusbar
        self.status_bar = QtWidgets.QStatusBar(self)
        #centralwidget
        self.central_widget = QtWidgets.QTabWidget(self)

        self.tab0=QtWidgets.QTextEdit()

        self.tab1 = QtWidgets.QTextEdit()

        #self.label = QLabel("Text editor je aktiviran!")

        

        self.actions_dict = {
            # FIXME: ispraviti ikonicu na X
            "quit": QtWidgets.QAction(QtGui.QIcon("resources/icons/document.png"), "&Quit", self),
            "plugin_manager": QtWidgets.QAction(QtGui.QIcon("resources/icons/puzzle.png"), "&Plugin Manager", self)
            # TODO: dodati i ostale akcije za help i za npr. osnovno za dokument
            # dodati open...
        }

        self._bind_actions()

        self._populate_menu_bar()

        self.setMenuBar(self.menu_bar)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(self.status_bar)
        self.setCentralWidget(self.central_widget)
        self.central_widget.addTab(self.tab0, "Pocetna prozor")
        # self.central_widget.setLayout(self.slika_layout)
        self.central_widget.setTabsClosable(True)
        self.central_widget.tabCloseRequested.connect(self.delete_tab)
        

        
    def _populate_menu_bar(self):
        file_menu = QtWidgets.QMenu("&File", self.menu_bar)
        plugins_menu = QtWidgets.QMenu("&Plugins", self.menu_bar)
        help_menu = QtWidgets.QMenu("&Help", self.menu_bar)

        file_menu.addAction(self.actions_dict["quit"])
        plugins_menu.addAction(self.actions_dict["plugin_manager"])

        self.menu_bar.addMenu(file_menu)
        self.menu_bar.addMenu(plugins_menu)
        self.menu_bar.addMenu(help_menu)

    def _bind_actions(self):
        self.actions_dict["quit"].setShortcut("Ctrl+Q")
        self.actions_dict["quit"].triggered.connect(self.close)
        self.actions_dict["plugin_manager"].triggered.connect(self.open_plugin_manager)

    def add_plugin_registry(self, registry):
        self.plugin_registry = registry

    # ********************************** #
    # Metode koje sluze za obradu akcija #
    # ********************************** #
    def open_plugin_manager(self):
        manager = PluginManager(self, self.plugin_registry)
        manager.show()

    # *************************************** #
    # Metode koje ce koristiti drugi widget-i #
    # *************************************** #
    # TODO: proveriti koje metode bi jos bile od znacaja
    def set_status_message(self, message=""):
        self.status_bar.clearMessage()
        self.status_bar.showMessage(message)

    def add_menu_action(self, menu_name, action):
        menues = self.menu_bar.findChildren(QtWidgets.QMenu)
        for menu in menues:
            if menu.title() == menu_name:
                menu.addAction(action)
                break
    
    def remove_menu_action(self, menu_name, action):
        menues = self.menu_bar.findChildren(QtWidgets.QMenu)
        for menu in menues:
            if menu.title() == menu_name:
                menu.removeAction(action)
                break

    def add_menu(self, menu):
        self.menu_bar.addMenu(menu)

    def add_widget(self):
        #self.set(self.label) 
        #self.dock = QtWidgets.QDockWidget(self)
        #self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.dock)
        self.central_widget.addTab(self.tab1, "text editor" )
        self.tab1.insertPlainText("Text editor je aktiviran!")
        
    def delete_tab(self,index):
        self.central_widget.removeTab(index)
    