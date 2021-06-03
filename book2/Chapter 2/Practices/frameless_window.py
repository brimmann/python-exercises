import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
	def __init__(self):
		"""MainWindow constructor"""
		super().__init__(cursor=qtc.Qt.WaitCursor)
		self.setWindowState(qtc.Qt.WindowFullScreen)
		self.setWindowFlags(qtc.Qt.FramelessWindowHint)
		# Main UI code goes here
		#End main UI code
		self.show()
		

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
