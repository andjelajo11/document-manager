from PySide2 import QtWidgets


class InfoWidget(QtWidgets.QDialog):
    # FIXME: postaviti relativnu putanju
    config_path = "configuration.json"
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QtWidgets.QVBoxLayout()
        self._name_label = QtWidgets.QLabel("Naziv Programa:")
        self._authors_label = QtWidgets.QLabel("Autori:")
        self._version_label = QtWidgets.QLabel("Verzija:")

        self._populate_layout()
        self.setLayout(self._layout)
        self.setWindowTitle("O Rukovaocu Multimedijalnim Dokumentima")
        self.resize(300, 128)


    def _populate_layout(self):
        # FIXME: procitati podatke iz konfiguracije i prepisati stringove (labele)
        self._layout.addWidget(self._name_label)
        self._layout.addWidget(QtWidgets.QLabel("Rukovalac Multimedijanim Dokumentima"))
        self._layout.addWidget(self._authors_label)
        self._layout.addWidget(QtWidgets.QLabel("Studenti Univerziteta Singidunum"))
        self._layout.addWidget(self._version_label)
        self._layout.addWidget(QtWidgets.QLabel("1.0.0"))
