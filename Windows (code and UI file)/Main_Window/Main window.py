import sqlite3      #imports the sqlite3 library so that you can use it
import string
import datetime

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
#import Resources_rc

app = QApplication([]) ## a REQUIREMENT for all applications to have one QApplication initialised
app.setStyle('Fusion')
window = QMainWindow() # creates the window itself
searchWindow = QDialogButtonBox()
AddClientWindow = QDialogButtonBox()
AddClientPopup = QDialogButtonBox()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1923, 915)
        MainWindow.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.action_New_Database = QAction(MainWindow)
        self.action_New_Database.setObjectName(u"action_New_Database")
        self.action_Open_Database = QAction(MainWindow)
        self.action_Open_Database.setObjectName(u"action_Open_Database")
        self.action_Save_Database = QAction(MainWindow)
        self.action_Save_Database.setObjectName(u"action_Save_Database")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionAdd_Client = QAction(MainWindow)
        self.actionAdd_Client.setObjectName(u"actionAdd_Client")
        icon = QIcon()
        icon.addFile(u"../../../Resources for program/Add_Client.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionAdd_Client.setIcon(icon)
        self.actionAdd_New_Seconday_Contact = QAction(MainWindow)
        self.actionAdd_New_Seconday_Contact.setObjectName(u"actionAdd_New_Seconday_Contact")
        self.actionAdd_New_Alarm = QAction(MainWindow)
        self.actionAdd_New_Alarm.setObjectName(u"actionAdd_New_Alarm")
        icon1 = QIcon()
        icon1.addFile(u"../../../Resources for program/calendar_icon_orange-plus-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"../../../Resources for program/calendar_icon_orange-plus-sign.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionAdd_New_Alarm.setIcon(icon1)
        self.actionSort_Clients = QAction(MainWindow)
        self.actionSort_Clients.setObjectName(u"actionSort_Clients")
        icon2 = QIcon()
        icon2.addFile(u"../../../Resources for program/Sort.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSort_Clients.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1914, 1020))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(-18, 60, 181, 881))
        self.listWidget.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(165, 292, 1708, 657))
        self.tabWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1705, 611))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setMidLineWidth(10)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(37)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableWidget_2 = QTableWidget(self.tab_4)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 2, 1708, 564))
        self.tableWidget_2.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tableWidget_4 = QTableWidget(self.tab_5)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(0, 0, 1715, 589))
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(92, -32, 93, 28))
        self.pushButton.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(162, 60, 1710, 231))
        self.groupBox.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(193, 193, 193);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(17, 34, 131, 21))
        self.label_2.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(15, 91, 131, 21))
        self.label_11.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(17, 63, 131, 21))
        self.label_12.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(385, 36, 131, 21))
        self.label_13.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(385, 66, 131, 21))
        self.label_14.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(15, 147, 131, 21))
        self.label_15.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(15, 119, 131, 21))
        self.label_16.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(385, 96, 117, 21))
        self.label_17.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(144, 35, 191, 22))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(144, 63, 191, 22))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(510, 36, 191, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(510, 66, 191, 22))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(510, 100, 191, 22))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(144, 91, 191, 22))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(144, 119, 191, 22))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(144, 147, 191, 22))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(15, 175, 131, 21))
        self.label_18.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(144, 175, 191, 22))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(150, 18, 180, 2))
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 10, 120, 20))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: bold 7pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(381, 8, 120, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: bold 7pt \"MS Shell Dlg 2\";")
        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(516, 16, 180, 2))
        self.line_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(388, 128, 131, 21))
        self.label_19.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(509, 131, 191, 22))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(508, 165, 191, 22))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(386, 156, 114, 21))
        self.label_21.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(825, 15, 131, 21))
        self.label_20.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(1130, 14, 36, 32))
        self.toolButton.setStyleSheet(u"")
        self.toolButton_2 = QToolButton(self.groupBox)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(950, 15, 34, 28))
        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(990, 10, 134, 34))
        self.label_22.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(2, -32, 93, 28))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.tabWidget.addTab(self.tab, "")
        self.groupBox.raise_()
        self.listWidget.raise_()
        self.tabWidget_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listWidget_2 = QListWidget(self.tab_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(-12, 60, 181, 896))
        self.listWidget_2.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.tableWidget_3 = QTableWidget(self.tab_2)
        if (self.tableWidget_3.columnCount() < 13):
            self.tableWidget_3.setColumnCount(13)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, __qtablewidgetitem21)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(168, 111, 1741, 807))
        self.tableWidget_3.setMinimumSize(QSize(811, 651))
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(167, 60, 1743, 52))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(199, 123, 123);")
        self.toolButton_3 = QToolButton(self.groupBox_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(7, 4, 80, 43))
        self.toolButton_3.setStyleSheet(u"")
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QSize(30, 40))
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_4 = QToolButton(self.groupBox_2)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(93, 5, 80, 43))
        self.toolButton_4.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../../Resources for program/Search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QSize(30, 30))
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_5 = QToolButton(self.groupBox_2)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(181, 5, 126, 42))
        self.toolButton_5.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../../../Resources for program/backwards arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QSize(30, 30))
        self.toolButton_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.calendarWidget = QCalendarWidget(self.tab_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(435, 3, 1473, 809))
        self.calendarWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(200, 200, 200);\n"
