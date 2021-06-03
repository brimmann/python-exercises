import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor.This widget will be our main window.We'll define all the UI components in here."""
        super().__init__()
        form = qtw.QWidget()
        self.setCentralWidget(form)
        form.setLayout(qtw.QVBoxLayout())
        self.filename = qtw.QLineEdit()
        self.filecontent = qtw.QTextEdit()
        self.savebutton = qtw.QPushButton('Save', clicked = self.save)
        
        form.layout().addWidget(self.filename)
        form.layout().addWidget(self.filecontent)
        form.layout().addWidget(self.savebutton)
        
    def save(self):
        filename = self.filname.text()
        error = ''
        if not filename:
            error = 'Filename empty'
        elif path.exists(filename):
            error = f'Will not overwrite {filename}'
        else:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.filecontent.toPlainText())
            except Exception as e:
                error = f'Cannot write file: {e}'
        if error:
            qtw.QMessagebox.critical(None, 'Error', error)
        super().__init__()
        # Main UI code goes here

        # End main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
