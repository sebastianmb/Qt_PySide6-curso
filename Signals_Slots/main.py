#VERSION1: Setting everything up in the global scope
"""
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

#The slot :responds when  something  happens

def button_clicked():
    print("You clicked the button , didnt you!")

app = QApplication()
button = QPushButton("Press Me")


#You can wire a slot to the  signal  using  the syntax  below:
button.clicked.connect(button_clicked)

button.show()

app.exec()
"""

#VERSION
