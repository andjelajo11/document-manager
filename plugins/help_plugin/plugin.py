from PySide2 import QtWidgets
from plugin_framework.extension import Extension
from .widgets.info_widget import InfoWidget
from .widgets.online_help_widget import OnlineHelpWidget
from .widgets.ofline_help_widget import OflineHelpWidget




class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        # TODO: ukoliko u nekom plugin-u treba sacuvati referencu na iface, napraviti atribut
        #About
        self.widget = InfoWidget(iface)
        self.open_action_1 = QtWidgets.QAction("&About") #ikonica!
        self.open_action_1.triggered.connect(self.open_about)
        print("Help plugin initialized!")

        #Online uputstvo
        self.online_widget = OnlineHelpWidget(iface)
        self.open_action_2 = QtWidgets.QAction("&Online uputstvo") #ikonica!
        self.open_action_2.triggered.connect(self.open_help_online)

        #Dokumentovano uputstvo
        self.ofline_widget = OflineHelpWidget(iface)
        self.open_action_3 = QtWidgets.QAction("&Dokumentovano uputstvo") #ikonica!
        self.open_action_3.triggered.connect(self.open_help_ofline)



    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        self.iface.add_menu_action("&Help", self.open_action_3)
        self.iface.add_menu_action("&Help", self.open_action_2)
        self.iface.add_menu_action("&Help", self.open_action_1)
        
        self.activated = True
        print("Activated")

    def deactivate(self):
        self.iface.remove_menu_action("&Help", self.open_action_1)
        self.iface.remove_menu_action("&Help", self.open_action_2)
        self.iface.remove_menu_action("&Help", self.open_action_3)
        self.activated = False
        print("Deactivated")

    def open_about(self):
        self.widget.show()

    def open_help_online(self):
        self.online_widget.show()

    def open_help_ofline(self):
        self.ofline_widget.show()