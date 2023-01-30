from PySide2 import QtWidgets


class MenuBar(QtWidgets.QMenuBar):

    def __init__(self):

        super().__init__()

    def _populate_menu_bar(self, actions_dict):
        file_menu = QtWidgets.QMenu("&File", self)
        plugins_menu = QtWidgets.QMenu("&Plugins", self)
        settings_menu = QtWidgets.QMenu("&Settings", self)
        help_menu = QtWidgets.QMenu("&Help", self)

        file_menu.addAction(actions_dict["quit"])
        plugins_menu.addAction(actions_dict["plugin_manager"])

        self.addMenu(file_menu)
        self.addMenu(plugins_menu)
        self.addMenu(help_menu)
        self.addMenu(settings_menu)


    def add_menu_action(self, menu_name, action):
        menues = self.findChildren(QtWidgets.QMenu)
        for menu in menues:
            if menu.title() == menu_name:
                menu.addAction(action)
                break

    def remove_menu_action(self, menu_name, action):
        menues = self.findChildren(QtWidgets.QMenu)
        for menu in menues:
            if menu.title() == menu_name:
                menu.removeAction(action)
                break
