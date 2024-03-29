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

        self.golden_check = qtw.QCheckBox("Golden Cookies")
        self.layout().addWidget(self.golden_check)

        self.ticker_check = qtw.QCheckBox("Ticker")
        self.layout().addWidget(self.ticker_check)

        self.wrinklers_check = qtw.QCheckBox("Pop Wrinklers")
        self.layout().addWidget(self.wrinklers_check)

        self.spell_combo_check = qtw.QCheckBox("Godzamok Combo")
        self.layout().addWidget(self.spell_combo_check)
