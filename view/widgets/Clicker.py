from PyQt5 import QtWidgets as qtw


class Clicker(qtw.QWidget):
    def __init__(self, webview):
        super().__init__()
        self.webview = webview
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel("Clicker")
        self.layout().addWidget(self.label)

        self.clicker_btn = qtw.QPushButton("START", clicked=self.toggle_clicker)
        self.layout().addWidget(self.clicker_btn)
        self.clicker_btn.setCheckable(True)

    def toggle_clicker(self, is_checked):
        if is_checked:
            self.clicker_btn.setText("STOP")
        else:
            self.clicker_btn.setText("START")

