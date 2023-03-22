from PyQt5 import QtWidgets as qtw


class Upgrades(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel("Automate")
        self.layout().addWidget(self.label)

        self.upg_check = qtw.QCheckBox("Upgrades")
        self.layout().addWidget(self.upg_check)

        self.build_check = qtw.QCheckBox("Buildings")
        self.layout().addWidget(self.build_check)
