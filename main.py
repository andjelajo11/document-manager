import sys, json
from PySide2 import QtWidgets, QtGui
from plugin_framework.plugin_registry import PluginRegistry
from ui.main_window import MainWindow


def _load_configuration(path="configuration.json"):
    with open(path, "r", encoding="utf-8") as fp:
        config = json.load(fp)
        return config

if __name__ == "__main__":
    config = _load_configuration()
    # TODO: u zavisnosti da li je authorization True ili False
    # aktivirati authorization plugin

    application = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow(config)
    # inicijalizacija registra svih plugin-onva
    plugin_registry = PluginRegistry("plugins", main_window)

    main_window.add_plugin_registry(plugin_registry)

    main_window.show()
    sys.exit(application.exec_())