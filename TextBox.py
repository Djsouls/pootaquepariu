from PyQt5.QtWidgets import QLineEdit, QWidget

class TextBox(QWidget):
	def __init__(self, parentWidget, defaultText='', placeholder='', fontSize=10, x=0, y=0, width=100, height=100):
		super().__init__()

		self.defaultText = defaultText
		self.placeholder = placeholder
		self.fontSize = fontSize
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.textBox = QLineEdit(parentWidget)

		self.setupTextBox()

	def setupTextBox(self):
		self.setTextBoxGeometry()

		self.textBox.setText(self.defaultText)

		self.textBox.setPlaceholderText(self.placeholder)

		self.setFontSize(self.fontSize)

	def setTextBoxGeometry(self):
		self.textBox.move(self.x, self.y)
		self.textBox.resize(self.width, self.height)

	def setFontSize(self, fontSize):
		font = self.textBox.font()
		font.setPointSize(fontSize)
		self.textBox.setFont(font)

	def setPosition(self, x, y):
		self.x = x
		self.y = y

		self.textBox.move(x, y)

	def setSize(self, width, height):
		self.width = width
		self.height = height

		self.textBox.resize(width, height)