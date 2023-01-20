from PySide2 import QtWidgets
from PySide2 import QtGui
from plugin_framework.extension import Extension
from plugins.vektorska_slika_plugin.image_widget import imageWidget





class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        # TODO: ukoliko u nekom plugin-u treba sacuvati referencu na iface, napraviti atribut
        


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        
        self.activated = True
        print("Activated")

    def deactivate(self):
  
        self.activated = False
        print("Deactivated")
    
    def slotSelected(self, path):
        self.image_widget = imageWidget(path)
        self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
        self.monotipTab.vectorImage(self.image_widget)