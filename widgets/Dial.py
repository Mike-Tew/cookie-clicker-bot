from PyQt5 import QtWidgets as qtw


class Dial(qtw.QWidget):
    def __init__(self, text):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel(text)
        self.layout().addWidget(self.label)

        self.dial = qtw.QDial()
        self.dial.setMinimum(10)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.layout().addWidget(self.dial)
