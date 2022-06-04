# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.AutoText)

        self.verticalLayout_3.addWidget(self.label_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.current_date_edit = QDateEdit(self.centralwidget)
        self.current_date_edit.setObjectName(u"current_date_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_date_edit.sizePolicy().hasHeightForWidth())
        self.current_date_edit.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.current_date_edit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.risk_spinbox = QDoubleSpinBox(self.centralwidget)
        self.risk_spinbox.setObjectName(u"risk_spinbox")
        sizePolicy.setHeightForWidth(self.risk_spinbox.sizePolicy().hasHeightForWidth())
        self.risk_spinbox.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.risk_spinbox)

        self.window_size_combobox = QComboBox(self.centralwidget)
        self.window_size_combobox.setObjectName(u"window_size_combobox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.window_size_combobox)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.control_layout = QHBoxLayout()
        self.control_layout.setObjectName(u"control_layout")
        self.previous_day = QPushButton(self.centralwidget)
        self.previous_day.setObjectName(u"previous_day")

        self.control_layout.addWidget(self.previous_day)

        self.optimize_button = QPushButton(self.centralwidget)
        self.optimize_button.setObjectName(u"optimize_button")

        self.control_layout.addWidget(self.optimize_button)

        self.next_day = QPushButton(self.centralwidget)
        self.next_day.setObjectName(u"next_day")

        self.control_layout.addWidget(self.next_day)


        self.verticalLayout_4.addLayout(self.control_layout)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.tickers_table = QTableWidget(self.centralwidget)
        if (self.tickers_table.columnCount() < 3):
            self.tickers_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tickers_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tickers_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tickers_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tickers_table.setObjectName(u"tickers_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tickers_table.sizePolicy().hasHeightForWidth())
        self.tickers_table.setSizePolicy(sizePolicy1)
        self.tickers_table.horizontalHeader().setCascadingSectionResizes(False)
        self.tickers_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.tickers_table.horizontalHeader().setStretchLastSection(True)
        self.tickers_table.verticalHeader().setCascadingSectionResizes(False)
        self.tickers_table.verticalHeader().setMinimumSectionSize(20)
        self.tickers_table.verticalHeader().setDefaultSectionSize(50)
        self.tickers_table.verticalHeader().setProperty("showSortIndicator", False)
        self.tickers_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tickers_table)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 489, 525))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.assets_img = QLabel(self.scrollAreaWidgetContents_2)
        self.assets_img.setObjectName(u"assets_img")

        self.verticalLayout_7.addWidget(self.assets_img)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_8)

        self.covariance_img = QLabel(self.scrollAreaWidgetContents_2)
        self.covariance_img.setObjectName(u"covariance_img")

        self.verticalLayout.addWidget(self.covariance_img)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.efficient_port_layout = QVBoxLayout()
        self.efficient_port_layout.setObjectName(u"efficient_port_layout")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.efficient_port_layout.addWidget(self.label_6)

        self.ef_image = QLabel(self.scrollAreaWidgetContents_2)
        self.ef_image.setObjectName(u"ef_image")

        self.efficient_port_layout.addWidget(self.ef_image)


        self.gridLayout.addLayout(self.efficient_port_layout, 0, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<b>\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043c\u043e\u0434\u0435\u043b\u0438</b>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043e\u043a\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0440\u0438\u0441\u043a\u0430", None))
        self.previous_day.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.optimize_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.next_day.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_7.setText("")
        self.label_9.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<b>\u0421\u043e\u0441\u0442\u0430\u0432 \u043f\u043e\u0440\u0442\u0444\u0435\u043b\u044f</b>", None))
        ___qtablewidgetitem = self.tickers_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043a\u0435\u0440", None));
        ___qtablewidgetitem1 = self.tickers_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u044f", None));
        ___qtablewidgetitem2 = self.tickers_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<b>\u0414\u043e\u043b\u0438 \u0430\u043a\u0442\u0438\u0432\u043e\u0432</b>", None))
        self.assets_img.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<b>\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u043a\u043e\u0432\u0430\u0440\u0438\u0430\u0446\u0438\u0438</b>", None))
        self.covariance_img.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<b>\u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438</b>", None))
        self.ef_image.setText("")
    # retranslateUi

