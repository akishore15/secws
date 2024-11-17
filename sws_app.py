pip install pyinstaller
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineSettings

class SecureBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SWS")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, False)
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, False)
        self.browser.setUrl("https://brave.com")

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = SecureBrowser()
    browser.show()
    sys.exit(app.exec_())
