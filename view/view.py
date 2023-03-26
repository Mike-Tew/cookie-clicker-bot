from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from view.widgets.BuildingWidget import Building
from view.widgets.Clicker import Clicker
from view.widgets.Upgrades import Upgrades


class View(qtw.QWidget):
    upd_store = qtc.pyqtSignal(str, bool)

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
        self.webview.load(qtc.QUrl("http://orteil.dashnet.org/cookieclicker/"))

        self.clicker_btn = Clicker(self.webview)
        store_layout.layout().addWidget(self.clicker_btn)

        self.upgrades_widget = Upgrades()
        store_layout.layout().addWidget(self.upgrades_widget)

        self.building_widgets = {
            building: Building(building, self.upd_store)
            for building in self.store
        }
        for building in self.building_widgets.values():
            building_layout.layout().addWidget(building)
            # self.upd_store.connect(building.test_slot)

    def update_store(self):
        pass
