import sys, json, atexit
from PySide2 import QtWidgets
from plugin_framework.plugin_registry import PluginRegistry
from integrativna_komponenta.main_window import MainWindow
from administracija.ui.login_dialog import LoginDialog
from administracija.controller.login_controller import LoginController



def reset_json_values():
    # Load the JSON file
    with open("plugin_framework/plugins.json", "r") as f:
        data = json.load(f)

    # Reset the values in the JSON data
    data = {"workspace_plugin": False, "celina_dokument": False, "otvoreni_dokument": False, "stranica_plugin": False}

    # Write the data back to the JSON file
    with open("plugin_framework/plugins.json", "w") as f:
        json.dump(data, f, indent=4)

    #brisanje konteksta za otvorene workspace kada se close app
    with open("rad_sa_celim_dokumentom/workspace_otvoreni.json", "r") as f:
        data = json.load(f)

    # Reset the values in the JSON data
    data = []

    # Write the data back to the JSON file
    with open("rad_sa_celim_dokumentom/workspace_otvoreni.json", "w") as f:
        json.dump(data, f, indent=4)


    #brisanje konteksta za otvorene dokumente kada se close app
    with open("rad_sa_celim_dokumentom/otvoreniDokumenti.json", "r") as f:
        data = json.load(f)

    # Reset the values in the JSON data
    data = []

    # Write the data back to the JSON file
    with open("rad_sa_celim_dokumentom/otvoreniDokumenti.json", "w") as f:
        json.dump(data, f, indent=4)

    #reset vrednosti konfiguracija
    with open("rad_sa_celim_dokumentom\configuration.json", "r") as f:
        data = json.load(f)

   
    data = {"alert_dialog": True}

    with open("rad_sa_celim_dokumentom\configuration.json", "w") as f:
        json.dump(data, f, indent=4)
   
        

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
    atexit.register(reset_json_values)
    sys.exit(application.exec_())


