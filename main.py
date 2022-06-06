import os
import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWebEngineWidgets as qtwe
from PyQt5 import QtWidgets as qtw

import js
from widgets.BuildingWidget import Building
from widgets.Clicker import Clicker
from widgets.Dial import Dial


class MainWindow(qtw.QMainWindow):
    test_signal = qtc.pyqtSignal(object)
    clicker_active = qtc.pyqtSignal(bool)
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

        self._create_menu_bar()

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

        # Store Widgets
        self.clicker_btn = Clicker(self.webview)
        store_layout.layout().addWidget(self.clicker_btn)

        self.custom_dial = Dial("Set Speed")
        store_layout.layout().addWidget(self.custom_dial)
        # self.speed_dial = qtw.QDial()
        # self.speed_dial.setWrapping(False)
        # self.speed_dial.setMinimum(10)
        # self.speed_dial.setMaximum(100)
        # self.speed_dial.setValue(30)
        # self.speed_dial.valueChanged.connect(self.val_change)
        # store_layout.layout().addWidget(self.speed_dial)

        self.upgrades_btn = qtw.QPushButton("UPGRADES")
        store_layout.layout().addWidget(self.upgrades_btn)
        self.upgrades_btn.setCheckable(True)

        # Building Widgets
        self.building_widgets = {
            building: Building(building, self.update_store) for building in self.store
        }
        for building in self.building_widgets.values():
            building_layout.layout().addWidget(building)
            self.test_signal.connect(building.test_slot)

        self.statusBar().showMessage("Launching Cookie Clicker")

        self.show()

    def val_change(self, value):
        print(value)

    def _create_menu_bar(self):
        menu_bar = qtw.QMenuBar(self)
        file_menu = menu_bar.addMenu("&File")
        options_menu = menu_bar.addMenu("&Options")
        options_menu.triggered.connect(self.test_checks)

        file_menu.addAction("Open", self.open_file)
        file_menu.addAction("&Exit", sys.exit)

        options_menu.addAction("Autosave")
        options_menu.addAction("1 Minute").setCheckable(True)
        options_menu.addAction("10 Minutes").setCheckable(True)
        options_menu.addAction("1 Hour").setCheckable(True)

        self.setMenuBar(menu_bar)

    def test_checks(self, action):
        print(action.isChecked(), action.text())

    def open_file(self):
        file_name = qtw.QFileDialog.getOpenFileName(self, "", "", "txt files (*.txt)")
        try:
            with open(file_name[0], "r", encoding="utf-8") as open_file:
                save_data = open_file.read()
            self.webview.page().runJavaScript(f"Game.LoadSave('{save_data}');")
            self.statusBar().showMessage("Save File Loaded.")
        except:
            self.statusBar().showMessage("Could not load file.")

    def auto_save(self):
        self.webview.page().runJavaScript("Game.WriteSave(1)", self.save_file)

    def save_file(self, save_data):
        with open("save.txt", "w", encoding="utf-8") as open_file:
            open_file.write(save_data)

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
