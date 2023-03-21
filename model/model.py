from PyQt5 import QtCore as qtc

import js


class Model(qtc.QObject):
    click_speed = 5
    buy_upgrades = False
    buy_buildings = False
    store_sig = qtc.pyqtSignal(object)
    store = {
        "Cursor": {"img": 1, "quantity": 1, "to_buy": 0},
        "Grandma": {"img": 1, "quantity": 2, "to_buy": 0},
        "Farm": {"img": 1, "quantity": 0, "to_buy": 4},
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
        "Cortex baker": {"img": 1, "quantity": 0, "to_buy": 0},
    }
    purchase_list = []

    def __init__(self, webview):
        super().__init__()
        self.webview = webview
        self.webview.loadFinished.connect(self.start_game_loop)
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.purchase_buildings)

    def start_game_loop(self):
        self.timer.start(500)

    def update_gui_loop(self):
        self.store_sig.emit(self.store)

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

    def send_store(self):
        self.store_sig.emit(self.store)

    def update_store(self, name, increase):
        if increase:
            self.store[name]["to_buy"] += 1
        elif self.store[name]["to_buy"] > self.store[name]["quantity"]:
            self.store[name]["to_buy"] -= 1

        self.refresh()
        self.purchase_buildings()

    def refresh(self):
        self.webview.page().runJavaScript(js.store_items, self.refresh_store)

    def refresh_store(self, current_store):
        for item in current_store:
            self.store[item]["quantity"] = current_store[item]
            quantity = self.store[item]["quantity"]
            to_buy = self.store[item]["to_buy"]
            if quantity >= to_buy:
                self.store[item]["to_buy"] = quantity

        self.send_store()

    def purchase_buildings(self):
        self.purchase_list = [
            building
            for building in self.store
            if self.store[building]["to_buy"] > self.store[building]["quantity"]
        ]

        for building in self.purchase_list:
            self.webview.page().runJavaScript(
                js.buy_building.replace("<BUILDING>", building)
            )

        self.refresh()
        # self.timer.start(500)
