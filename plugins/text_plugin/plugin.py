from PySide2.QtWidgets import QLabel
from plugin_framework.extension import Extension
from ui.model.CentralWidget import CentralWidget

class Plugin(Extension):

    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """ 
        super().__init__(specification, iface)
        self.widget = QLabel()
        self.widget.setFixedWidth(500)

    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        CentralWidget.layout.addWidget(self.widget)   
        self.activated = True
        print("Activated")

    def deactivate(self):
        CentralWidget.layout.itemAt(1).widget().setParent(None)
        self.activated = False

        print("Deactivated")

