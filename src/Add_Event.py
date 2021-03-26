from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

app = QApplication([]) ## a REQUIREMENT for all applications to have one QApplication initialised
window = QDockWidget() 

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(720, 470)
        DockWidget.setMinimumSize(QSize(720, 470))
        DockWidget.setMaximumSize(QSize(720, 470))
        DockWidget.setStyleSheet(u"background-color: rgb(154, 154, 154);")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.groupBox = QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 700, 450))
        self.groupBox.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
"border-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 32, 196, 46))
        self.label_2.setStyleSheet(u"")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 176, 303, 97))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(78, 359, 137, 59))
        self.pushButton.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(204, 204, 204);")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(310, 102, 360, 240))
        self.textEdit.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.dateTimeEdit = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(310, 24, 360, 61))
        self.dateTimeEdit.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(494, 363, 137, 59))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">When is the event?</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-size:12pt;\">What is the event regarding?</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Create Event", None))
        self.textEdit.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("DockWidget", u"Cancel", None))
    # retranslateUi
        
def main():
    Mainwindow = Ui_DockWidget()
    Mainwindow.setupUi(window)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()