import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
class Turner(object):
	def __init__(self):
		self
	
	def TurnIt(self, string):
		
		txt = string.upper()
		print(txt)
class MainWindow(qtw.QWidget):
	def __init__(self):
		"""MainWindow constructor"""
		super().__init__()
		# Main UI code goes here
		self.entry1 = qtw.QLineEdit()
		self.entry2 = qtw.QLineEdit()
		self.button = qtw.QPushButton("Done")
		self.button2 = qtw.QPushButton("Show")
		ref = Turner()
		
		layout = qtw.QVBoxLayout()
		layout.addWidget(self.entry1)
		#layout.addWidget(self.entry2)
		layout.addWidget(self.button)
		#layout.addWidget(self.button2)
		self.setLayout(layout)
		
		#self.entry1.textChanged.connect()
		self.entry1.editingFinished.connect(lambda: print('editing finishid'))
		#self.entry2.returnPressed.connect(self.entry1.editingFinished)
		self.button.clicked.connect(self.entry1.editingFinished)
		#End main UI code
		self.show()
		

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
