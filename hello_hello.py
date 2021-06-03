import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
	def __init__(self):
		"""MainWindow constructor"""
		super().__init__()
		# Main UI code goes here
		self.setLayout(qtw.QVBoxLayout())
		self.resize(800, 600)
		mess = qtw.QLabel()
		mess.setAlignment(qtc.Qt.AlignCenter)
		self.layout().addWidget(mess)
		
		butt = qtw.QPushButton("Press Me")
		self.layout().addWidget(butt)
		
		butt.clicked.connect(lambda : mess.setText("Hello Elham"))
		
		#End main UI code
		self.show()
		

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
