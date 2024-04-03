# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MG_new_transaction.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from view import res_new_window_rc

class Ui_Dialog_new(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 270)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setBaseSize(QSize(424, 270))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 70, 140, 255), stop:0.427447 rgba(48, 140, 105, 255), stop:1 rgba(48, 138,  126, 255));\n"
"font-family: BigCaslon;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255 ,255 ,255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_trans_label = QLabel(self.frame)
        self.new_trans_label.setObjectName(u"new_trans_label")
        self.new_trans_label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.new_trans_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.new_trans_label)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setAcceptDrops(False)
        self.cb_category.setStyleSheet(u"\n"
"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"border-radius: 0px;\n"
"height: 20px;\n"
"}\n"
"\n"
"QComboBox: item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setEnabled(True)
        self.data.setStyleSheet(u"font-size: 16 pt;\n"
"color: white; \n"
"padding-left: 10px;\n"
"border-radius: 0px;\n"
"height: 20px;")
        self.data.setCalendarPopup(True)
        self.data.setDate(QDate(2024, 1, 1))

        self.verticalLayout.addWidget(self.data)

        self.amount = QLineEdit(self.frame)
        self.amount.setObjectName(u"amount")
        self.amount.setAcceptDrops(False)
        self.amount.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"height: 30px;\n"
"")
        self.amount.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.amount.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.amount)

        self.descript = QLineEdit(self.frame)
        self.descript.setObjectName(u"descript")
        self.descript.setAcceptDrops(False)
        self.descript.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.descript)

        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/newPrefix/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon)
        self.save_button.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.save_button)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.new_trans_label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u0410\u043a\u0441\u0435\u0441\u0441\u0443\u0430\u0440\u044b", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"\u0411\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"\u0411\u044b\u0442\u043e\u0432\u0430\u044f \u0445\u0438\u043c\u0438\u044f", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"\u0416\u041a\u0425", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("Dialog", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.cb_category.setItemText(5, QCoreApplication.translate("Dialog", u"\u041a\u0430\u0444\u0435/\u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d\u044b", None))
        self.cb_category.setItemText(6, QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0442\u0435\u043d\u0442", None))
        self.cb_category.setItemText(7, QCoreApplication.translate("Dialog", u"\u041a\u0440\u0430\u0441\u043e\u0442\u0430 \u0438 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435", None))
        self.cb_category.setItemText(8, QCoreApplication.translate("Dialog", u"\u041c\u0435\u0434\u0438\u043a\u0430\u043c\u0435\u043d\u0442\u044b", None))
        self.cb_category.setItemText(9, QCoreApplication.translate("Dialog", u"\u041d\u0430\u043b\u043e\u0433\u0438", None))
        self.cb_category.setItemText(10, QCoreApplication.translate("Dialog", u"\u041e\u0434\u0435\u0436\u0434\u0430 \u0438 \u043e\u0431\u0443\u0432\u044c", None))
        self.cb_category.setItemText(11, QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u044b\u0445", None))
        self.cb_category.setItemText(12, QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b", None))
        self.cb_category.setItemText(13, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.cb_category.setItemText(14, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.cb_category.setItemText(15, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043d\u043e\u0435", None))
        self.cb_category.setItemText(16, QCoreApplication.translate("Dialog", u"\u0421\u0435\u0440\u0432\u0438\u0441\u044b", None))
        self.cb_category.setItemText(17, QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u043e\u0439\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b", None))
        self.cb_category.setItemText(18, QCoreApplication.translate("Dialog", u"\u0422\u0435\u0445\u043d\u0438\u043a\u0430", None))
        self.cb_category.setItemText(19, QCoreApplication.translate("Dialog", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.cb_category.setItemText(20, QCoreApplication.translate("Dialog", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442", None))
        self.cb_category.setItemText(21, QCoreApplication.translate("Dialog", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.cb_category.setItemText(22, QCoreApplication.translate("Dialog", u"\u0426\u0438\u0444\u0440\u043e\u0432\u044b\u0435 \u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.cb_category.setItemText(23, QCoreApplication.translate("Dialog", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0430", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
#if QT_CONFIG(tooltip)
        self.data.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0434\u0430\u0442\u0443 \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u0445\u043e\u0434\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.amount.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0443\u043c\u043c\u0443 \u0440\u0430\u0441\u0445\u043e\u0434\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.amount.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430...", None))
#if QT_CONFIG(tooltip)
        self.descript.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u0430, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u0442\u043e\u0432\u0430\u0440 \u0438\u043b\u0438 \u0443\u0441\u043b\u0443\u0433\u0443</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.descript.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435...", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

