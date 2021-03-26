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

AddingAnActivity = QWidget() # creates the window itself
#CODE FOR ADDING THINGS TO A RIGHT CLICK OPTION
self.actionAdd_Activity = QAction("Add an Activity")
self.tableWidget.addAction(self.actionAdd_Activity)
self.actionAdd_Activity.triggered.connect()
self.actionEdit_Activity = QAction("Edit an Activity")
self.tableWidget.addAction(self.actionAdd_Activity)
#FIN

# Code for adding data into the tables
def updateTables(self):
    db = sqlite3.connect('example.db')
    query = " SELECT * FROM Companies"
    result = db.execute(query)
    for row_num, row_data in enumerate(result):
        self.tableWidget_3.insertRow(row_num)
        for col_num, col_data in enumerate(row_data):
            self.tableWidget_3.setItem(row_num,col_num, QTableWidgetItem(str(col_data)))
        
    db.close()
#Finish here

#code to update Detailed View
def updateDetailed(self, companyID): # function which will update all the information in the detailed window
        db = sqlite3.connect('example.db')
        query = " SELECT * FROM Companies WHERE ID = %s" %(companyID)
        result = db.execute(query)
        result = result.fetchall()
        self.lineEdit.setText(str(result[0][1]))
        db.close()
        
#done      
#set Column Widths
self.tableWidget_2.setColumnWidth(2, 1000)
        
#connecting Arrows to buttons
self.toolButton_2.clicked.connect(lambda: self.updateDetailed(int(self.lineEdit_11.text())-1))
self.toolButton.clicked.connect(lambda: self.updateDetailed(int(self.lineEdit_11.text())+1))
# if table is double clicked - > do something
self.tableWidget_3.itemDoubleClicked.connect(lambda: self.updateDetailed(1))
#