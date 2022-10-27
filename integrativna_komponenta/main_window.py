from PySide2 import QtWidgets, QtGui

from integrativna_komponenta.ui.centar_widget import CentralWidget
from integrativna_komponenta.ui.menu_bar import MenuBar
from plugin_framework.ui.plugin_manager import PluginManager
from integrativna_komponenta.ui.status_bar import StatusBar
from integrativna_komponenta.ui.tool_bar import ToolBar


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config

        self.actions_dict = {
            "quit": QtWidgets.QAction(QtGui.QIcon("resources/icons/document.png"), "&Quit", self),
            "plugin_manager": QtWidgets.QAction(QtGui.QIcon("resources/icons/puzzle.png"), "&Plugin Manager", self)
        }

        self.setWindowTitle(self.config["title"])
        self.setWindowIcon(QtGui.QIcon(self.config["icon"]))
        self.resize(self.config["window_size"]["width"], self.config["window_size"]["height"])

        # registar plugin-ova
        self.plugin_registry = None
        #meni
        self.menu_bar = MenuBar()
        #toolbar
        self.tool_bar = ToolBar("Toolbar")
        #statusbar
        self.status_bar = StatusBar()
        #centralwidget
        self.central_widget = CentralWidget()

        self._bind_actions()

        self.menu_bar._populate_menu_bar(self.actions_dict)

        self.setMenuBar(self.menu_bar)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(self.status_bar)
        self.setCentralWidget(self.central_widget)

    # *************************************** #
    # Metode koje ce koristiti drugi widget-i #
    # *************************************** #
    def set_status_message(self, message=""):
        self.status_bar.clearMessage()
        self.status_bar.showMessage(message)

    def add_menu(self, menu):
        self.menu_bar.addMenu(menu)

    def add_plugin_registry(self, registry):
        self.plugin_registry = registry

    def _bind_actions(self):
        self.actions_dict["quit"].setShortcut("Ctrl+Q")
        self.actions_dict["quit"].triggered.connect(self.close)
        self.actions_dict["plugin_manager"].triggered.connect(self.open_plugin_manager)

    # ********************************** #
    # Metode koje sluze za obradu akcija #
    # ********************************** #
    def open_plugin_manager(self):
        manager = PluginManager(self, self.plugin_registry)
        manager.show()

    def add_menu_action(self, menu_name, action):
        self.menu_bar.add_menu_action(menu_name, action)

    def remove_menu_action(self, menu_name, action):
        self.menu_bar.remove_menu_action(menu_name, action)