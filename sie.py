import sys
import requests
from PyQt5.QtWidgets import QApplication ,QWidget
from PyQt5.QtCore import Qt
app=QApplication(sys.argv)#yo application le k kaam garx ta controls functionality honita yo ta hamle control garni ho py dwara so we pass sys.argv  to control sys with python instruction
window=QWidget()
window.show()
sys.exit(app.exec_())
