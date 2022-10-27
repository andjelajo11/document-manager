from plugin_framework.extension import Extension
from .widget import TextEdit

class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.widget = TextEdit(iface.central_widget)
        print("INIT TEST")

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        print("Activated")

    def deactivate(self):
        print("Deactivated")