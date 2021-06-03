import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    

    def __init__(self):
        """MainWindow constructor.This widget will be our main window.We'll define all the UI components in here."""
        super().__init__()
         # The list widget
        data = [ 'Hamburger', 'Cheeseburger', 'Chicked Nuggets', 'Hot Dog', 'Fish SandWich']
        self.setLayout(qtw.QVBoxLayout())
        listwidget = qtw.QListWidget()
        listwidget.addItems(data)
    
        #the Combobox
        combobox = qtw.QComboBox()
        combobox.addItems(data)
        self.layout().addWidget(listwidget)
        self.layout().addWidget(combobox)
        
        for i in range(listwidget.count()):
            item = listwidget.item(i)
            item.setFlags(item.flags() | qtc.Qt.ItemIsEditable)
        
        
        model = qtc.QStringListModel(data)
        listview = qtw.QListView()
        listview.setModel(model)
        listview.setModel(model)
        model_combobox = qtw.QComboBox()
        model_combobox.setModel(model)
        
        self.layout().addWidget(listview)
        self.layout().addWidget(model_combobox)
    
        self.layout()
        # Main UI code goes here

        # End main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
