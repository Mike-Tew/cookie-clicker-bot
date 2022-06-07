import js
from PyQt5 import QtCore as qtc


class Model(qtc.QObject):
    test_signal = qtc.pyqtSignal(object)
    buy_upgrades = False
    buy_buildings = False
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

    def __init__(self, webview):
        super().__init__()
        self.webview = webview

    def toggle_clicker(self, value):
        if value:
            self.webview.page().runJavaScript(js.clicker)
        else:
            self.webview.page().runJavaScript(js.stop_clicker)

    def click_speed(self, value):
        print(value)
