
#Importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

#the sys module is responsible for processing command line arguments
import sys 

app= QApplication(sys.argv)

window=QWidget()
window.show()

#Start the event loop
app.exec()