import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QGridLayout, QWidget

from TextBox import TextBox
from Color import Color
from CryptoExchangeGraph import CryptoExchangeGraph

'''
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 0, 1)
        layout.addWidget(Color('blue'), 1, 0)
        layout.addWidget(Color('purple'), 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

'''

class Root(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUi()

	def initUi(self):
		self.setWindowTitle('Haha just kill me')
		self.setGeometry(250, 35, 850, 685)

		layout = QGridLayout()

		layout.addWidget(CryptoExchangeGraph('BTC', 'USD'), 0, 0)
		layout.addWidget(CryptoExchangeGraph('XMR', 'JPY'), 0, 1)
		layout.addWidget(CryptoExchangeGraph('NMC', 'EUR'), 1, 0)
		layout.addWidget(CryptoExchangeGraph('DOGE', 'MXN'), 1, 1)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		self.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = Root()
    sys.exit(app.exec_())