# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'budget_set_UI.ui'
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

class Ui_Dialog_budget(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 288)
        Dialog.setBaseSize(QSize(412, 288))
        Dialog.setAcceptDrops(True)
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
        self.new_budget_label = QLabel(self.frame)
        self.new_budget_label.setObjectName(u"new_budget_label")
        self.new_budget_label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.new_budget_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.new_budget_label)

        self.bud_per_day = QLineEdit(self.frame)
        self.bud_per_day.setObjectName(u"bud_per_day")
        self.bud_per_day.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.bud_per_day)

        self.bud_per_week = QLineEdit(self.frame)
        self.bud_per_week.setObjectName(u"bud_per_week")
        self.bud_per_week.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"height: 30px;\n"
"")
        self.bud_per_week.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bud_per_week.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.bud_per_week)

        self.bud_per_month = QLineEdit(self.frame)
        self.bud_per_month.setObjectName(u"bud_per_month")
        self.bud_per_month.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.bud_per_month)

        self.save_budget_button = QPushButton(self.frame)
        self.save_budget_button.setObjectName(u"save_budget_button")
        self.save_budget_button.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/newPrefix/icons/change_budget.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_budget_button.setIcon(icon)
        self.save_budget_button.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.save_budget_button)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0411\u044e\u0434\u0436\u0435\u0442", None))
        self.new_budget_label.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u0431\u044e\u0434\u0436\u0435\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.bud_per_day.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u0443\u044e \u0441\u0443\u043c\u043c\u0443 \u0437\u0430\u0442\u0440\u0430\u0442 \u0437\u0430 \u0434\u0435\u043d\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bud_per_day.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430 \u0434\u0435\u043d\u044c...", None))
#if QT_CONFIG(tooltip)
        self.bud_per_week.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u0443\u044e \u0441\u0443\u043c\u043c\u0443 \u0437\u0430\u0442\u0440\u0430\u0442 \u0437\u0430 \u043d\u0435\u0434\u0435\u043b\u044e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bud_per_week.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e...", None))
#if QT_CONFIG(tooltip)
        self.bud_per_month.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u0443\u044e \u0441\u0443\u043c\u043c\u0443 \u0437\u0430\u0442\u0440\u0430\u0442 \u0437\u0430 \u043c\u0435\u0441\u044f\u0446</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bud_per_month.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430 \u043c\u0435\u0441\u044f\u0446...", None))
        self.save_budget_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

