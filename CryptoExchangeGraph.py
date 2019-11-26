from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

from TextBox import TextBox
from Canvas import Canvas

class CryptoExchangeGraph(QWidget):
	def __init__(self, defaultCrypto='BTC', defaultExchange='USD'):
		super().__init__()
		
		self.setAutoFillBackground(True)

		fontSize = 10

		cryptoX = 320
		cryptoY = 30
		cryptoWidth = 70
		cryptoHeight = 25

		horizontalTextBoxSpace = 30

		exchangeX = cryptoX + cryptoWidth + horizontalTextBoxSpace
		exchangeY = cryptoY + cryptoHeight + 25
		exchangeWidth = cryptoWidth
		exchangeHeight = cryptoHeight

		self.canvas = Canvas(self)
		self.canvas.move(0, 0)
		self.canvas.resize(315, 300)

		labelWidth = 30
		labelCrypto = QLabel(self)
		labelCrypto.setText('Crypto')
		labelCrypto.move(cryptoX + (cryptoWidth - labelWidth)/2.5, cryptoY - 20)

		labelExchange = QLabel(self)
		labelExchange.setText('Exchange')
		labelExchange.move(cryptoX + (cryptoWidth - labelWidth)/2.5 - 2, exchangeY - 20)

		self.cryptoTextBox = TextBox(self, defaultText=defaultCrypto, placeholder='Crypto', fontSize=fontSize, x=cryptoX, y=cryptoY, width=cryptoWidth, height=cryptoHeight)
		self.exchangeTextBox = TextBox(self, defaultText=defaultExchange, placeholder='Exchange', fontSize=fontSize, x=cryptoX, y=exchangeY, width=cryptoWidth, height=exchangeHeight)

		buttonGo = QPushButton('Go', self)
		buttonGo.move(cryptoX - 2, exchangeY + exchangeHeight + 20)
		buttonGo.clicked.connect(self.updateGraph)

	def updateGraph(self):
		print('ohayo')