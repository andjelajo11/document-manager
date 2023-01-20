import json
from PySide2 import QtWidgets
from PySide2 import QtGui
from plugin_framework.extension import Extension
from plugins.help_plugin.widgets.info_widget import InfoWidget



class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)

        self.widget = InfoWidget(iface)
        self.action_1 = QtWidgets.QAction("Delete Dialog ON") 
        self.action_1.setCheckable(True)
        self.action_1.setChecked(False)
        self.action_1.toggled.connect(self.config_bool)
    def activate(self):
        self.iface.add_menu_action("&Settings", self.action_1)  
        self.activated = True
        print("Activated")
        

    def deactivate(self):
        self.iface.remove_menu_action("&Settings", self.action_1)
        self.activated = False
        print("Deactivated")

    def dialog_action(self):
        self.widget.show()

    #proverava se da li je čekirana ili nije opcija za iskakanje alert dijaloga pre brisanja
    def config_bool(self):
        if self.action_1.isChecked() == True: #ako je čekirana u json configu se vrednost menja na false
            with open('rad_sa_celim_dokumentom\configuration.json') as data_file: 
                data = json.load(data_file)   
            data["alert_dialog"] = False
            with open('rad_sa_celim_dokumentom\configuration.json', 'w') as f:
                    json.dump(data, f, indent=2)
            self.action_1.setText("Delete Dialog OFF")
        else:               
            with open('rad_sa_celim_dokumentom\configuration.json') as data_file: 
                data = json.load(data_file)   
            data["alert_dialog"] = True #ako nije čekirana u json configu se vrednost menja na true
            with open('rad_sa_celim_dokumentom\configuration.json', 'w') as f:
                    json.dump(data, f, indent=2)
            self.action_1.setText("Delete Dialog ON")
