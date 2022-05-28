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

    def __init__(self):
        super().__init__()

        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(3000)

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
        buttons_layout = qtw.QVBoxLayout()
        self.widget.layout().addLayout(buttons_layout, 1)

        self.webview = qtwe.QWebEngineView()
        webview_layout.addWidget(self.webview)
        self.webview.load(qtc.QUrl("https://orteil.dashnet.org/cookieclicker/"))

        self.text_input = qtw.QLineEdit()
        buttons_layout.layout().addWidget(self.text_input)
        run_js_btn = qtw.QPushButton("Run Javascript", clicked=self._run_js)
        buttons_layout.layout().addWidget(run_js_btn)
        start_clicker_btn = qtw.QPushButton("START", clicked=self._start_clicker)
        buttons_layout.layout().addWidget(start_clicker_btn)
        stop_clicker_btn = qtw.QPushButton("STOP", clicked=self._stop_clicker)
        buttons_layout.layout().addWidget(stop_clicker_btn)

        self.building_widgets = {
            building: Building(building, self.update_store) for building in self.store
        }
        for building in self.building_widgets.values():
            buttons_layout.layout().addWidget(building)
            self.test_signal.connect(building.test_slot)

        self.show()

    def update_gui(self, var):
        # try:
        for item in var:
            self.store[item]["quantity"] = var[item]
            if self.store[item]["quantity"] > self.store[item]["to_buy"]:
                self.store[item]["to_buy"] = self.store[item]["quantity"]
        # except:
        #     print("Can't find items")
        #     print(self.store)

        self.test_signal.emit(self.store)

    def refresh(self):
        self.webview.page().runJavaScript(js.store_items, self.update_gui)

    def update_store(self, name, increase):
        if increase:
            self.store[name]["to_buy"] += 1
        elif self.store[name]["to_buy"] > self.store[name]["quantity"]:
            self.store[name]["to_buy"] -= 1

        self.test_signal.emit(self.store)

    def _run_js(self):
        self.webview.page().runJavaScript(self.text_input.text())

    def _start_clicker(self):
        self.webview.page().runJavaScript(js.clicker)

    def _stop_clicker(self):
        self.webview.page().runJavaScript(js.stop_clicker)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
