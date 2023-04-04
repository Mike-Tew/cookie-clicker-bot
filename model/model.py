from PyQt5 import QtCore as qtc

import js


class Model(qtc.QObject):
    auto_upg = False
    auto_build = False
    auto_golden = False
    auto_ticker = False
    auto_pop_wrinkler = False
    auto_spell_combo = False

    store_sig = qtc.pyqtSignal(object)
    store = {
        "Cursor": {"name": "Cursor", "quantity": 0, "to_buy": 0},
        "Grandma": {"name": "Grandma", "quantity": 0, "to_buy": 0},
        "Farm": {"name": "Farm", "quantity": 0, "to_buy": 0},
        "Mine": {"name": "Mine", "quantity": 0, "to_buy": 0},
        "Factory": {"name": "Factory", "quantity": 0, "to_buy": 0},
        "Bank": {"name": "Bank", "quantity": 0, "to_buy": 0},
        "Temple": {"name": "Temple", "quantity": 0, "to_buy": 0},
        "Wizard tower": {"name": "Wizard", "quantity": 0, "to_buy": 0},
        "Shipment": {"name": "Shipment", "quantity": 0, "to_buy": 0},
        "Alchemy lab": {"name": "Alchemy", "quantity": 0, "to_buy": 0},
        "Portal": {"name": "Portal", "quantity": 0, "to_buy": 0},
        "Time machine": {"name": "Time", "quantity": 0, "to_buy": 0},
        "Antimatter condenser": {"name": "Antimatter", "quantity": 0, "to_buy": 0},
        "Prism": {"name": "Prism", "quantity": 0, "to_buy": 0},
        "Chancemaker": {"name": "Chancemaker", "quantity": 0, "to_buy": 0},
        "Fractal engine": {"name": "Fractal", "quantity": 0, "to_buy": 0},
        "Javascript console": {"name": "Javascript", "quantity": 0, "to_buy": 0},
        "Idleverse": {"name": "Idleverse", "quantity": 0, "to_buy": 0},
        "Cortex baker": {"name": "Cortex", "quantity": 0, "to_buy": 0},
    }
    purchase_list = []

    def __init__(self, webview):
        super().__init__()
        self.webview = webview
        self.webview.loadFinished.connect(self.start_game_loop)
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.game_loop)

    def start_game_loop(self):
        self.timer.start(500)

    def game_loop(self):
        self.refresh()
        if self.auto_upg:
            self.webview.page().runJavaScript(js.buy_upgrade)
        if self.auto_build:
            self.buy_buildings()
        if self.auto_golden:
            self.webview.page().runJavaScript(js.click_golden)
        if self.auto_ticker:
            self.webview.page().runJavaScript(js.click_ticker)
        if self.auto_pop_wrinkler:
            self.webview.page().runJavaScript(js.pop_wrinkler)
        if self.auto_spell_combo:
            self.webview.page().runJavaScript(js.spell_combo)
            self.webview.page().runJavaScript(js.buy_and_sell)

    def update_gui(self):
        self.store_sig.emit(self.store)

    def toggle_clicker(self, value):
        if value:
            self.webview.page().runJavaScript(js.clicker)
        else:
            self.webview.page().runJavaScript(js.stop_clicker)

    def set_auto_upg(self, value):
        self.auto_upg = value

    def set_auto_build(self, value):
        self.auto_build = value

    def set_auto_golden(self, value):
        self.auto_golden = value

    def set_auto_ticker(self, value):
        self.auto_ticker = value

    def set_auto_pop_wrinkler(self, value):
        self.auto_pop_wrinkler = value

    def set_auto_spell_combo(self, value):
        self.auto_spell_combo = value

    def update_store(self, name, increase):
        if increase:
            self.store[name]["to_buy"] += 1
        elif self.store[name]["to_buy"] > self.store[name]["quantity"]:
            self.store[name]["to_buy"] -= 1

        self.refresh()

    def refresh(self):
        self.webview.page().runJavaScript(js.store_items, self.refresh_store)

    def refresh_store(self, current_store):
        for item in current_store:
            self.store[item]["quantity"] = current_store[item]
            quantity = self.store[item]["quantity"]
            to_buy = self.store[item]["to_buy"]
            if quantity >= to_buy:
                self.store[item]["to_buy"] = quantity

        self.update_gui()

    def buy_buildings(self):
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
