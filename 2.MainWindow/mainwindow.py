from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app=app #declare an app member
        self.setWindowTitle("Custom MainWindow")

        #Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")