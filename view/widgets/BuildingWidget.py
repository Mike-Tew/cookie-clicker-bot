from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw


class Building(qtw.QWidget):
    def __init__(self, name, lbl_name, upd_store):
        super().__init__()
        layout = qtw.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.name = name
        print(lbl_name)
        self.upd_store = upd_store

        img_lbl = qtw.QLabel("IMG")
        img_lbl.setPixmap(qtg.QPixmap(f"./assests/{lbl_name}.png").scaled(40, 40))
        layout.addWidget(img_lbl)
        name_lbl = qtw.QLabel(lbl_name)
        layout.addWidget(name_lbl)
        self.amount_lbl = qtw.QLabel("0/0")
        layout.addWidget(self.amount_lbl)

        down_btn = qtw.QPushButton("-")
        down_btn.clicked.connect(lambda: upd_store.emit(name, False))
        layout.addWidget(down_btn)

        up_btn = qtw.QPushButton("+")
        up_btn.clicked.connect(lambda: upd_store.emit(name, True))
        layout.addWidget(up_btn)

        self.setLayout(layout)

    def upd_lbl(self, store):
        quantity = store[self.name]["quantity"]
        to_buy = store[self.name]["to_buy"]
        formatted_lbl = f"{quantity}/{to_buy}"
        self.amount_lbl.setText(formatted_lbl)
