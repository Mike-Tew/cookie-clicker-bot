from PyQt5 import QtWidgets as qtw


class Upgrades(qtw.QWidget):
    def __init__(self, text, upg_val, build_val):
        super().__init__()
        self.upg_val = upg_val
        self.build_val = build_val
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel(text)
        self.layout().addWidget(self.label)

        self.upg_check = qtw.QCheckBox("Upgrades")
        self.upg_check.toggled.connect(self.update_upg_val)
        self.layout().addWidget(self.upg_check)

        self.build_check = qtw.QCheckBox("Buildings")
        self.build_check.toggled.connect(self.update_build_val)
        self.layout().addWidget(self.build_check)

    def update_upg_val(self, val):
        print(val)
        self.upg_val = val

    def update_build_val(self, val):
        print(val)
        self.build_val = val
