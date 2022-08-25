from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('texts')

title1 = QLabel('PHP')
title2 = QLabel('JS')
title3 = QLabel('Python')
title4 = QLabel('Pascal')
title5 = QLabel('SQL')
title6 = QLabel('C++')

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
v_line = QVBoxLayout()

h_line1.addWidget(title1, alignment = Qt.AlignLeft)
h_line1.addWidget(title2, alignment = Qt.AlignRight)
h_line2.addWidget(title3, alignment = Qt.AlignLeft)
h_line2.addWidget(title4, alignment = Qt.AlignRight)
h_line3.addWidget(title5, alignment = Qt.AlignLeft)
h_line3.addWidget(title6, alignment = Qt.AlignRight)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)
main_win.setLayout(v_line)

main_win.setLayout(h_line1)
main_win.setLayout(h_line2)
main_win.setLayout(h_line3)

app.exec_()


