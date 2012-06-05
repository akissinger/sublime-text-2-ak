# import sublime, sublime_plugin
# import sys

# sys.path.append('/usr/lib/python2.7/dist-packages')

# from PySide.QtCore import *
# from PySide.QtGui import *

# class OutputBox(QDialog):
# 	def __init__(self,parent=None):
# 		super(OutputBox,self).__init__(parent)
# 		self.setWindowTitle("Snarf")
# 		self.edit = QLineEdit("Input stuff")
# 		self.button = QPushButton("Then Punch")
# 		layout = QVBoxLayout()
# 		layout.addWidget(self.edit)
# 		layout.addWidget(self.button)
# 		self.setLayout(layout)

# 		self.button.clicked.connect(self.display_message)

# 	def display_message(self):
# 		sublime.status_message("Bam: %s" % self.edit.text())

# class TestPysideCommand(sublime_plugin.WindowCommand):
# 	def open_window(self):
# 		if QApplication.instance() == None:
# 			QApplication(['-sublime-'])
# 		win = OutputBox()
# 		win.show()
# 		QApplication.instance().exec_()

# 	def run(self):
# 		print "test"
# 		self.open_window()
# 		print "finished open_window"