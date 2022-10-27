from plugin_framework.extension import Extension
from .widgets.widget import TextEdit
from .widgets.tekst_dialog import TekstPoruka

from PySide2 import QtWidgets

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)

        self.widget = TekstPoruka(iface)
        #self.show_dialog = QtWidgets.QAction("&About")
        #self.open_action.triggered.connect(self.open_dialog)
        print("Help plugin initialized!")

        # super().__init__(specification, iface)
        # self.widget = TextEdit(iface.central_widget)
        # print("INIT TEST")

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")
        self.iface.add_widget()
        self.activated = True
        

    def deactivate(self):
        print("Deactivated")

    def open_dialog(self):
        self.widget.show()