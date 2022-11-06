from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt


class PluginManagerModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, plugins=[]):
        super().__init__(parent)
        self.plugins = plugins

    def get_element(self, index):
        # print(index.row(), index.column())
        if (index.isValid()):
            # element = index.internalPointer() # dobavljanje vrednosti na indeksu
            element = self.plugins[index.row()]
            if element:
                return element
        return self.plugins

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.plugins)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 5

    def data(self, index, role=Qt.DisplayRole):
        element = self.get_element(index)
        print(element)
        if index.column() == 0 and role == Qt.DisplayRole:
            return element.plugin_specification.id
        elif index.column() == 1 and role == Qt.DisplayRole:
            return element.name # pristup property-ju
        elif index.column() == 2 and role == Qt.DisplayRole:
            return element.plugin_specification.description
        elif index.column() == 3 and role == Qt.DisplayRole:
            return element.plugin_specification.core_version
        elif index.column() == 4 and role == Qt.DecorationRole:
            # TODO: prikazati odgovarajucu ikonicu za stanje plugin-a
            if element.activated:
                return QtGui.QIcon("resources/icons/tick-octagon.png")
            else:
                return QtGui.QIcon("resources/icons/cross-script.png")

    def parent(self, child_index):
        return QtCore.QModelIndex() # nevalidan indeks

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if section == 0 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "ID"
        elif section == 1 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Naziv"
        elif section == 2 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Opis"
        elif section == 3 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Verzija aplikacije"
        elif section == 4 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Status"