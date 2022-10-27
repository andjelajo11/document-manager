from abc import ABC
from plugin_framework.plugin import Plugin

class Extension(Plugin, ABC):
    def __init__(self, plugin_specification, iface):
        self.plugin_specification = plugin_specification
        self.iface = iface
        self.activated = False

    @property
    def name(self):
        return self.plugin_specification.name + "-" + self.plugin_specification.version


    @name.setter
    def name(self, value):
        # TODO: proveri da li je value tipa str
        # ako nije mozda konvertovati
        # ili ga odbaciti kao rezultat (ne vrsiti setovanje)
        splitted = value.split("-")
        self.plugin_specification.name = splitted[0]
        self.plugin_specification.version = splitted[1]


    

    