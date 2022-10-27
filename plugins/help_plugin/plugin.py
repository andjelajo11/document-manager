from PySide2 import QtWidgets
from plugin_framework.extension import Extension
from .widgets.info_widget import InfoWidget


class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        # TODO: ukoliko u nekom plugin-u treba sacuvati referencu na iface, napraviti atribut
        self.widget = InfoWidget(iface)
        self.open_action = QtWidgets.QAction("&About")
        self.open_action.triggered.connect(self.open_help)
        print("Help plugin initialized!")

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.iface.add_menu_action("&Help", self.open_action)
        self.activated = True
        print("Activated")

    def deactivate(self):
        self.iface.remove_menu_action("&Help", self.open_action)
        self.activated = False
        print("Deactivated")

    def open_help(self):
        self.widget.show()