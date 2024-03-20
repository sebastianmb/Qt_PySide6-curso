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

#VERSION2: SIGNALS SENDIG VALUES, CAPTURE VALUES IN SLOTS

"""
from PySide6.QtWidgets import QApplication,QPushButton

#The splot_ responds when something happens
def button_clicked(data):
    print("You clicked the button , didnt you! checked : ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True) #Makes the button checkable. Its unchecked by default

button.clicked.connect(button_clicked)



button.show()
app.exec()

"""

#VERSION3 : capture value from a slider - other example

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


#The Slot : responds when something happens
def respond_to_slider(data):
    print("slider moed to : ", data)

app=QApplication()
slider=QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#You jsut do the connection. The Qt system takes care of
# passing the data from the signal to the slot

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()