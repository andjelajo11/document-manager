from plugin_framework.extension import Extension

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        autentifikacija = open("./plugins/authentification_plugin/activation.txt", "r")

        autentifikacija = autentifikacija.read()

    
    
        if autentifikacija == "True":
            self.activated = True
        else:
            self.activated = False



    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        
        activation = open("./plugins/authentification_plugin/activation.txt", "w")

        activation.write("True")

        activation.close()

        self.activated = True
        

    def deactivate(self):
        activation = open("./plugins/authentification_plugin/activation.txt", "w")

        activation.write("False")

        activation.close()
        print("Deactivated")

        self.activated = False
    
    def aktiviran(self):
        if self.activated == True:
            return True
        else:
            return False
