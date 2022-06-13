from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw


class Dial(qtw.QWidget):
    dial_sig = qtc.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel("Set Speed")
        self.layout().addWidget(self.label)

        self.dial = qtw.QDial()
        self.dial.setMinimum(1)
        self.dial.setMaximum(10)
        self.dial.setValue(5)
        self.layout().addWidget(self.dial)
