from PyQt5 import QtWidgets as qtw


class Building(qtw.QWidget):
    def __init__(self, name, update_store):
        super().__init__()
        layout = qtw.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.name = name

        img_lbl = qtw.QLabel("IMG")
        layout.addWidget(img_lbl)
        name_lbl = qtw.QLabel(name)
        layout.addWidget(name_lbl)
        self.amount_lbl = qtw.QLabel("0/0")
        layout.addWidget(self.amount_lbl)

        down_btn = qtw.QPushButton("-")
        down_btn.clicked.connect(lambda: update_store(name, False))
        layout.addWidget(down_btn)

        up_btn = qtw.QPushButton("+")
        up_btn.clicked.connect(lambda: update_store(name, True))
        layout.addWidget(up_btn)

        self.setLayout(layout)

    def test_slot(self, store):
        quantity = store[self.name]["quantity"]
        to_buy = store[self.name]["to_buy"]
        formatted_lbl = f"{quantity}/{to_buy}"
        self.amount_lbl.setText(formatted_lbl)
