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
		
		self.badbutton = qtw.QPushButton("Bad")
		self.layout().addWidget(self.badbutton)
		self.text_editor = qtw.QLineEdit()
		self.layout().addWidget(self.text_editor)
		
		self.text_editor.textChanged.connect(self.needs_args)
		self.badbutton.clicked.connect(self.needs_args)
		#End main UI code
		self.show()
	
	def needs_args(self, arg1):
		if isinstance(arg1, str):
			print(arg1.upper())
		else:
			print(arg1)
		

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
