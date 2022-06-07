import os
import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWebEngineWidgets as qtwe
from PyQt5 import QtWidgets as qtw

import js
from model.model import Model
from view.view import View


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cookie Clicker Bot")
        self.setFixedSize(1900, 1080)
        self._create_menu_bar()

        webview = qtwe.QWebEngineView()
        self.model = Model(webview)
        self.view = View(webview, self.model.store)
        self.setCentralWidget(self.view)

        self.view.clicker_btn.click_sig.connect(self.model.toggle_clicker)
        self.view.speed_dial.dial.valueChanged.connect(self.model.click_speed)
        self.view.upgrades_widget.upg_check.toggled.connect(self.val_change)
        self.view.upgrades_widget.build_check.toggled.connect(self.val_change)

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

        # if self.upgrades_btn.isChecked():
        #     self.webview.page().runJavaScript(js.buy_upgrade)

        for building in self.purchase_list:
            self.webview.page().runJavaScript(
                js.buy_building.replace("<BUILDING>", building)
            )

    def refresh(self):
        print(self.buy_buildings, self.buy_upgrades)
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
