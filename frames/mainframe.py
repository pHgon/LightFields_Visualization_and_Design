# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 695)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 131, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 109, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 58, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 131, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 109, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 58, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 131, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 109, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 58, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label_tela = QtWidgets.QLabel(self.centralwidget)
        self.label_tela.setGeometry(QtCore.QRect(440, 20, 901, 631))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_tela.setPalette(palette)
        self.label_tela.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_tela.setMouseTracking(True)
        self.label_tela.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_tela.setAutoFillBackground(True)
        self.label_tela.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_tela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_tela.setLineWidth(5)
        self.label_tela.setText("")
        self.label_tela.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tela.setIndent(0)
        self.label_tela.setObjectName("label_tela")
        self.groupBox_cores = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_cores.setGeometry(QtCore.QRect(20, 220, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_cores.setFont(font)
        self.groupBox_cores.setTitle("")
        self.groupBox_cores.setObjectName("groupBox_cores")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_cores)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_nitidez = QtWidgets.QSpinBox(self.groupBox_cores)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_nitidez.setFont(font)
        self.spinBox_nitidez.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_nitidez.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_nitidez.setSuffix("")
        self.spinBox_nitidez.setMinimum(-100)
        self.spinBox_nitidez.setMaximum(100)
        self.spinBox_nitidez.setSingleStep(1)
        self.spinBox_nitidez.setProperty("value", 0)
        self.spinBox_nitidez.setDisplayIntegerBase(10)
        self.spinBox_nitidez.setObjectName("spinBox_nitidez")
        self.gridLayout.addWidget(self.spinBox_nitidez, 3, 2, 1, 1)
        self.label_contraste = QtWidgets.QLabel(self.groupBox_cores)
        self.label_contraste.setObjectName("label_contraste")
        self.gridLayout.addWidget(self.label_contraste, 2, 0, 1, 1)
        self.slider_nitidez = QtWidgets.QSlider(self.groupBox_cores)
        self.slider_nitidez.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_nitidez.setMinimum(-100)
        self.slider_nitidez.setMaximum(100)
        self.slider_nitidez.setProperty("value", 0)
        self.slider_nitidez.setOrientation(QtCore.Qt.Horizontal)
        self.slider_nitidez.setObjectName("slider_nitidez")
        self.gridLayout.addWidget(self.slider_nitidez, 3, 1, 1, 1)
        self.label_brilho = QtWidgets.QLabel(self.groupBox_cores)
        self.label_brilho.setObjectName("label_brilho")
        self.gridLayout.addWidget(self.label_brilho, 1, 0, 1, 1)
        self.spinBox_contraste = QtWidgets.QSpinBox(self.groupBox_cores)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_contraste.setFont(font)
        self.spinBox_contraste.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_contraste.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_contraste.setSuffix("")
        self.spinBox_contraste.setMinimum(-100)
        self.spinBox_contraste.setMaximum(100)
        self.spinBox_contraste.setProperty("value", 0)
        self.spinBox_contraste.setObjectName("spinBox_contraste")
        self.gridLayout.addWidget(self.spinBox_contraste, 2, 2, 1, 1)
        self.slider_contraste = QtWidgets.QSlider(self.groupBox_cores)
        self.slider_contraste.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_contraste.setMinimum(-100)
        self.slider_contraste.setMaximum(100)
        self.slider_contraste.setProperty("value", 0)
        self.slider_contraste.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contraste.setObjectName("slider_contraste")
        self.gridLayout.addWidget(self.slider_contraste, 2, 1, 1, 1)
        self.label_saturacao = QtWidgets.QLabel(self.groupBox_cores)
        self.label_saturacao.setObjectName("label_saturacao")
        self.gridLayout.addWidget(self.label_saturacao, 4, 0, 1, 1)
        self.spinBox_brilho = QtWidgets.QSpinBox(self.groupBox_cores)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_brilho.setFont(font)
        self.spinBox_brilho.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_brilho.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_brilho.setSuffix("")
        self.spinBox_brilho.setMinimum(-100)
        self.spinBox_brilho.setMaximum(100)
        self.spinBox_brilho.setProperty("value", 0)
        self.spinBox_brilho.setDisplayIntegerBase(10)
        self.spinBox_brilho.setObjectName("spinBox_brilho")
        self.gridLayout.addWidget(self.spinBox_brilho, 1, 2, 1, 1)
        self.slider_brilho = QtWidgets.QSlider(self.groupBox_cores)
        self.slider_brilho.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.slider_brilho.setMouseTracking(False)
        self.slider_brilho.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_brilho.setMinimum(-100)
        self.slider_brilho.setMaximum(100)
        self.slider_brilho.setProperty("value", 0)
        self.slider_brilho.setTracking(True)
        self.slider_brilho.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brilho.setObjectName("slider_brilho")
        self.gridLayout.addWidget(self.slider_brilho, 1, 1, 1, 1)
        self.label_nitidez = QtWidgets.QLabel(self.groupBox_cores)
        self.label_nitidez.setObjectName("label_nitidez")
        self.gridLayout.addWidget(self.label_nitidez, 3, 0, 1, 1)
        self.label_text_cores = QtWidgets.QLabel(self.groupBox_cores)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_text_cores.setFont(font)
        self.label_text_cores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_cores.setObjectName("label_text_cores")
        self.gridLayout.addWidget(self.label_text_cores, 0, 0, 1, 1)
        self.spinBox_saturacao = QtWidgets.QSpinBox(self.groupBox_cores)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_saturacao.setFont(font)
        self.spinBox_saturacao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_saturacao.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_saturacao.setSuffix("")
        self.spinBox_saturacao.setMinimum(-100)
        self.spinBox_saturacao.setMaximum(100)
        self.spinBox_saturacao.setSingleStep(1)
        self.spinBox_saturacao.setProperty("value", 0)
        self.spinBox_saturacao.setDisplayIntegerBase(10)
        self.spinBox_saturacao.setObjectName("spinBox_saturacao")
        self.gridLayout.addWidget(self.spinBox_saturacao, 4, 2, 1, 1)
        self.slider_saturacao = QtWidgets.QSlider(self.groupBox_cores)
        self.slider_saturacao.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_saturacao.setMinimum(-100)
        self.slider_saturacao.setMaximum(100)
        self.slider_saturacao.setProperty("value", 0)
        self.slider_saturacao.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturacao.setObjectName("slider_saturacao")
        self.gridLayout.addWidget(self.slider_saturacao, 4, 1, 1, 1)
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_cores)
        self.pushButton_reset.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout.addWidget(self.pushButton_reset, 0, 2, 1, 1)
        self.pushButton_depthmap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_depthmap.setGeometry(QtCore.QRect(50, 430, 131, 61))
        self.pushButton_depthmap.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_depthmap.setObjectName("pushButton_depthmap")
        self.pushButton_alldepthmaps = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_alldepthmaps.setGeometry(QtCore.QRect(260, 430, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_alldepthmaps.setFont(font)
        self.pushButton_alldepthmaps.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_alldepthmaps.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_alldepthmaps.setAcceptDrops(False)
        self.pushButton_alldepthmaps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_alldepthmaps.setAutoFillBackground(False)
        self.pushButton_alldepthmaps.setCheckable(False)
        self.pushButton_alldepthmaps.setObjectName("pushButton_alldepthmaps")
        self.l_ang_hoz = QtWidgets.QLabel(self.centralwidget)
        self.l_ang_hoz.setGeometry(QtCore.QRect(300, 190, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_ang_hoz.setFont(font)
        self.l_ang_hoz.setObjectName("l_ang_hoz")
        self.l_ang_ver = QtWidgets.QLabel(self.centralwidget)
        self.l_ang_ver.setGeometry(QtCore.QRect(340, 190, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_ang_ver.setFont(font)
        self.l_ang_ver.setObjectName("l_ang_ver")
        self.label_hist = QtWidgets.QLabel(self.centralwidget)
        self.label_hist.setGeometry(QtCore.QRect(30, 100, 201, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_hist.setPalette(palette)
        self.label_hist.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_hist.setMouseTracking(True)
        self.label_hist.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_hist.setAutoFillBackground(True)
        self.label_hist.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_hist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_hist.setLineWidth(5)
        self.label_hist.setText("")
        self.label_hist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hist.setIndent(0)
        self.label_hist.setObjectName("label_hist")
        self.label_text_histograma = QtWidgets.QLabel(self.centralwidget)
        self.label_text_histograma.setGeometry(QtCore.QRect(30, 60, 161, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_text_histograma.setFont(font)
        self.label_text_histograma.setObjectName("label_text_histograma")
        self.label_text_minimapa = QtWidgets.QLabel(self.centralwidget)
        self.label_text_minimapa.setGeometry(QtCore.QRect(278, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_text_minimapa.setFont(font)
        self.label_text_minimapa.setObjectName("label_text_minimapa")
        self.radioButton_red = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_red.setGeometry(QtCore.QRect(40, 190, 51, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.radioButton_red.setPalette(palette)
        self.radioButton_red.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_red.setChecked(True)
        self.radioButton_red.setAutoExclusive(False)
        self.radioButton_red.setObjectName("radioButton_red")
        self.radioButton_green = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_green.setGeometry(QtCore.QRect(100, 190, 61, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.radioButton_green.setPalette(palette)
        self.radioButton_green.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_green.setChecked(True)
        self.radioButton_green.setAutoExclusive(False)
        self.radioButton_green.setObjectName("radioButton_green")
        self.radioButton_blue = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_blue.setGeometry(QtCore.QRect(170, 190, 61, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.radioButton_blue.setPalette(palette)
        self.radioButton_blue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_blue.setChecked(True)
        self.radioButton_blue.setAutoExclusive(False)
        self.radioButton_blue.setObjectName("radioButton_blue")
        self.label_text_exibicao = QtWidgets.QLabel(self.centralwidget)
        self.label_text_exibicao.setGeometry(QtCore.QRect(30, 0, 151, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_text_exibicao.setFont(font)
        self.label_text_exibicao.setObjectName("label_text_exibicao")
        self.radioButton_original = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_original.setGeometry(QtCore.QRect(150, 40, 83, 16))
        self.radioButton_original.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_original.setObjectName("radioButton_original")
        self.radioButton_maximizar = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_maximizar.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.radioButton_maximizar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_maximizar.setChecked(True)
        self.radioButton_maximizar.setObjectName("radioButton_maximizar")
        self.frame_roi = QtWidgets.QFrame(self.centralwidget)
        self.frame_roi.setGeometry(QtCore.QRect(40, 530, 151, 91))
        self.frame_roi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_roi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_roi.setObjectName("frame_roi")
        self.radioButton_zigzag = QtWidgets.QRadioButton(self.frame_roi)
        self.radioButton_zigzag.setGeometry(QtCore.QRect(10, 70, 77, 25))
        self.radioButton_zigzag.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_zigzag.setChecked(True)
        self.radioButton_zigzag.setObjectName("radioButton_zigzag")
        self.radioButton_espiral = QtWidgets.QRadioButton(self.frame_roi)
        self.radioButton_espiral.setGeometry(QtCore.QRect(90, 70, 77, 25))
        self.radioButton_espiral.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_espiral.setChecked(False)
        self.radioButton_espiral.setObjectName("radioButton_espiral")
        self.pushButton_roi_zigzag = QtWidgets.QPushButton(self.frame_roi)
        self.pushButton_roi_zigzag.setGeometry(QtCore.QRect(10, 0, 131, 61))
        self.pushButton_roi_zigzag.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_roi_zigzag.setObjectName("pushButton_roi_zigzag")
        self.frame_upsampling = QtWidgets.QFrame(self.centralwidget)
        self.frame_upsampling.setGeometry(QtCore.QRect(240, 520, 171, 111))
        self.frame_upsampling.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_upsampling.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upsampling.setObjectName("frame_upsampling")
        self.radioButton_up2x = QtWidgets.QRadioButton(self.frame_upsampling)
        self.radioButton_up2x.setGeometry(QtCore.QRect(40, 80, 83, 16))
        self.radioButton_up2x.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_up2x.setChecked(True)
        self.radioButton_up2x.setObjectName("radioButton_up2x")
        self.radioButton_up4x = QtWidgets.QRadioButton(self.frame_upsampling)
        self.radioButton_up4x.setGeometry(QtCore.QRect(100, 80, 83, 16))
        self.radioButton_up4x.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_up4x.setObjectName("radioButton_up4x")
        self.pushButton_upsampling = QtWidgets.QPushButton(self.frame_upsampling)
        self.pushButton_upsampling.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.pushButton_upsampling.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_upsampling.setObjectName("pushButton_upsampling")
        self.label_tela.raise_()
        self.groupBox_cores.raise_()
        self.pushButton_depthmap.raise_()
        self.pushButton_alldepthmaps.raise_()
        self.l_ang_hoz.raise_()
        self.l_ang_ver.raise_()
        self.label_hist.raise_()
        self.label_text_histograma.raise_()
        self.label_text_minimapa.raise_()
        self.radioButton_red.raise_()
        self.radioButton_green.raise_()
        self.radioButton_blue.raise_()
        self.radioButton_original.raise_()
        self.radioButton_maximizar.raise_()
        self.label_text_exibicao.raise_()
        self.frame_roi.raise_()
        self.frame_upsampling.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setEnabled(True)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.slider_brilho.valueChanged['int'].connect(self.spinBox_brilho.setValue)
        self.spinBox_brilho.valueChanged['int'].connect(self.slider_brilho.setValue)
        self.slider_saturacao.valueChanged['int'].connect(self.spinBox_saturacao.setValue)
        self.spinBox_saturacao.valueChanged['int'].connect(self.slider_saturacao.setValue)
        self.slider_contraste.valueChanged['int'].connect(self.spinBox_contraste.setValue)
        self.spinBox_contraste.valueChanged['int'].connect(self.slider_contraste.setValue)
        self.slider_nitidez.valueChanged['int'].connect(self.spinBox_nitidez.setValue)
        self.spinBox_nitidez.valueChanged['int'].connect(self.slider_nitidez.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LytroFake"))
        self.label_contraste.setText(_translate("MainWindow", "Contrast"))
        self.label_brilho.setText(_translate("MainWindow", "Brightness"))
        self.label_saturacao.setText(_translate("MainWindow", "Saturation"))
        self.label_nitidez.setText(_translate("MainWindow", "Sharpness"))
        self.label_text_cores.setText(_translate("MainWindow", "Colors"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_depthmap.setText(_translate("MainWindow", "DepthMap"))
        self.pushButton_alldepthmaps.setText(_translate("MainWindow", "Disparity"))
        self.l_ang_hoz.setText(_translate("MainWindow", "x:"))
        self.l_ang_ver.setText(_translate("MainWindow", "y:"))
        self.label_text_histograma.setText(_translate("MainWindow", "Histogram"))
        self.label_text_minimapa.setText(_translate("MainWindow", "Minimap"))
        self.radioButton_red.setText(_translate("MainWindow", "Red"))
        self.radioButton_green.setText(_translate("MainWindow", "Green"))
        self.radioButton_blue.setText(_translate("MainWindow", "Blue"))
        self.label_text_exibicao.setText(_translate("MainWindow", "Exhibition"))
        self.radioButton_original.setText(_translate("MainWindow", "Original"))
        self.radioButton_maximizar.setText(_translate("MainWindow", "Maximize"))
        self.radioButton_zigzag.setText(_translate("MainWindow", "ZigZag"))
        self.radioButton_espiral.setText(_translate("MainWindow", "Spiral"))
        self.pushButton_roi_zigzag.setText(_translate("MainWindow", "Region Of\n"
"Interest"))
        self.radioButton_up2x.setText(_translate("MainWindow", "2x"))
        self.radioButton_up4x.setText(_translate("MainWindow", "4x"))
        self.pushButton_upsampling.setText(_translate("MainWindow", "Upsampling"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
