from plugin_framework.extension import Extension
from plugins.vektorska_slika_plugin.image_widget import imageWidget
import json





class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        # TODO: ukoliko u nekom plugin-u treba sacuvati referencu na iface, napraviti atribut
        


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["vektor_plugin"] = True
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)   
        self.activated = True
        print("Activated")

    def deactivate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)
        
        plugins["vektor_plugin"] = False

        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)
        self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
        print(type(self.monotipTab))
        tab_name = "Vector"
        tabs_with_same_name = []
        for i in range(self.monotipTab.count()):
            if self.monotipTab.tabText(i) == tab_name:
                tabs_with_same_name.append(i)
        for i in reversed(tabs_with_same_name):
            self.monotipTab.removeTab(i)



        self.activated = False
        print("Deactivated")
    
    def slotSelected(self, path):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)
        
        activated = plugins["vektor_plugin"]
        if activated == True:

            self.image_widget = imageWidget(path)
            self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
            self.monotipTab.vectorImage(self.image_widget)