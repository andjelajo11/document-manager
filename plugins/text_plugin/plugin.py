from plugins.text_plugin.textEditor import TextEditor
from plugin_framework.extension import Extension





class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        
        
        self.activated = True
        print("Activated")

    def deactivate(self):

        self.activated = False
        print("Deactivated")
    
    def slotSelected(self, path):
        self.textEditor = TextEditor(path)
        self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
        self.monotipTab.textEditor(self.textEditor)
