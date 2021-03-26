
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

app = QApplication([]) ## a REQUIREMENT for all applications to have one QApplication initialised
app.setStyle('Fusion')
window = QDialog() # creates the window itself

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(817, 162)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(440, 102, 258, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(19, 48, 218, 26))
        self.comboBox.setStyleSheet(u"alternate-background-color: rgb(214, 214, 214);")
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(255, 48, 280, 26))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(22, 18, 109, 21))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(545, 48, 244, 26))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 100, 156, 21))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Client ID", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Company Name", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Name", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Extension", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Address 1", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Address 2", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"City", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"Postcode", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"County", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Starts with", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Ends with", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"Contains", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Search in column", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Followed by number?", None))
    # retranslateUi

def main():
   # db = sqlite3.connect('example.db') #load in the database
    Mainwindow = Ui_Dialog()
    Mainwindow.setupUi(window)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
