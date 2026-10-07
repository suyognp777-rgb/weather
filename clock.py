import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt


class digitalclock(QWidget):
    def __innit__(self):
        super().__innit__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(700,400,300,100)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
    def settime(self):
        self.update



if __name__=="__main__":
    app = QApplication(sys.argv)
    clock=digitalclock()
    clock.show()
    sys.exit(app.exec_())

