from PyQt5 import QtWidgets as qtw


class Building(qtw.QWidget):
    def __init__(self, name, update_store):
        super().__init__()
        layout = qtw.QHBoxLayout()

        img_lbl = qtw.QLabel("IMG")
        layout.addWidget(img_lbl)
        name_lbl = qtw.QLabel(name)
        layout.addWidget(name_lbl)
        amount_lbl = qtw.QLabel("100/150")
        layout.addWidget(amount_lbl)

        down_btn = qtw.QPushButton("-")
        down_btn.clicked.connect(lambda: update_store(name, False))
        layout.addWidget(down_btn)

        up_btn = qtw.QPushButton("+")
        up_btn.clicked.connect(lambda: update_store(name, True))
        layout.addWidget(up_btn)

        self.setLayout(layout)
