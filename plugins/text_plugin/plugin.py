from PySide2 import QtWidgets
from PySide2 import QtGui
from plugins.text_plugin.textEditor import TextEditor
from monotip_handler.monotip_tab import MonotipTab
from plugin_framework.extension import Extension





class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.textEditor = TextEditor()


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
        self.monotipTab.textEditor(self.textEditor)
        
        self.activated = True
        print("Activated")

    def deactivate(self):

        self.activated = False
        print("Deactivated")
