import sys
from distutils import command

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWebEngineWidgets as qtwe
from PyQt5 import QtWidgets as qtw


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
        test_btn = qtw.QPushButton("TEST", clicked=self.print_text)
        buttons_layout.layout().addWidget(test_btn)

        self.show()

    def print_text(self):
        print("test")
        self.webview.page().runJavaScript("console.log(123);")
        self.webview.page().runJavaScript(self.text_input.text())



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