"")
        self.calendarWidget.setFirstDayOfWeek(Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.listWidget1 = QListWidget(self.tab_6)
        self.listWidget1.setObjectName(u"listWidget1")
        self.listWidget1.setGeometry(QRect(0, 118, 431, 676))
        self.listWidget1.setAutoFillBackground(False)
        self.listWidget1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(197, 197, 197);")
        self.listWidget1.setLineWidth(1)
        self.listWidget1.setMidLineWidth(0)
        self.listWidget1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.groupBox_3 = QGroupBox(self.tab_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 2, 430, 117))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(22, 9, 115, 86))
        self.label_4.setStyleSheet(u"font: 48pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(161, 4, 170, 77))
        self.label_5.setStyleSheet(u"font: 24pt \"MS Shell Dlg 2\";")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(163, 65, 145, 34))
        self.label_6.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1923, 26))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.action_New_Database)
        self.menu_File.addAction(self.action_Open_Database)
        self.menu_File.addAction(self.action_Save_Database)
        self.menu_File.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionAdd_Client)
        self.toolBar.addAction(self.actionAdd_New_Alarm)

        self.retranslateUi(MainWindow)
        self.tableWidget_3.itemDoubleClicked.connect(self.tabWidget.update)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_New_Database.setText(QCoreApplication.translate("MainWindow", u"&New Database", None))
#if QT_CONFIG(shortcut)
        self.action_New_Database.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_Open_Database.setText(QCoreApplication.translate("MainWindow", u"&Open Database", None))
#if QT_CONFIG(shortcut)
        self.action_Open_Database.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save_Database.setText(QCoreApplication.translate("MainWindow", u"&Save Database", None))
#if QT_CONFIG(shortcut)
        self.action_Save_Database.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionAdd_Client.setText(QCoreApplication.translate("MainWindow", u"Add Client", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_Client.setToolTip(QCoreApplication.translate("MainWindow", u"Adds a Client to the Database", None))
#endif // QT_CONFIG(tooltip)
        self.actionAdd_New_Seconday_Contact.setText(QCoreApplication.translate("MainWindow", u"Add New Seconday Contact", None))
        self.actionAdd_New_Alarm.setText(QCoreApplication.translate("MainWindow", u"Add New Alarm", None))
        self.actionSort_Clients.setText(QCoreApplication.translate("MainWindow", u"Sort Clients", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Subject", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Activities", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Note", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Notes", None))
        ___qtablewidgetitem6 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Contact Name", None));
        ___qtablewidgetitem7 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem8 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Secondary Contacts", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"List View", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Client Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Address 1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Address 2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Extension", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Business Details", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"County", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Postcode", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Client Number", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0 of 0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Detailed View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Detailed View", None))
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Client ID", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Company Name", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Extension", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Address 1", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Address 2", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"County", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Postcode", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(10)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(11)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(12)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Other Info", None));
        self.groupBox_2.setTitle("")
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"Remove filters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"List View", None))
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>NUMBER</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MONTH", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DAY", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Calendar View", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

def main():
    db = sqlite3.connect('example.db') #load in the database
    Mainwindow = Ui_MainWindow()
    Mainwindow.setupUi(window)
    db.close()
    window.showMaximized()
    app.exec_()

if __name__ == "__main__":
    main()