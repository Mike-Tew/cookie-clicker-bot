import os
import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWebEngineWidgets as qtwe
from PyQt5 import QtWidgets as qtw

import js
from BuildingWidget import Building


class MainWindow(qtw.QMainWindow):
    test_signal = qtc.pyqtSignal(object)
    store = {
        "Cursor": {"img": 1, "quantity": 0, "to_buy": 0},
        "Grandma": {"img": 1, "quantity": 0, "to_buy": 0},
        "Farm": {"img": 1, "quantity": 0, "to_buy": 0},
        "Mine": {"img": 1, "quantity": 0, "to_buy": 0},
        "Factory": {"img": 1, "quantity": 0, "to_buy": 0},
        "Bank": {"img": 1, "quantity": 0, "to_buy": 0},
        "Temple": {"img": 1, "quantity": 0, "to_buy": 0},
        "Wizard tower": {"img": 1, "quantity": 0, "to_buy": 0},
        "Shipment": {"img": 1, "quantity": 0, "to_buy": 0},
        "Alchemy lab": {"img": 1, "quantity": 0, "to_buy": 0},
        "Portal": {"img": 1, "quantity": 0, "to_buy": 0},
        "Time machine": {"img": 1, "quantity": 0, "to_buy": 0},
        "Antimatter condenser": {"img": 1, "quantity": 0, "to_buy": 0},
        "Prism": {"img": 1, "quantity": 0, "to_buy": 0},
        "Chancemaker": {"img": 1, "quantity": 0, "to_buy": 0},
        "Fractal engine": {"img": 1, "quantity": 0, "to_buy": 0},
        "Javascript console": {"img": 1, "quantity": 0, "to_buy": 0},
        "Idleverse": {"img": 1, "quantity": 0, "to_buy": 0},
    }
    purchase_list = []
    buy_upgrades = False

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cookie Clicker Bot")
        self.setFixedSize(1900, 1080)

        navigation = self.addToolBar("Navigation")
        style = self.style()

        self.urlbar = qtw.QLineEdit()
        navigation.addWidget(self.urlbar)
        self.go = navigation.addAction("Go")
        self.go.setIcon(style.standardIcon(style.SP_DialogOkButton))

        # Central Widget
        self.widget = qtw.QWidget()
        self.widget.setLayout(qtw.QHBoxLayout())
        self.setCentralWidget(self.widget)

        webview_layout = qtw.QVBoxLayout()
        self.widget.layout().addLayout(webview_layout, 4)
        building_layout = qtw.QVBoxLayout()
        self.widget.layout().addLayout(building_layout, 1)
        store_layout = qtw.QHBoxLayout()
        building_layout.addLayout(store_layout)
        store_layout.setContentsMargins(20, 20, 20, 20)

        self.webview = qtwe.QWebEngineView()
        webview_layout.addWidget(self.webview)
        self.webview.load(qtc.QUrl("https://orteil.dashnet.org/cookieclicker/"))
        self.webview.loadFinished.connect(self.loading_finished)

        self.toggle_clicker_btn = qtw.QPushButton("START", clicked=self.toggle_clicker)
        store_layout.layout().addWidget(self.toggle_clicker_btn)
        self.toggle_clicker_btn.setCheckable(True)

        self.upgrades_btn = qtw.QPushButton("UPGRADES")
        store_layout.layout().addWidget(self.upgrades_btn)
        self.upgrades_btn.setCheckable(True)

        self.auto_save_btn = qtw.QPushButton("AUTOSAVE", clicked=self.auto_save)
        store_layout.layout().addWidget(self.auto_save_btn)

        self.building_widgets = {
            building: Building(building, self.update_store) for building in self.store
        }
        for building in self.building_widgets.values():
            building_layout.layout().addWidget(building)
            self.test_signal.connect(building.test_slot)

        self.show()

    def save_file(self, save_data):
        print(save_data)
        with open("save.txt", "w") as open_file:
            open_file.write(save_data)

    def auto_save(self):
        self.webview.page().runJavaScript("Game.WriteSave(1)", self.save_file)

    def loading_finished(self):
        print("Finished loading webpage")
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(3000)

    def update_gui(self, var):
        for item in var:
            self.store[item]["quantity"] = var[item]
            quantity = self.store[item]["quantity"]
            to_buy = self.store[item]["to_buy"]
            if quantity >= to_buy:
                self.store[item]["to_buy"] = quantity

        self.test_signal.emit(self.store)
        self.purchase_list = [
            building
            for building in self.store
            if self.store[building]["to_buy"] > self.store[building]["quantity"]
        ]

        if self.upgrades_btn.isChecked():
            self.webview.page().runJavaScript(js.buy_upgrade)

        for building in self.purchase_list:
            self.webview.page().runJavaScript(
                js.buy_building.replace("<BUILDING>", building)
            )

    def refresh(self):
        self.webview.page().runJavaScript(js.store_items, self.update_gui)

    def update_store(self, name, increase):
        if increase:
            self.store[name]["to_buy"] += 1
        elif self.store[name]["to_buy"] > self.store[name]["quantity"]:
            self.store[name]["to_buy"] -= 1

        self.test_signal.emit(self.store)

    def toggle_clicker(self):
        if self.toggle_clicker_btn.isChecked():
            self.toggle_clicker_btn.setText("STOP")
            self.webview.page().runJavaScript(js.clicker)
        else:
            self.toggle_clicker_btn.setText("START")
            self.webview.page().runJavaScript(js.stop_clicker)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
