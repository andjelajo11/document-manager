import sys, json
from PySide2 import QtWidgets
from plugin_framework.plugin_registry import PluginRegistry
from integrativna_komponenta.main_window import MainWindow
from administracija.ui.login_dialog import LoginDialog
from administracija.controller.login_controller import LoginController


def _load_configuration(path="configuration.json"):
    with open(path, "r", encoding="utf-8") as fp:
        config = json.load(fp)
        return config

if __name__ == "__main__":
    config = _load_configuration()

    
    application = QtWidgets.QApplication(sys.argv)

    autentifikacija = open("./plugins/authentification_plugin/activation.txt", "r")

    autentifikacija = autentifikacija.read()

    
    
    if autentifikacija == "True":
        login_controller = LoginController()
        login = LoginDialog(controller=login_controller)
        result = login.exec()

        if result == 1:

            main_window = MainWindow(config, user=login.login_model)
            
            plugin_registry = PluginRegistry("plugins", main_window)

            main_window.add_plugin_registry(plugin_registry)

            main_window.show()
        else:
            sys.exit()
    # pokrenuti aplikaciju
    else:
        main_window = MainWindow(config, user=None)
        plugin_registry = PluginRegistry("plugins", main_window)

        main_window.add_plugin_registry(plugin_registry)

        main_window.show()
    sys.exit(application.exec_())
