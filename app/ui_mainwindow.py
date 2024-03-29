# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\GitHub\Repasitories\Signalerator\app\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 570))
        MainWindow.setMaximumSize(QtCore.QSize(800, 570))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(241, 243, 245);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        MainWindow.setAnimated(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget.setObjectName("centralwidget")
        self.signalFormsWidget = QtWidgets.QWidget(self.centralwidget)
        self.signalFormsWidget.setGeometry(QtCore.QRect(30, 309, 331, 211))
        self.signalFormsWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.signalFormsWidget.setObjectName("signalFormsWidget")
        self.signalFormLayout = QtWidgets.QVBoxLayout(self.signalFormsWidget)
        self.signalFormLayout.setContentsMargins(20, 20, 20, 20)
        self.signalFormLayout.setSpacing(0)
        self.signalFormLayout.setObjectName("signalFormLayout")
        self.signalFormsLabel = QtWidgets.QLabel(self.signalFormsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalFormsLabel.sizePolicy().hasHeightForWidth())
        self.signalFormsLabel.setSizePolicy(sizePolicy)
        self.signalFormsLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.signalFormsLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signalFormsLabel.setFont(font)
        self.signalFormsLabel.setStyleSheet("padding: 0;")
        self.signalFormsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.signalFormsLabel.setObjectName("signalFormsLabel")
        self.signalFormLayout.addWidget(self.signalFormsLabel)
        self.signalFormsForm = QtWidgets.QWidget(self.signalFormsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalFormsForm.sizePolicy().hasHeightForWidth())
        self.signalFormsForm.setSizePolicy(sizePolicy)
        self.signalFormsForm.setStyleSheet("padding: 0;")
        self.signalFormsForm.setObjectName("signalFormsForm")
        self.singalFormForm = QtWidgets.QFormLayout(self.signalFormsForm)
        self.singalFormForm.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.singalFormForm.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.singalFormForm.setContentsMargins(-1, -1, -1, 0)
        self.singalFormForm.setHorizontalSpacing(11)
        self.singalFormForm.setVerticalSpacing(0)
        self.singalFormForm.setObjectName("singalFormForm")
        self.rectangleSignalButton = QtWidgets.QRadioButton(self.signalFormsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rectangleSignalButton.sizePolicy().hasHeightForWidth())
        self.rectangleSignalButton.setSizePolicy(sizePolicy)
        self.rectangleSignalButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rectangleSignalButton.setFont(font)
        self.rectangleSignalButton.setStyleSheet("padding: 0;")
        self.rectangleSignalButton.setCheckable(False)
        self.rectangleSignalButton.setChecked(False)
        self.rectangleSignalButton.setObjectName("rectangleSignalButton")
        self.singalFormForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rectangleSignalButton)
        self.triangularSignalButton = QtWidgets.QRadioButton(self.signalFormsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.triangularSignalButton.sizePolicy().hasHeightForWidth())
        self.triangularSignalButton.setSizePolicy(sizePolicy)
        self.triangularSignalButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.triangularSignalButton.setFont(font)
        self.triangularSignalButton.setStyleSheet("padding: 0;")
        self.triangularSignalButton.setCheckable(False)
        self.triangularSignalButton.setObjectName("triangularSignalButton")
        self.singalFormForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.triangularSignalButton)
        self.sinusoidButton = QtWidgets.QRadioButton(self.signalFormsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidButton.sizePolicy().hasHeightForWidth())
        self.sinusoidButton.setSizePolicy(sizePolicy)
        self.sinusoidButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sinusoidButton.setFont(font)
        self.sinusoidButton.setStyleSheet("padding: 0;")
        self.sinusoidButton.setCheckable(False)
        self.sinusoidButton.setObjectName("sinusoidButton")
        self.singalFormForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sinusoidButton)
        self.customSignalButton = QtWidgets.QRadioButton(self.signalFormsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customSignalButton.sizePolicy().hasHeightForWidth())
        self.customSignalButton.setSizePolicy(sizePolicy)
        self.customSignalButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customSignalButton.setFont(font)
        self.customSignalButton.setStyleSheet("padding: 0;")
        self.customSignalButton.setCheckable(False)
        self.customSignalButton.setObjectName("customSignalButton")
        self.singalFormForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.customSignalButton)
        self.customSignalLineEdit = QtWidgets.QLineEdit(self.signalFormsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customSignalLineEdit.sizePolicy().hasHeightForWidth())
        self.customSignalLineEdit.setSizePolicy(sizePolicy)
        self.customSignalLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.customSignalLineEdit.setStyleSheet("* {\n"
"    padding: 0;\n"
"    background-color: rgb(240, 240, 240);\n"
"    color: rgb(100, 100, 100);\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"    border: 1px solid rgb(240, 240, 240);\n"
"}\n"
"\n"
"*[readOnly=\"false\"][verified=\"true\"] {\n"
"    border-color: green;\n"
"}\n"
"\n"
"*[readOnly=\"false\"][verified=\"false\"] {\n"
"    border-color: red;\n"
"}\n"
"\n"
"*:read-only {\n"
"    background-color: rgb(210, 210, 210);\n"
"}")
        self.customSignalLineEdit.setText("")
        self.customSignalLineEdit.setMaxLength(100)
        self.customSignalLineEdit.setReadOnly(True)
        self.customSignalLineEdit.setClearButtonEnabled(False)
        self.customSignalLineEdit.setProperty("verified", False)
        self.customSignalLineEdit.setObjectName("customSignalLineEdit")
        self.singalFormForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.customSignalLineEdit)
        self.noSignalButton = QtWidgets.QRadioButton(self.signalFormsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noSignalButton.sizePolicy().hasHeightForWidth())
        self.noSignalButton.setSizePolicy(sizePolicy)
        self.noSignalButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.noSignalButton.setFont(font)
        self.noSignalButton.setStyleSheet("padding: 0;")
        self.noSignalButton.setChecked(True)
        self.noSignalButton.setObjectName("noSignalButton")
        self.singalFormForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.noSignalButton)
        self.customSignalLineEdit.raise_()
        self.triangularSignalButton.raise_()
        self.customSignalButton.raise_()
        self.rectangleSignalButton.raise_()
        self.sinusoidButton.raise_()
        self.noSignalButton.raise_()
        self.signalFormLayout.addWidget(self.signalFormsForm)
        self.settingsWidget = QtWidgets.QWidget(self.centralwidget)
        self.settingsWidget.setGeometry(QtCore.QRect(30, 140, 331, 151))
        self.settingsWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.settingsWidget)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsLabel = QtWidgets.QLabel(self.settingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsLabel.sizePolicy().hasHeightForWidth())
        self.settingsLabel.setSizePolicy(sizePolicy)
        self.settingsLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.settingsLabel.setFont(font)
        self.settingsLabel.setStyleSheet("padding: 0;")
        self.settingsLabel.setObjectName("settingsLabel")
        self.verticalLayout_4.addWidget(self.settingsLabel)
        self.settingsForm = QtWidgets.QWidget(self.settingsWidget)
        self.settingsForm.setStyleSheet("padding: 0;")
        self.settingsForm.setObjectName("settingsForm")
        self.voltageForm = QtWidgets.QFormLayout(self.settingsForm)
        self.voltageForm.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.voltageForm.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.voltageForm.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.voltageForm.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.voltageForm.setContentsMargins(0, 10, 0, 0)
        self.voltageForm.setHorizontalSpacing(30)
        self.voltageForm.setVerticalSpacing(10)
        self.voltageForm.setObjectName("voltageForm")
        self.minVoltageLabel = QtWidgets.QLabel(self.settingsForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minVoltageLabel.setFont(font)
        self.minVoltageLabel.setStyleSheet("padding: 0;")
        self.minVoltageLabel.setObjectName("minVoltageLabel")
        self.voltageForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minVoltageLabel)
        self.minVoltageSpinBox = QtWidgets.QDoubleSpinBox(self.settingsForm)
        self.minVoltageSpinBox.setMinimumSize(QtCore.QSize(60, 20))
        self.minVoltageSpinBox.setStyleSheet("padding: 0;\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius: 3px;\n"
"padding-left: 5px;")
        self.minVoltageSpinBox.setWrapping(False)
        self.minVoltageSpinBox.setFrame(False)
        self.minVoltageSpinBox.setReadOnly(False)
        self.minVoltageSpinBox.setDecimals(1)
        self.minVoltageSpinBox.setMinimum(0.0)
        self.minVoltageSpinBox.setMaximum(1.0)
        self.minVoltageSpinBox.setSingleStep(0.1)
        self.minVoltageSpinBox.setProperty("value", 0.0)
        self.minVoltageSpinBox.setObjectName("minVoltageSpinBox")
        self.voltageForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minVoltageSpinBox)
        self.maxVoltageLabel = QtWidgets.QLabel(self.settingsForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maxVoltageLabel.setFont(font)
        self.maxVoltageLabel.setStyleSheet("padding: 0;")
        self.maxVoltageLabel.setObjectName("maxVoltageLabel")
        self.voltageForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxVoltageLabel)
        self.maxVoltageSpinBox = QtWidgets.QDoubleSpinBox(self.settingsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxVoltageSpinBox.sizePolicy().hasHeightForWidth())
        self.maxVoltageSpinBox.setSizePolicy(sizePolicy)
        self.maxVoltageSpinBox.setMinimumSize(QtCore.QSize(60, 20))
        self.maxVoltageSpinBox.setStyleSheet("padding: 0;\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius: 3px;\n"
"padding-left: 5px")
        self.maxVoltageSpinBox.setDecimals(1)
        self.maxVoltageSpinBox.setMinimum(0.1)
        self.maxVoltageSpinBox.setMaximum(5.0)
        self.maxVoltageSpinBox.setSingleStep(0.1)
        self.maxVoltageSpinBox.setProperty("value", 1.0)
        self.maxVoltageSpinBox.setObjectName("maxVoltageSpinBox")
        self.voltageForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxVoltageSpinBox)
        self.periodLabel = QtWidgets.QLabel(self.settingsForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.periodLabel.setFont(font)
        self.periodLabel.setStyleSheet("padding: 0;")
        self.periodLabel.setObjectName("periodLabel")
        self.voltageForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.periodLabel)
        self.periodSpinBox = QtWidgets.QDoubleSpinBox(self.settingsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.periodSpinBox.sizePolicy().hasHeightForWidth())
        self.periodSpinBox.setSizePolicy(sizePolicy)
        self.periodSpinBox.setMinimumSize(QtCore.QSize(60, 20))
        self.periodSpinBox.setStyleSheet("padding: 0;\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius: 3px;\n"
"padding-left: 5px")
        self.periodSpinBox.setDecimals(2)
        self.periodSpinBox.setMinimum(0.2)
        self.periodSpinBox.setMaximum(60.0)
        self.periodSpinBox.setSingleStep(0.01)
        self.periodSpinBox.setProperty("value", 1.0)
        self.periodSpinBox.setObjectName("periodSpinBox")
        self.voltageForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.periodSpinBox)
        self.verticalLayout_4.addWidget(self.settingsForm)
        self.rightWidget = QtWidgets.QWidget(self.centralwidget)
        self.rightWidget.setGeometry(QtCore.QRect(379, 30, 391, 490))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightWidget.sizePolicy().hasHeightForWidth())
        self.rightWidget.setSizePolicy(sizePolicy)
        self.rightWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.rightWidget.setObjectName("rightWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.rightWidget)
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.currentVoltageLabel = QtWidgets.QLabel(self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentVoltageLabel.sizePolicy().hasHeightForWidth())
        self.currentVoltageLabel.setSizePolicy(sizePolicy)
        self.currentVoltageLabel.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.currentVoltageLabel.setFont(font)
        self.currentVoltageLabel.setStyleSheet("padding: 0;")
        self.currentVoltageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentVoltageLabel.setObjectName("currentVoltageLabel")
        self.verticalLayout_5.addWidget(self.currentVoltageLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.currentVoltageLCDLayout = QtWidgets.QHBoxLayout()
        self.currentVoltageLCDLayout.setSpacing(0)
        self.currentVoltageLCDLayout.setObjectName("currentVoltageLCDLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.currentVoltageLCDLayout.addItem(spacerItem1)
        self.currentVoltageLCD = QtWidgets.QLCDNumber(self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentVoltageLCD.sizePolicy().hasHeightForWidth())
        self.currentVoltageLCD.setSizePolicy(sizePolicy)
        self.currentVoltageLCD.setMinimumSize(QtCore.QSize(0, 130))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.currentVoltageLCD.setFont(font)
        self.currentVoltageLCD.setStyleSheet("padding: 0;\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 10px;")
        self.currentVoltageLCD.setFrameShape(QtWidgets.QFrame.Box)
        self.currentVoltageLCD.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentVoltageLCD.setLineWidth(1)
        self.currentVoltageLCD.setSmallDecimalPoint(False)
        self.currentVoltageLCD.setDigitCount(4)
        self.currentVoltageLCD.setMode(QtWidgets.QLCDNumber.Dec)
        self.currentVoltageLCD.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.currentVoltageLCD.setProperty("intValue", 0)
        self.currentVoltageLCD.setObjectName("currentVoltageLCD")
        self.currentVoltageLCDLayout.addWidget(self.currentVoltageLCD)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.currentVoltageLCDLayout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.currentVoltageLCDLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem3)
        self.graphLayout = QtWidgets.QHBoxLayout()
        self.graphLayout.setSpacing(0)
        self.graphLayout.setObjectName("graphLayout")
        self.graphWidget = PlotWidget(self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setMinimumSize(QtCore.QSize(310, 200))
        self.graphWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.graphWidget.setStyleSheet("padding: 0;\n"
"border: 1px solid rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.graphWidget.setObjectName("graphWidget")
        self.graphLayout.addWidget(self.graphWidget)
        self.verticalLayout_5.addLayout(self.graphLayout)
        self.connectWidget = QtWidgets.QWidget(self.centralwidget)
        self.connectWidget.setGeometry(QtCore.QRect(30, 30, 331, 90))
        self.connectWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.connectWidget.setObjectName("connectWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.connectWidget)
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalWidget_4 = QtWidgets.QWidget(self.connectWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_4.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_4.setSizePolicy(sizePolicy)
        self.horizontalWidget_4.setStyleSheet("padding: 0;\n"
"border-radius: 0;")
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.connectLabel = QtWidgets.QLabel(self.horizontalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectLabel.sizePolicy().hasHeightForWidth())
        self.connectLabel.setSizePolicy(sizePolicy)
        self.connectLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connectLabel.setFont(font)
        self.connectLabel.setObjectName("connectLabel")
        self.horizontalLayout_7.addWidget(self.connectLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.connectStatusLabel = QtWidgets.QLabel(self.horizontalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectStatusLabel.sizePolicy().hasHeightForWidth())
        self.connectStatusLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.connectStatusLabel.setFont(font)
        self.connectStatusLabel.setStyleSheet("* {\n"
"    color: red;\n"
"}\n"
"\n"
"*[connected=\"true\"] {\n"
"    color: green;\n"
"}")
        self.connectStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectStatusLabel.setProperty("connected", False)
        self.connectStatusLabel.setObjectName("connectStatusLabel")
        self.horizontalLayout_7.addWidget(self.connectStatusLabel)
        self.verticalLayout_6.addWidget(self.horizontalWidget_4)
        self.horizontalWidget = QtWidgets.QWidget(self.connectWidget)
        self.horizontalWidget.setStyleSheet("padding: 0;\n"
"border-radius: 0;")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.portsList = QtWidgets.QComboBox(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portsList.sizePolicy().hasHeightForWidth())
        self.portsList.setSizePolicy(sizePolicy)
        self.portsList.setMinimumSize(QtCore.QSize(105, 20))
        self.portsList.setMaximumSize(QtCore.QSize(150, 16777215))
        self.portsList.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 3px;\n"
"padding-left: 5px;")
        self.portsList.setCurrentText("")
        self.portsList.setMaxVisibleItems(10)
        self.portsList.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.portsList.setFrame(True)
        self.portsList.setObjectName("portsList")
        self.horizontalLayout_4.addWidget(self.portsList)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.connectButton = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setMinimumSize(QtCore.QSize(95, 22))
        self.connectButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(220, 220, 230);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton[checkable=\"true\"] {\n"
"    background-color: rgb(0, 163, 245);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton[checkable=\"true\"]:hover {\n"
"    background-color: rgb(0, 143, 225);\n"
"}\n"
"\n"
"QPushButton[checkable=\"true\"]:pressed {\n"
"    background-color: rgb(0, 123, 205);\n"
"}\n"
"\n"
"QPushButton[connected=\"true\"]{\n"
"    background-color: rgb(200, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"            \n"
"QPushButton[connected=\"true\"]:hover {\n"
"    background-color: rgb(180, 0, 0);\n"
"}\n"
"")
        self.connectButton.setCheckable(False)
        self.connectButton.setAutoExclusive(False)
        self.connectButton.setProperty("connected", False)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_4.addWidget(self.connectButton)
        self.verticalLayout_6.addWidget(self.horizontalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QtCore.QSize(800, 20))
        self.statusBar.setMaximumSize(QtCore.QSize(800, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(False)
        self.statusBar.setFont(font)
        self.statusBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusBar.setStyleSheet("background-color: rgb(230, 232, 233);\n"
"text-align: middle;")
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.portsList, self.connectButton)
        MainWindow.setTabOrder(self.connectButton, self.minVoltageSpinBox)
        MainWindow.setTabOrder(self.minVoltageSpinBox, self.maxVoltageSpinBox)
        MainWindow.setTabOrder(self.maxVoltageSpinBox, self.rectangleSignalButton)
        MainWindow.setTabOrder(self.rectangleSignalButton, self.triangularSignalButton)
        MainWindow.setTabOrder(self.triangularSignalButton, self.sinusoidButton)
        MainWindow.setTabOrder(self.sinusoidButton, self.customSignalButton)
        MainWindow.setTabOrder(self.customSignalButton, self.customSignalLineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signalerator"))
        self.signalFormsLabel.setText(_translate("MainWindow", "Вид сигнала"))
        self.rectangleSignalButton.setText(_translate("MainWindow", "Прямоугольный"))
        self.triangularSignalButton.setText(_translate("MainWindow", "Треугольный"))
        self.sinusoidButton.setText(_translate("MainWindow", "Синусоида"))
        self.customSignalButton.setText(_translate("MainWindow", "Произвольный"))
        self.customSignalLineEdit.setPlaceholderText(_translate("MainWindow", "Введите функцию V(x)"))
        self.noSignalButton.setText(_translate("MainWindow", "Отключено"))
        self.settingsLabel.setText(_translate("MainWindow", "Настройки"))
        self.minVoltageLabel.setText(_translate("MainWindow", "Мин. выходное напряжение"))
        self.minVoltageSpinBox.setSuffix(_translate("MainWindow", " V"))
        self.maxVoltageLabel.setText(_translate("MainWindow", "Макс. выходное напряжение"))
        self.maxVoltageSpinBox.setSuffix(_translate("MainWindow", " V"))
        self.periodLabel.setText(_translate("MainWindow", "Период функции"))
        self.periodSpinBox.setSuffix(_translate("MainWindow", " s"))
        self.currentVoltageLabel.setText(_translate("MainWindow", "Текущее напряжение"))
        self.connectLabel.setText(_translate("MainWindow", "Подключение"))
        self.connectStatusLabel.setText(_translate("MainWindow", "не подключено"))
        self.connectButton.setText(_translate("MainWindow", "Подключиться"))
from pyqtgraph import PlotWidget
