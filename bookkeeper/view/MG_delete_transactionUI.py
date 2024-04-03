# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MG_delete_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from view import res_new_window_rc

class Ui_Dialog_delete(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(431, 164)
        Dialog.setBaseSize(QSize(431, 164))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 70, 140, 255), stop:0.427447 rgba(48, 140, 105, 255), stop:1 rgba(48, 138,  126, 255));\n"
"font-family: BigCaslon;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255 ,255 ,255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.delete_trans_label = QLabel(self.frame)
        self.delete_trans_label.setObjectName(u"delete_trans_label")
        self.delete_trans_label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.delete_trans_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.delete_trans_label)

        self.delete_id = QLineEdit(self.frame)
        self.delete_id.setObjectName(u"delete_id")
        self.delete_id.setAcceptDrops(False)
        self.delete_id.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.delete_id)

        self.delete_button = QPushButton(self.frame)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255, 255, 0);\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"border-radius: 7px;\n"
"height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon)
        self.delete_button.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.delete_button)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.delete_trans_label.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
#if QT_CONFIG(tooltip)
        self.delete_id.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435  id \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438, \u0438\u043c\u0435\u044e\u0449\u0435\u0439\u0441\u044f \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_id.setPlaceholderText(QCoreApplication.translate("Dialog", u" id...", None))
        self.delete_button.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

