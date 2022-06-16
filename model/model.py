import js
from PyQt5 import QtCore as qtc


class Model(qtc.QObject):
    click_speed = 5
    buy_upgrades = False
    buy_buildings = False
    store_sig = qtc.pyqtSignal(object)
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

    def __init__(self, webview):
        super().__init__()
        self.webview = webview

    def toggle_clicker(self, value):
        if value:
            self.webview.page().runJavaScript(
                js.clicker.replace("<CLICKS>", str(self.click_speed))
            )
        else:
            self.webview.page().runJavaScript(js.stop_clicker)

    def change_click_speed(self, value):
        self.click_speed = value

    def auto_upg(self, value):
        self.buy_upgrades = value

    def auto_build(self, value):
        self.buy_buildings = value

    def update_store(self, buy, name):
        print(buy, name)
        self.send_store()

    def send_store(self):
        self.store_sig.emit(self.store)
