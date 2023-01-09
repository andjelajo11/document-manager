from PySide2 import QtWidgets
from .plugin_manager_model import PluginManagerModel


class PluginManager(QtWidgets.QDialog):
    def __init__(self, parent=None, plugin_registry=None):
        super().__init__(parent)
        self.plugin_registry = plugin_registry
        # TODO: uvezati akcije za buttonbox
        # TODO: napraviti model podataka za plugin-ove u tabli
        self.activate_button = QtWidgets.QPushButton("Activate", self)
        self.deactivate_button = QtWidgets.QPushButton("Deactivate", self)
        self.install_button = QtWidgets.QPushButton("Install", self)
        self.uninstall_button = QtWidgets.QPushButton("Uninstall", self)
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Close, self)
        self.button_box.clicked.connect(lambda:self.close())
        self.table_view = QtWidgets.QTableView(self)
        self.widget_layout = QtWidgets.QGridLayout(self)
        self.plugin_model = None # model koji se ucitava za plugin-ve koji su importovani

        self.table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self._create_model()

        self._bind_actions()
        self._populate_layout()
        self.setLayout(self.widget_layout)

        self.setWindowTitle("Upravljanje dodacima")
        self.resize(600, 350)

    def _bind_actions(self):
        self.activate_button.clicked.connect(self.activate_plugin)
        self.deactivate_button.clicked.connect(self.deactivate_plugin)
        self.install_button.clicked.connect(self.install_plugin)
        self.uninstall_button.clicked.connect(self.uninstall_plugin)

    def _populate_layout(self):
        self.widget_layout.addWidget(self.activate_button, 0, 0)
        self.widget_layout.addWidget(self.deactivate_button, 0, 1)
        self.widget_layout.addWidget(self.install_button, 0, 2)
        self.widget_layout.addWidget(self.uninstall_button, 0, 3)
        self.widget_layout.addWidget(self.table_view, 1, 0, 1, 4)
        self.widget_layout.addWidget(self.button_box, 2, 0, 1, 4)

    # na osnovu dostupnih plugin-ova iz registry-ja napraviti model
    def _create_model(self):
        self.plugin_model = PluginManagerModel(None, self.plugin_registry._plugins)
        self.table_view.setModel(self.plugin_model)

    def list_plugins(self):
        for plugin in self.plugin_registry._plugins:
            print(plugin.name)

    def activate_plugin(self):
        # Pronaci trenutno selektovani element u tabeli
        selected_indexes = self.table_view.selectedIndexes()
        # TODO: ova lista moze biti prazna
        element = self.plugin_model.get_element(selected_indexes[0])
        self.plugin_registry.activate(element.plugin_specification.id)
        # TODO: azurirati prikaz

    def deactivate_plugin(self):
        # Pronaci trenutno selektovani element u tabeli
        selected_indexes = self.table_view.selectedIndexes()
        # TODO: ova lista moze biti prazna
        element = self.plugin_model.get_element(selected_indexes[0])
        self.plugin_registry.deactivate(element.plugin_specification.id)
        # TODO: azurirati prikaz

    def install_plugin(self):
        # Pronaci trenutno selektovani element u tabeli
        selected_indexes = self.table_view.selectedIndexes()
        # TODO: ova lista moze biti prazna
        element = self.plugin_model.get_element(selected_indexes[0])
        self.plugin_registry.install(element.plugin_specification.id)

    def uninstall_plugin(self):
        # Pronaci trenutno selektovani element u tabeli
        selected_indexes = self.table_view.selectedIndexes()
        # TODO: ova lista moze biti prazna
        element = self.plugin_model.get_element(selected_indexes[0])
        self.plugin_registry.uninstall(element.plugin_specification.id)
