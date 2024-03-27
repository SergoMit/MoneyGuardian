# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MoneyGuardianUI_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from bookkeeper.view import res_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 589)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 70, 140, 255), stop:0.427447 rgba(48, 140, 105, 255), stop:1 rgba(48, 138,  126, 255));\n"
"font-family: BigCaslon;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tables_name = QFrame(self.centralwidget)
        self.tables_name.setObjectName(u"tables_name")
        self.tables_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1 px solid rgba(255,255, 255, 40);\n"
"border-radius: 7px;")
        self.horizontalLayout_4 = QHBoxLayout(self.tables_name)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.expense_label = QLabel(self.tables_name)
        self.expense_label.setObjectName(u"expense_label")
        self.expense_label.setEnabled(True)
        self.expense_label.setStyleSheet(u"color: SandyBrown;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"\n"
"")
        self.expense_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.expense_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.day_label = QLabel(self.tables_name)
        self.day_label.setObjectName(u"day_label")
        self.day_label.setStyleSheet(u"font-weight: bold;\n"
"")
        self.day_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.day_label)

        self.week_label = QLabel(self.tables_name)
        self.week_label.setObjectName(u"week_label")
        self.week_label.setStyleSheet(u"font-weight: bold;\n"
"")
        self.week_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.week_label)

        self.month_label = QLabel(self.tables_name)
        self.month_label.setObjectName(u"month_label")
        self.month_label.setStyleSheet(u"font-weight: bold;\n"
"")
        self.month_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.month_label)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.day_expense = QLabel(self.tables_name)
        self.day_expense.setObjectName(u"day_expense")
        self.day_expense.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.day_expense)

        self.week_expense = QLabel(self.tables_name)
        self.week_expense.setObjectName(u"week_expense")
        self.week_expense.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.week_expense)

        self.month_expense = QLabel(self.tables_name)
        self.month_expense.setObjectName(u"month_expense")
        self.month_expense.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.month_expense)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budget_label = QLabel(self.tables_name)
        self.budget_label.setObjectName(u"budget_label")
        self.budget_label.setStyleSheet(u"color: SandyBrown;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"")
        self.budget_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.budget_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.day_budget = QLabel(self.tables_name)
        self.day_budget.setObjectName(u"day_budget")
        self.day_budget.setStyleSheet(u"color: MediumSpringGreen;")
        self.day_budget.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.day_budget)

        self.week_budget = QLabel(self.tables_name)
        self.week_budget.setObjectName(u"week_budget")
        self.week_budget.setStyleSheet(u"color: LawnGreen;")
        self.week_budget.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.week_budget)

        self.month_budget = QLabel(self.tables_name)
        self.month_budget.setObjectName(u"month_budget")
        self.month_budget.setStyleSheet(u"color: Lime;")
        self.month_budget.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.month_budget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.residual_label = QLabel(self.tables_name)
        self.residual_label.setObjectName(u"residual_label")
        self.residual_label.setStyleSheet(u"color: SandyBrown;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"")
        self.residual_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.residual_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.day_residual = QLabel(self.tables_name)
        self.day_residual.setObjectName(u"day_residual")
        self.day_residual.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.day_residual)

        self.week_residual = QLabel(self.tables_name)
        self.week_residual.setObjectName(u"week_residual")
        self.week_residual.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.week_residual)

        self.month_residual = QLabel(self.tables_name)
        self.month_residual.setObjectName(u"month_residual")
        self.month_residual.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.month_residual)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addWidget(self.tables_name)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:none;\n"
"border:none;\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.new_button = QPushButton(self.frame)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255, 255, 0);\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.new_button.setIcon(icon)
        self.new_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.new_button, 0, 0, 1, 1)

        self.change_button = QPushButton(self.frame)
        self.change_button.setObjectName(u"change_button")
        self.change_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255, 255, 0);\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.change_button.setIcon(icon1)
        self.change_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.change_button, 0, 1, 1, 1)

        self.del_button = QPushButton(self.frame)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255, 255, 0);\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.del_button.setIcon(icon2)
        self.del_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.del_button, 0, 2, 1, 1)

        self.budget_button = QPushButton(self.frame)
        self.budget_button.setObjectName(u"budget_button")
        self.budget_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255, 255, 0);\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/change_budget.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.budget_button.setIcon(icon3)
        self.budget_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.budget_button, 0, 3, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.table_viewer = QTableWidget(self.centralwidget)
        self.table_viewer.setObjectName(u"table_viewer")

        self.verticalLayout_8.addWidget(self.table_viewer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Money Guardian", None))
        self.expense_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.day_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c ", None))
        self.week_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0435\u043b\u044f ", None))
        self.month_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446 ", None))
        self.day_expense.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.week_expense.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.month_expense.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.budget_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044e\u0434\u0436\u0435\u0442", None))
        self.day_budget.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.week_budget.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.month_budget.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.residual_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a", None))
        self.day_residual.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.week_residual.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.month_residual.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.new_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.change_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.del_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.budget_button.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044e\u0434\u0436\u0435\u0442", None))
    # retranslateUi

