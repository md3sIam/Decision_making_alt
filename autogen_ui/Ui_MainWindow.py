# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 30)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.m_matricesFrame = QtWidgets.QFrame(self.centralwidget)
        self.m_matricesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_matricesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_matricesFrame.setObjectName("m_matricesFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.m_matricesFrame)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.m_matrixA = QtWidgets.QFrame(self.m_matricesFrame)
        self.m_matrixA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_matrixA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_matrixA.setObjectName("m_matrixA")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.m_matrixA)
        self.horizontalLayout_2.setContentsMargins(0, 0, 40, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelA = QtWidgets.QLabel(self.m_matrixA)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelA.setFont(font)
        self.labelA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelA.setObjectName("labelA")
        self.horizontalLayout_2.addWidget(self.labelA)
        self.tableViewA = QtWidgets.QTableView(self.m_matrixA)
        self.tableViewA.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableViewA.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableViewA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableViewA.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableViewA.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableViewA.setObjectName("tableViewA")
        self.tableViewA.horizontalHeader().setVisible(True)
        self.tableViewA.verticalHeader().setVisible(True)
        self.horizontalLayout_2.addWidget(self.tableViewA)
        self.horizontalLayout.addWidget(self.m_matrixA)
        self.m_matrixB = QtWidgets.QFrame(self.m_matricesFrame)
        self.m_matrixB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_matrixB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_matrixB.setObjectName("m_matrixB")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.m_matrixB)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelB = QtWidgets.QLabel(self.m_matrixB)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setItalic(False)
        self.labelB.setFont(font)
        self.labelB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelB.setObjectName("labelB")
        self.horizontalLayout_3.addWidget(self.labelB)
        self.tableViewB = QtWidgets.QTableView(self.m_matrixB)
        self.tableViewB.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableViewB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableViewB.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableViewB.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableViewB.setObjectName("tableViewB")
        self.horizontalLayout_3.addWidget(self.tableViewB)
        self.horizontalLayout.addWidget(self.m_matrixB)
        self.horizontalLayout.setStretch(0, 32)
        self.horizontalLayout.setStretch(1, 8)
        self.verticalLayout.addWidget(self.m_matricesFrame)
        self.m_buttonsFrame = QtWidgets.QFrame(self.centralwidget)
        self.m_buttonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_buttonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_buttonsFrame.setObjectName("m_buttonsFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.m_buttonsFrame)
        self.horizontalLayout_4.setContentsMargins(66, 10, 8, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.m_changeEqualitySizeFrame = QtWidgets.QFrame(self.m_buttonsFrame)
        self.m_changeEqualitySizeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_changeEqualitySizeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_changeEqualitySizeFrame.setObjectName("m_changeEqualitySizeFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.m_changeEqualitySizeFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(21)
        self.gridLayout.setObjectName("gridLayout")
        self.m_removeRowButton = QtWidgets.QPushButton(self.m_changeEqualitySizeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_removeRowButton.sizePolicy().hasHeightForWidth())
        self.m_removeRowButton.setSizePolicy(sizePolicy)
        self.m_removeRowButton.setMinimumSize(QtCore.QSize(0, 40))
        self.m_removeRowButton.setMaximumSize(QtCore.QSize(40, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_removeRowButton.setFont(font)
        self.m_removeRowButton.setStyleSheet("color: white;\n"
"border-radius: 20px; \n"
"background-color: #ff5353;")
        self.m_removeRowButton.setObjectName("m_removeRowButton")
        self.gridLayout.addWidget(self.m_removeRowButton, 0, 2, 1, 1)
        self.m_removeColumnButton = QtWidgets.QPushButton(self.m_changeEqualitySizeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_removeColumnButton.sizePolicy().hasHeightForWidth())
        self.m_removeColumnButton.setSizePolicy(sizePolicy)
        self.m_removeColumnButton.setMinimumSize(QtCore.QSize(0, 40))
        self.m_removeColumnButton.setMaximumSize(QtCore.QSize(40, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_removeColumnButton.setFont(font)
        self.m_removeColumnButton.setStyleSheet("color:white;\n"
"border-radius: 20px; \n"
"background-color: #ff5353;")
        self.m_removeColumnButton.setObjectName("m_removeColumnButton")
        self.gridLayout.addWidget(self.m_removeColumnButton, 1, 2, 1, 1)
        self.m_addRowButton = QtWidgets.QPushButton(self.m_changeEqualitySizeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_addRowButton.sizePolicy().hasHeightForWidth())
        self.m_addRowButton.setSizePolicy(sizePolicy)
        self.m_addRowButton.setMinimumSize(QtCore.QSize(0, 40))
        self.m_addRowButton.setMaximumSize(QtCore.QSize(40, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_addRowButton.setFont(font)
        self.m_addRowButton.setStyleSheet("color: white;\n"
"border-radius: 20px; \n"
"background-color: #79f079;")
        self.m_addRowButton.setObjectName("m_addRowButton")
        self.gridLayout.addWidget(self.m_addRowButton, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.m_changeEqualitySizeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.m_addColumnButton = QtWidgets.QPushButton(self.m_changeEqualitySizeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_addColumnButton.sizePolicy().hasHeightForWidth())
        self.m_addColumnButton.setSizePolicy(sizePolicy)
        self.m_addColumnButton.setMinimumSize(QtCore.QSize(0, 40))
        self.m_addColumnButton.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_addColumnButton.setFont(font)
        self.m_addColumnButton.setStyleSheet("border-radius: 20px; \n"
"background-color: #79f079;\n"
"color: white;")
        self.m_addColumnButton.setObjectName("m_addColumnButton")
        self.gridLayout.addWidget(self.m_addColumnButton, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.m_changeEqualitySizeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 40)
        self.gridLayout.setColumnMinimumWidth(2, 40)
        self.horizontalLayout_4.addWidget(self.m_changeEqualitySizeFrame)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.m_checkButtonFrame = QtWidgets.QFrame(self.m_buttonsFrame)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        self.m_checkButtonFrame.setFont(font)
        self.m_checkButtonFrame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.m_checkButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_checkButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_checkButtonFrame.setObjectName("m_checkButtonFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.m_checkButtonFrame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.m_checkButton = QtWidgets.QPushButton(self.m_checkButtonFrame)
        self.m_checkButton.setMinimumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.m_checkButton.setFont(font)
        self.m_checkButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.m_checkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.m_checkButton.setStyleSheet("")
        self.m_checkButton.setObjectName("m_checkButton")
        self.verticalLayout_2.addWidget(self.m_checkButton)
        self.horizontalLayout_4.addWidget(self.m_checkButtonFrame)
        self.verticalLayout.addWidget(self.m_buttonsFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 26))
        self.menubar.setObjectName("menubar")
        self.m_formMenu = QtWidgets.QMenu(self.menubar)
        self.m_formMenu.setObjectName("m_formMenu")
        self.m_aboutMenu = QtWidgets.QMenu(self.menubar)
        self.m_aboutMenu.setObjectName("m_aboutMenu")
        MainWindow.setMenuBar(self.menubar)
        self.m_setMatrixSizeAction = QtWidgets.QAction(MainWindow)
        self.m_setMatrixSizeAction.setObjectName("m_setMatrixSizeAction")
        self.m_aboutAction = QtWidgets.QAction(MainWindow)
        self.m_aboutAction.setObjectName("m_aboutAction")
        self.m_setCellSizeAction = QtWidgets.QAction(MainWindow)
        self.m_setCellSizeAction.setObjectName("m_setCellSizeAction")
        self.m_formMenu.addAction(self.m_setMatrixSizeAction)
        self.m_formMenu.addAction(self.m_setCellSizeAction)
        self.m_aboutMenu.addAction(self.m_aboutAction)
        self.menubar.addAction(self.m_formMenu.menuAction())
        self.menubar.addAction(self.m_aboutMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверка системы на совместность"))
        self.labelA.setText(_translate("MainWindow", "A = "))
        self.labelB.setText(_translate("MainWindow", "b = "))
        self.m_removeRowButton.setText(_translate("MainWindow", "-"))
        self.m_removeColumnButton.setText(_translate("MainWindow", "-"))
        self.m_addRowButton.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Строка:"))
        self.m_addColumnButton.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "Столбец:"))
        self.m_checkButton.setText(_translate("MainWindow", "Проверить систему на совместность"))
        self.m_formMenu.setTitle(_translate("MainWindow", "Форма"))
        self.m_aboutMenu.setTitle(_translate("MainWindow", "Справка"))
        self.m_setMatrixSizeAction.setText(_translate("MainWindow", "Задать размеры матрицы А"))
        self.m_aboutAction.setText(_translate("MainWindow", "О приложении"))
        self.m_setCellSizeAction.setText(_translate("MainWindow", "Задать размеры ячеек"))
