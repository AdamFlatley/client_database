import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
tableWidget = QTableWidget()
tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)

quitAction = QAction("Quit", None)
quitAction.triggered.connect(qApp.quit)
tableWidget.addAction(quitAction)

tableWidget.show()
sys.exit(app.exec_())