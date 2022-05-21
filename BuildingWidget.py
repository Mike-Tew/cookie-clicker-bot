from PyQt5 import QtWidgets as qtw


class Building(qtw.QWidget):
    def __init__(self):
        super().__init__()

        layout = qtw.QHBoxLayout()

        img_lbl = qtw.QLabel("IMG")
        layout.addWidget(img_lbl)
        name_lbl = qtw.QLabel("CURSOR")
        layout.addWidget(name_lbl)
        amount_lbl = qtw.QLabel("100/150")
        layout.addWidget(amount_lbl)

        down_btn = qtw.QPushButton("-")
        layout.addWidget(down_btn)
        up_btn = qtw.QPushButton("+")
        layout.addWidget(up_btn)

        self.setLayout(layout)
