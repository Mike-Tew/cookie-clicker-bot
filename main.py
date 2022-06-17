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

        self.view.clicker_btn.clicker_btn.toggled.connect(self.model.toggle_clicker)
        self.view.speed_dial.dial.valueChanged.connect(self.model.change_click_speed)
        self.view.upgrades_widget.upg_check.toggled.connect(self.model.auto_upg)
        self.view.upgrades_widget.build_check.toggled.connect(self.model.auto_build)
        self.view.upd_store.connect(self.model.update_store)
        for building in self.view.building_widgets.values():
            self.model.store_sig.connect(building.upd_lbl)

        self.show()
        self.statusBar().showMessage("Launching Cookie Clicker")

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

    def loading_finished(self):
        print("Finished loading webpage")
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(3000)

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


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
