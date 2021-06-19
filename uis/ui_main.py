# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(670, 500)
        MainWindow.setMinimumSize(QSize(670, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgba(28, 29, 73, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.555012 rgba(28, 29, 73, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(16777215, 50))
        self.frame_title.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_title)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(60, 231, 195)")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_contents = QFrame(self.frame)
        self.frame_contents.setObjectName(u"frame_contents")
        self.frame_contents.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.frame_contents.setFrameShape(QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contents)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 5)
        self.frame_cpu = QFrame(self.frame_contents)
        self.frame_cpu.setObjectName(u"frame_cpu")
        self.frame_cpu.setMinimumSize(QSize(0, 0))
        self.frame_cpu.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_cpu.setFrameShape(QFrame.StyledPanel)
        self.frame_cpu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_cpu)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 50, 10, 0)
        self.label_cpu_title = QLabel(self.frame_cpu)
        self.label_cpu_title.setObjectName(u"label_cpu_title")
        self.label_cpu_title.setMinimumSize(QSize(0, 30))
        self.label_cpu_title.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_cpu_title.setFont(font1)
        self.label_cpu_title.setStyleSheet(u"color:rgb(60, 231, 195);\n"
"border:none;")
        self.label_cpu_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_cpu_title)

        self.label_cpu_usage_per = QLabel(self.frame_cpu)
        self.label_cpu_usage_per.setObjectName(u"label_cpu_usage_per")
        self.label_cpu_usage_per.setMinimumSize(QSize(0, 80))
        self.label_cpu_usage_per.setMaximumSize(QSize(16777215, 80))
        font2 = QFont()
        font2.setPointSize(50)
        self.label_cpu_usage_per.setFont(font2)
        self.label_cpu_usage_per.setStyleSheet(u"border:none;\n"
"color: rgb(220, 220, 220);")
        self.label_cpu_usage_per.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_cpu_usage_per)

        self.label_cpu_model = QLabel(self.frame_cpu)
        self.label_cpu_model.setObjectName(u"label_cpu_model")
        self.label_cpu_model.setMinimumSize(QSize(0, 20))
        self.label_cpu_model.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_cpu_model.setFont(font3)
        self.label_cpu_model.setStyleSheet(u"border:none;\n"
"color: rgb(128, 102, 168);")
        self.label_cpu_model.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_cpu_model)

        self.frame_cpu_detail = QFrame(self.frame_cpu)
        self.frame_cpu_detail.setObjectName(u"frame_cpu_detail")
        self.frame_cpu_detail.setMinimumSize(QSize(0, 0))
        self.frame_cpu_detail.setStyleSheet(u"border: none;")
        self.frame_cpu_detail.setFrameShape(QFrame.StyledPanel)
        self.frame_cpu_detail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_cpu_detail)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_cpu_detail_column = QFrame(self.frame_cpu_detail)
        self.frame_cpu_detail_column.setObjectName(u"frame_cpu_detail_column")
        self.frame_cpu_detail_column.setFrameShape(QFrame.StyledPanel)
        self.frame_cpu_detail_column.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_cpu_detail_column)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_freq_title = QLabel(self.frame_cpu_detail_column)
        self.label_freq_title.setObjectName(u"label_freq_title")
        self.label_freq_title.setMinimumSize(QSize(0, 0))
        self.label_freq_title.setMaximumSize(QSize(16777215, 16777215))
        self.label_freq_title.setFont(font3)
        self.label_freq_title.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_freq_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_freq_title)

        self.label_core_phy_title = QLabel(self.frame_cpu_detail_column)
        self.label_core_phy_title.setObjectName(u"label_core_phy_title")
        self.label_core_phy_title.setMaximumSize(QSize(16777215, 16777215))
        self.label_core_phy_title.setFont(font3)
        self.label_core_phy_title.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_phy_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_core_phy_title)

        self.label_core_log_title = QLabel(self.frame_cpu_detail_column)
        self.label_core_log_title.setObjectName(u"label_core_log_title")
        self.label_core_log_title.setMaximumSize(QSize(16777215, 16777215))
        self.label_core_log_title.setFont(font3)
        self.label_core_log_title.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_log_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_core_log_title)


        self.horizontalLayout_2.addWidget(self.frame_cpu_detail_column, 0, Qt.AlignTop)

        self.frame_cpu_detail_data = QFrame(self.frame_cpu_detail)
        self.frame_cpu_detail_data.setObjectName(u"frame_cpu_detail_data")
        self.frame_cpu_detail_data.setFrameShape(QFrame.StyledPanel)
        self.frame_cpu_detail_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_cpu_detail_data)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_freq = QLabel(self.frame_cpu_detail_data)
        self.label_freq.setObjectName(u"label_freq")
        self.label_freq.setFont(font3)
        self.label_freq.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_freq.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_freq)

        self.label_core_phy = QLabel(self.frame_cpu_detail_data)
        self.label_core_phy.setObjectName(u"label_core_phy")
        self.label_core_phy.setFont(font3)
        self.label_core_phy.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_phy.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_core_phy)

        self.label_core_log = QLabel(self.frame_cpu_detail_data)
        self.label_core_log.setObjectName(u"label_core_log")
        self.label_core_log.setFont(font3)
        self.label_core_log.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_log.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_core_log)


        self.horizontalLayout_2.addWidget(self.frame_cpu_detail_data, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_cpu_detail)


        self.horizontalLayout.addWidget(self.frame_cpu)

        self.frame_memory = QFrame(self.frame_contents)
        self.frame_memory.setObjectName(u"frame_memory")
        self.frame_memory.setMinimumSize(QSize(0, 0))
        self.frame_memory.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_memory.setFrameShape(QFrame.StyledPanel)
        self.frame_memory.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_memory)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 50, 10, 0)
        self.label_memory_title = QLabel(self.frame_memory)
        self.label_memory_title.setObjectName(u"label_memory_title")
        self.label_memory_title.setMinimumSize(QSize(0, 30))
        self.label_memory_title.setMaximumSize(QSize(16777215, 30))
        self.label_memory_title.setFont(font1)
        self.label_memory_title.setStyleSheet(u"color:rgb(60, 231, 195);\n"
"border:none;")
        self.label_memory_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_memory_title)

        self.label_memory_usage_per = QLabel(self.frame_memory)
        self.label_memory_usage_per.setObjectName(u"label_memory_usage_per")
        self.label_memory_usage_per.setMinimumSize(QSize(0, 80))
        self.label_memory_usage_per.setMaximumSize(QSize(16777215, 80))
        self.label_memory_usage_per.setFont(font2)
        self.label_memory_usage_per.setStyleSheet(u"border:none;\n"
"color: rgb(220, 220, 220);")
        self.label_memory_usage_per.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_memory_usage_per)

        self.frame_memory_detail = QFrame(self.frame_memory)
        self.frame_memory_detail.setObjectName(u"frame_memory_detail")
        self.frame_memory_detail.setMinimumSize(QSize(0, 0))
        self.frame_memory_detail.setStyleSheet(u"border: none;")
        self.frame_memory_detail.setFrameShape(QFrame.StyledPanel)
        self.frame_memory_detail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_memory_detail)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_memory_detail_column = QFrame(self.frame_memory_detail)
        self.frame_memory_detail_column.setObjectName(u"frame_memory_detail_column")
        self.frame_memory_detail_column.setFrameShape(QFrame.StyledPanel)
        self.frame_memory_detail_column.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_memory_detail_column)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_memory_total_title = QLabel(self.frame_memory_detail_column)
        self.label_memory_total_title.setObjectName(u"label_memory_total_title")
        self.label_memory_total_title.setFont(font3)
        self.label_memory_total_title.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_total_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_memory_total_title)

        self.label_memory_free_title = QLabel(self.frame_memory_detail_column)
        self.label_memory_free_title.setObjectName(u"label_memory_free_title")
        self.label_memory_free_title.setFont(font3)
        self.label_memory_free_title.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_free_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_memory_free_title)

        self.label_memory_used_title = QLabel(self.frame_memory_detail_column)
        self.label_memory_used_title.setObjectName(u"label_memory_used_title")
        self.label_memory_used_title.setFont(font3)
        self.label_memory_used_title.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_used_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_memory_used_title)


        self.horizontalLayout_3.addWidget(self.frame_memory_detail_column, 0, Qt.AlignTop)

        self.frame_memory_detail_data = QFrame(self.frame_memory_detail)
        self.frame_memory_detail_data.setObjectName(u"frame_memory_detail_data")
        self.frame_memory_detail_data.setFrameShape(QFrame.StyledPanel)
        self.frame_memory_detail_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_memory_detail_data)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_memory_total = QLabel(self.frame_memory_detail_data)
        self.label_memory_total.setObjectName(u"label_memory_total")
        self.label_memory_total.setFont(font3)
        self.label_memory_total.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_total.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_memory_total)

        self.label_memory_free = QLabel(self.frame_memory_detail_data)
        self.label_memory_free.setObjectName(u"label_memory_free")
        self.label_memory_free.setFont(font3)
        self.label_memory_free.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_free.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_memory_free)

        self.label_memory_used = QLabel(self.frame_memory_detail_data)
        self.label_memory_used.setObjectName(u"label_memory_used")
        self.label_memory_used.setFont(font3)
        self.label_memory_used.setStyleSheet(u"border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_used.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_memory_used)


        self.horizontalLayout_3.addWidget(self.frame_memory_detail_data, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_memory_detail)


        self.horizontalLayout.addWidget(self.frame_memory)


        self.verticalLayout_2.addWidget(self.frame_contents)


        self.verticalLayout.addWidget(self.frame)

        self.frame_credits = QFrame(self.centralwidget)
        self.frame_credits.setObjectName(u"frame_credits")
        self.frame_credits.setMinimumSize(QSize(0, 25))
        self.frame_credits.setMaximumSize(QSize(16777215, 25))
        self.frame_credits.setStyleSheet(u"border: none;\n"
"background-color:none;")
        self.frame_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_credits)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_credits)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        font4 = QFont()
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_10.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_credits)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 670, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Task Monitor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Task Monitor", None))
        self.label_cpu_title.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_cpu_usage_per.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_cpu_model.setText(QCoreApplication.translate("MainWindow", u"Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz", None))
        self.label_freq_title.setText(QCoreApplication.translate("MainWindow", u"Speed :", None))
        self.label_core_phy_title.setText(QCoreApplication.translate("MainWindow", u"Core (Physical) :", None))
        self.label_core_log_title.setText(QCoreApplication.translate("MainWindow", u"Core (logical) :", None))
        self.label_freq.setText(QCoreApplication.translate("MainWindow", u"3.1920 GHz", None))
        self.label_core_phy.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_core_log.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_memory_title.setText(QCoreApplication.translate("MainWindow", u"MEMORY", None))
        self.label_memory_usage_per.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_memory_total_title.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self.label_memory_free_title.setText(QCoreApplication.translate("MainWindow", u"Free :", None))
        self.label_memory_used_title.setText(QCoreApplication.translate("MainWindow", u"Used :", None))
        self.label_memory_total.setText(QCoreApplication.translate("MainWindow", u"32 GB", None))
        self.label_memory_free.setText(QCoreApplication.translate("MainWindow", u"19 GB", None))
        self.label_memory_used.setText(QCoreApplication.translate("MainWindow", u"13 GB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Create By Overload", None))
    # retranslateUi

