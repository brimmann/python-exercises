import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
	def __init__(self):
		"""MainWindow constructor"""
		super().__init__()
		# Main UI code goes here
		self.layout = qtw.QVBoxLayout()
		self.setLayout(self.layout)
		self.quitbutton = qtw.QPushButton('Quit')
		self.layout.addWidget(self.quitbutton)
		self.test_list = qtw.QListWidget()
		self.layout.addWidget(self.test_list)
		self.test_list.addItem("Hello")
		
		
		self.quitbutton.clicked.connect(self.close)
		#End main UI code
		self.show()
		

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
