import sys
from calendar import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget, Ui_MainWindow):
	def __init__(self):
		"""MainWindow constructor"""
		super().__init__()
		self.setupUi(self)
		# Main UI code goes here
		# disable the first category item
		self.event_category.model().item(0).setEnabled(False)
		# Populate the event list when the calendar is clicked
		self.calendar.selectionChanged.connect(self.populate_list)
		# Populate the event form when an item is selected
		self.event_list.itemSelectionChanged.connect(
		self.populate_form)
		# Save event when save is hit
		self.add_button.clicked.connect(self.save_event)
		# connect delete button
		self.del_button.clicked.connect(self.delete_event)
		# Enable 'delete' only when an event is selected
		self.event_list.itemSelectionChanged.connect(
		self.check_delete_btn)
		self.check_delete_btn()
		# check for selection of "new…" for category
		self.event_category.currentTextChanged.connect(
		self.on_category_change)
		#End main UI code
		self.show()
	def clear_form(self):
		self.event_title.clear()
		self.event_category.setCurrentIndex(0)
		self.event_time.setTime(qtc.QTime(8, 0))
		self.allday_check.setChecked(False)
		self.event_detail.setPlainText('')
	
	def populate_list(self):
		self.event_list.clear()
		self.clear_form()
		date = self.calendar.selectedDate()
		for event in self.events.get(date, []):
			time = (event['time'].toString('hh:mm') if event['time'] else 'All Day')
			self.event_list.addItem(f"{time}: {event['title']}")
			
	def populate_form(self):
		self.clear_form()
		date = self.calendar.selectedDate()
		event_number = self.event_list.currentRow()
		if event_number == -1:
			return
		event_data = self.events.get(date)[event_number]
		
		self.event_category.setCurrentText(event_data['category'])
		if event_data['time'] is None:
			self.allday_check.setChecked(True)
		else:
			self.event_time.setTime(event_data['time'])
		self.event_title.setText(event_data['title'])
		self.event_detail.setPlainText(event_data['detail'])
	
	def save_event(self):
		event = {'category': self.event_category.currentText(), 'time': (None if self.allday_check.isChecked() else self.event_time.time()), 'title' : self.event_title.text(), 'detail': self.event_detail.toPlainText()}
		
		date = self.calendar.selectedDate()
		event_list = self.events.get(date, [])
		event_number = self.event_list.currentRow()
		
		if event_number == -1:
			event_list.append(event)
		else:
			event_list[event_number] = event
		
		event_list.sort(key = lambda x: x['time'] or qtc.QTime(0, 0))
		self.events[date] = event_list
		self.populate_list()
	
	def delete_event(self):
		date = self.calendar.selectedDate()
		row = self.event_list.currentRow()
		del(self.events[date][row])
		self.event_list.setCurrentRow(-1)
		self.clear_form()
		self.populate_list()
		
	def check_delete_btn(self):
		self.del_button.setDisabled(self.event_list.currentRow() == -1)
	
	def on_category_change(self, text):
		if text == 'New...':
			self.dialog = CategoryWindow()
			self.dialog.submitted.connect(self.add_category)
			self.event_category.setCurrentIndex(0)
	
	def add_category(self, category):
		print("Entered2")
		self.event_category.addItem(category)
		self.event_category.setCurrentText(category)
		

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
