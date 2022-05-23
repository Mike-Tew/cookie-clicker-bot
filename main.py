import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWebEngineWidgets as qtwe
from PyQt5 import QtWidgets as qtw

import js
from BuildingWidget import Building


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

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


        signal_ = qtc.pyqtSignal()
        btn = qtw.QPushButton("signal")
        btn.clicked.connect(self.test_signal)
        buttons_layout.layout().addWidget(btn)
        buttons_layout.layout().addWidget(Building("Cursor", self.test_signal))
        # buttons_layout.layout().addWidget(Building("Grandma"))
        # buttons_layout.layout().addWidget(Building("Farm"))
        # buttons_layout.layout().addWidget(Building("Mine"))
        # buttons_layout.layout().addWidget(Building("Factory"))

        self.show()

    def test_signal(self):
        print("Signalling", self.sender().text())

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
