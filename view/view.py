import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWebEngineWidgets as qtwe
from PyQt5 import QtWidgets as qtw

from view.widgets.BuildingWidget import Building
from view.widgets.Clicker import Clicker
from view.widgets.Dial import Dial
from view.widgets.Upgrades import Upgrades


class View(qtw.QWidget):
    def __init__(self, webview, store):
        super().__init__()
        self.store = store
        self.setLayout(qtw.QHBoxLayout())

        webview_layout = qtw.QVBoxLayout()
        self.layout().addLayout(webview_layout, 4)
        building_layout = qtw.QVBoxLayout()
        self.layout().addLayout(building_layout, 1)
        store_layout = qtw.QHBoxLayout()
        building_layout.addLayout(store_layout)
        store_layout.setContentsMargins(20, 20, 20, 20)

        self.webview = webview
        webview_layout.addWidget(self.webview)
        self.webview.load(qtc.QUrl("https://orteil.dashnet.org/cookieclicker/"))
        self.webview.loadFinished.connect(self.loading_finished)

        self.clicker_btn = Clicker(self.webview)
        store_layout.layout().addWidget(self.clicker_btn)

        self.speed_dial = Dial()
        store_layout.layout().addWidget(self.speed_dial)

        self.upgrades_widget = Upgrades()
        store_layout.layout().addWidget(self.upgrades_widget)

        self.building_widgets = {
            building: Building(building, self.update_store) for building in self.store
        }
        for building in self.building_widgets.values():
            building_layout.layout().addWidget(building)
            # self.test_signal.connect(building.test_slot)

        # self.statusBar().showMessage("Launching Cookie Clicker")

    def loading_finished(self):
        pass

    def update_store(self):
        pass