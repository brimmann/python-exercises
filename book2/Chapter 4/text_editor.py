import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
class SettingsDialog(qtw.QDialog):
	"""Dialog for setting the settings"""
	def __init__(self, settings, parent = None):
		super().__init__(parent, modal = True)
		self.setLayout(qtw.QFormLayout())
		self.settings = settings
		self.layout().addRow(qtw.QLabel('<h1>Application Setting</h1>'),)
		self.show_warnings_cb = qtw.QCheckBox(checked = settings.value('show_warnings', type=bool))
		self.layout().addRow("Show Warning", self.show_warnings_cb)
		self.show_dock_cb = qtw.QCheckBox(checked = settings.value('show_dock', type=bool))
		self.layout().addRow("Show Dock Tools", self.show_dock_cb)
		
		self.accept_btn = qtw.QPushButton('Ok', clicked = self.accept)
		self.cancel_btn = qtw.QPushButton('Cancel', clicked = self.reject)
		self.layout().addRow(self.accept_btn, self.cancel_btn)
		#self.show()
	
	def accept(self):
		self.settings.setValue('show_warnings', self.show_warnings_cb.isChecked())
		self.settings.setValue('show_dock', self.show_dock_cb.isChecked())
		super().accept()
		
class MainWindow(qtw.QMainWindow):
	#setting = {'show_warnings': True}
	settings = qtc.QSettings('Alan D Moore', 'text editor')
	def __init__(self):
		"""MainWindow constructor"""
		super().__init__()
		# Main UI code goes here
		#Central Widget#
		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)
		self.resize(420, 320)
		self.setWindowTitle("Text Editor Alpha")
		
		#Statusbar#
		self.statusBar().showMessage('Welcome to text_editor.py')
		charcount_label = qtw.QLabel("chars: 0")
		self.textedit.textChanged.connect(lambda: charcount_label.setText("chars: " + str(len(self.textedit.toPlainText()))))
		self.statusBar().addPermanentWidget(charcount_label)
		
		#Menubar#
		menubar = self.menuBar()
		file_menu = menubar.addMenu('File')
		edit_menu = menubar.addMenu('Edit')
		help_menu = menubar.addMenu('Help')
		#Menu Actions#
		open_action = file_menu.addAction('Open')
		save_action = file_menu.addAction('Save')
		quit_action = file_menu.addAction('Quit', self.destroy)
		edit_menu.addAction('Undo', self.textedit.undo)
		redo_action = qtw.QAction('Redo', self)
		redo_action.triggered.connect(self.textedit.redo)
		edit_menu.addAction(redo_action)
		help_menu.addAction('About', self.showAboutDialog)
		open_action.triggered.connect(self.openFile)
		save_action.triggered.connect(self.saveFile)
		font_action = edit_menu.addAction("font")
		settings_action = edit_menu.addAction("settings")
		font_action.triggered.connect(self.set_font)
		settings_action.triggered.connect(self.show_settings)
		
		#Toolbar#
		toolbar = self.addToolBar('File')
		#Tollbar Actions#
		toolbar.addAction(open_action)
		#Disable Movement#
		toolbar.setMovable(False)
		toolbar.setFloatable(False)
		#Alowing Sides#
		toolbar.setAllowedAreas(qtc.Qt.TopToolBarArea | qtc.Qt.BottomToolBarArea)
		#Adding Icons#
		open_icon = self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
		save_icon = self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)
		open_action.setIcon(open_icon)
		toolbar.addAction(save_icon, 'Save', lambda: self.statusBar().showMessage('File Saved!'))
		help_action = qtw.QAction(self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton), 'help', self, triggered = lambda: self.statusBar().showMessage('Sorry, no help yet!'))
		toolbar.addAction(help_action)
		#Add Another Toolbar#
		toolbar2 = qtw.QToolBar('Edit')
		toolbar2.addAction('Copy', self.textedit.copy)
		toolbar2.addAction('Cut', self.textedit.cut)
		toolbar2.addAction('Paste', self.textedit.paste)
		self.addToolBar(qtc.Qt.RightToolBarArea, toolbar2)
		
		#Adding Dock Widget
		if self.settings.value('show_dock', False, type=bool):
			dock = qtw.QDockWidget("Replace")
			self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)
			dock.setFeatures(qtw.QDockWidget.DockWidgetMovable)
			#Form
			replace_widget = qtw.QWidget()
			replace_widget.setLayout(qtw.QVBoxLayout())
			dock.setWidget(replace_widget)
			self.search_text_inp = qtw.QLineEdit(placeholderText = 'search')
			self.replace_text_inp = qtw.QLineEdit(placeholderText = 'replace')
			search_and_replace_btn = qtw.QPushButton("Search and Replace", clicked = self.search_and_replace)
			replace_widget.layout().addWidget(self.search_text_inp)
			replace_widget.layout().addWidget(self.replace_text_inp)
			replace_widget.layout().addWidget(search_and_replace_btn)
			replace_widget.layout().addStretch()
		
		#Dialog and Message Boxes
		if self.settings.value('show_warnings', False, type=bool):
			response = qtw.QMessageBox.question(self, 'My Text Editor', 'This is beta software, do you want to continue?', qtw.QMessageBox.Yes | qtw.QMessageBox.Abort)
			if response == qtw.QMessageBox.Abort:
				self.close()
				sys.exit()
			#custom box
			splash_screen = qtw.QMessageBox()
			splash_screen.setWindowTitle('My Text Editor')
			splash_screen.setText('BETA SOFTWARE WARNING!')
			splash_screen.setInformativeText('This is very, very beta, are you really sure you want to use it?')
			splash_screen.setDetailedText('This editor was wirtten for pedagogical purposes, and probably is not fit for real work.')
			splash_screen.setWindowModality(qtc.Qt.WindowModal)
			splash_screen.addButton(qtw.QMessageBox.Yes)
			splash_screen.addButton(qtw.QMessageBox.Abort)
			response = splash_screen.exec()
			if response == qtw.QMessageBox.Abort:
				self.close()
				sys.exit()
		#End main UI code
		self.show()
	
	def search_and_replace(self):
		s_text = self.search_text_inp.text()
		r_text = self.replace_text_inp.text()
		
		if s_text:
			self.textedit.setText(self.textedit.toPlainText().replace(s_text, r_text))
		
	def showAboutDialog(self):
		qtw.QMessageBox.about(self, "About text_editor.py", "This is a text editor written in PyQt5.")
	
	def openFile(self):
		filename, _ = qtw.QFileDialog.getOpenFileName(self, "Select a text file to open..", qtc.QDir.homePath(), 'Text Files (*.txt)', 'Text Files (*.txt)', qtw.QFileDialog.DontResolveSymlinks)
		if filename:
			try:
				with open(filename, 'r') as fh:
					self.textedit.setText(fh.read())
			except Exception as e:
				qtw.QMessageBox.critical(f"Could not load file: {e}")
				
	def saveFile(self):
		filename, _ = qtw.QFileDialog.getSaveFileName(self, "Select the file to save to...", qtc.QDir.homePath(), 'Text Files (*.txt)')
		if filename:
			try:
				with open(filename, 'w') as fh:
					fh.write(self.textedit.toPlainText())
			except Exception as e:
				qtw.QMessageBox.critical(f"could not save file: {e}")
	
	def set_font(self):
		current = self.textedit.currentFont()
		font, accepted = qtw.QFontDialog.getFont(current, self, options = (qtw.QFontDialog.DontUseNativeDialog | qtw.QFontDialog.MonospacedFonts))
		if accepted:
			self.textedit.setCurrentFont(font)
	def show_settings(self):
		settings_dialog = SettingsDialog(self.settings, self)
		settings_dialog.exec()

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
