# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KmainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 804)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnDumpPtr = QtWidgets.QPushButton(self.groupBox)
        self.btnDumpPtr.setMinimumSize(QtCore.QSize(0, 40))
        self.btnDumpPtr.setObjectName("btnDumpPtr")
        self.gridLayout_4.addWidget(self.btnDumpPtr, 2, 0, 1, 1)
        self.btnFart = QtWidgets.QPushButton(self.groupBox)
        self.btnFart.setMinimumSize(QtCore.QSize(0, 40))
        self.btnFart.setObjectName("btnFart")
        self.gridLayout_4.addWidget(self.btnFart, 2, 1, 1, 1)
        self.btnDumpDex = QtWidgets.QPushButton(self.groupBox)
        self.btnDumpDex.setMinimumSize(QtCore.QSize(0, 40))
        self.btnDumpDex.setObjectName("btnDumpDex")
        self.gridLayout_4.addWidget(self.btnDumpDex, 2, 2, 1, 1)
        self.btnDumpSo = QtWidgets.QPushButton(self.groupBox)
        self.btnDumpSo.setMinimumSize(QtCore.QSize(0, 40))
        self.btnDumpSo.setObjectName("btnDumpSo")
        self.gridLayout_4.addWidget(self.btnDumpSo, 0, 0, 1, 1)
        self.btnWallbreaker = QtWidgets.QPushButton(self.groupBox)
        self.btnWallbreaker.setMinimumSize(QtCore.QSize(0, 40))
        self.btnWallbreaker.setObjectName("btnWallbreaker")
        self.gridLayout_4.addWidget(self.btnWallbreaker, 0, 1, 1, 1)
        self.btnCallFunction = QtWidgets.QPushButton(self.groupBox)
        self.btnCallFunction.setMinimumSize(QtCore.QSize(0, 40))
        self.btnCallFunction.setObjectName("btnCallFunction")
        self.gridLayout_4.addWidget(self.btnCallFunction, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.chkLibArt = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkLibArt.setObjectName("chkLibArt")
        self.gridLayout_5.addWidget(self.chkLibArt, 0, 6, 1, 1)
        self.chkJavaEnc = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkJavaEnc.setObjectName("chkJavaEnc")
        self.gridLayout_5.addWidget(self.chkJavaEnc, 0, 2, 1, 1)
        self.chkNetwork = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkNetwork.setObjectName("chkNetwork")
        self.gridLayout_5.addWidget(self.chkNetwork, 0, 0, 1, 1)
        self.chkRegisterNative = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkRegisterNative.setObjectName("chkRegisterNative")
        self.gridLayout_5.addWidget(self.chkRegisterNative, 0, 4, 1, 1)
        self.chkSslPining = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkSslPining.setObjectName("chkSslPining")
        self.gridLayout_5.addWidget(self.chkSslPining, 0, 3, 1, 1)
        self.chkJni = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkJni.setObjectName("chkJni")
        self.gridLayout_5.addWidget(self.chkJni, 0, 1, 1, 1)
        self.chkArtMethod = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkArtMethod.setObjectName("chkArtMethod")
        self.gridLayout_5.addWidget(self.chkArtMethod, 0, 5, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMatchMethod = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMatchMethod.setMinimumSize(QtCore.QSize(0, 40))
        self.btnMatchMethod.setObjectName("btnMatchMethod")
        self.horizontalLayout.addWidget(self.btnMatchMethod)
        self.btnNatives = QtWidgets.QPushButton(self.groupBox_2)
        self.btnNatives.setMinimumSize(QtCore.QSize(0, 40))
        self.btnNatives.setObjectName("btnNatives")
        self.horizontalLayout.addWidget(self.btnNatives)
        self.btnStalker = QtWidgets.QPushButton(self.groupBox_2)
        self.btnStalker.setMinimumSize(QtCore.QSize(0, 40))
        self.btnStalker.setObjectName("btnStalker")
        self.horizontalLayout.addWidget(self.btnStalker)
        self.btnTuoke = QtWidgets.QPushButton(self.groupBox_2)
        self.btnTuoke.setMinimumSize(QtCore.QSize(0, 40))
        self.btnTuoke.setObjectName("btnTuoke")
        self.horizontalLayout.addWidget(self.btnTuoke)
        self.btnCustom = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCustom.setEnabled(True)
        self.btnCustom.setMinimumSize(QtCore.QSize(0, 40))
        self.btnCustom.setObjectName("btnCustom")
        self.horizontalLayout.addWidget(self.btnCustom)
        self.btnPatch = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPatch.setEnabled(True)
        self.btnPatch.setMinimumSize(QtCore.QSize(0, 40))
        self.btnPatch.setObjectName("btnPatch")
        self.horizontalLayout.addWidget(self.btnPatch)
        self.gridLayout_7.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupLogs = QtWidgets.QTabWidget(self.tab_2)
        self.groupLogs.setObjectName("groupLogs")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtLogs = QtWidgets.QPlainTextEdit(self.tab_3)
        self.txtLogs.setReadOnly(True)
        self.txtLogs.setObjectName("txtLogs")
        self.gridLayout_3.addWidget(self.txtLogs, 0, 0, 1, 1)
        self.groupLogs.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtoutLogs = QtWidgets.QPlainTextEdit(self.tab_5)
        self.txtoutLogs.setReadOnly(True)
        self.txtoutLogs.setObjectName("txtoutLogs")
        self.gridLayout_2.addWidget(self.txtoutLogs, 0, 0, 1, 1)
        self.groupLogs.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabHooks = QtWidgets.QTableWidget(self.tab_4)
        self.tabHooks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabHooks.setObjectName("tabHooks")
        self.tabHooks.setColumnCount(0)
        self.tabHooks.setRowCount(0)
        self.gridLayout_9.addWidget(self.tabHooks, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.txtSaveHooks = QtWidgets.QLineEdit(self.frame)
        self.txtSaveHooks.setObjectName("txtSaveHooks")
        self.gridLayout_8.addWidget(self.txtSaveHooks, 0, 1, 1, 1)
        self.btnSaveHooks = QtWidgets.QPushButton(self.frame)
        self.btnSaveHooks.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnSaveHooks.setObjectName("btnSaveHooks")
        self.gridLayout_8.addWidget(self.btnSaveHooks, 0, 2, 1, 1)
        self.btnImportHooks = QtWidgets.QPushButton(self.frame)
        self.btnImportHooks.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnImportHooks.setObjectName("btnImportHooks")
        self.gridLayout_8.addWidget(self.btnImportHooks, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 1, 0, 1, 1)
        self.cmbHooks = QtWidgets.QComboBox(self.frame)
        self.cmbHooks.setObjectName("cmbHooks")
        self.gridLayout_8.addWidget(self.cmbHooks, 1, 1, 1, 1)
        self.btnLoadHooks = QtWidgets.QPushButton(self.frame)
        self.btnLoadHooks.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnLoadHooks.setObjectName("btnLoadHooks")
        self.gridLayout_8.addWidget(self.btnLoadHooks, 1, 2, 1, 1)
        self.btnClearHooks = QtWidgets.QPushButton(self.frame)
        self.btnClearHooks.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnClearHooks.setObjectName("btnClearHooks")
        self.gridLayout_8.addWidget(self.btnClearHooks, 1, 3, 1, 1)
        self.gridLayout_9.addWidget(self.frame, 1, 0, 1, 1)
        self.groupLogs.addTab(self.tab_4, "")
        self.gridLayout_6.addWidget(self.groupLogs, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.txtModule = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtModule.setObjectName("txtModule")
        self.gridLayout_10.addWidget(self.txtModule, 0, 0, 1, 1)
        self.listModules = QtWidgets.QListWidget(self.groupBox_3)
        self.listModules.setObjectName("listModules")
        self.gridLayout_10.addWidget(self.listModules, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnExport = QtWidgets.QPushButton(self.tab)
        self.btnExport.setObjectName("btnExport")
        self.verticalLayout.addWidget(self.btnExport)
        self.btnSymbol = QtWidgets.QPushButton(self.tab)
        self.btnSymbol.setObjectName("btnSymbol")
        self.verticalLayout.addWidget(self.btnSymbol)
        self.btnSymbolClear = QtWidgets.QPushButton(self.tab)
        self.btnSymbolClear.setObjectName("btnSymbolClear")
        self.verticalLayout.addWidget(self.btnSymbolClear)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.txtSymbol = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtSymbol.setObjectName("txtSymbol")
        self.gridLayout_12.addWidget(self.txtSymbol, 0, 0, 1, 1)
        self.listSymbol = QtWidgets.QListWidget(self.groupBox_5)
        self.listSymbol.setObjectName("listSymbol")
        self.gridLayout_12.addWidget(self.listSymbol, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.gridLayout_14.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.listClasses = QtWidgets.QListWidget(self.groupBox_4)
        self.listClasses.setObjectName("listClasses")
        self.gridLayout_11.addWidget(self.listClasses, 1, 0, 1, 1)
        self.txtClass = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtClass.setObjectName("txtClass")
        self.gridLayout_11.addWidget(self.txtClass, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnMethod = QtWidgets.QPushButton(self.tab)
        self.btnMethod.setObjectName("btnMethod")
        self.verticalLayout_2.addWidget(self.btnMethod)
        self.btnMethodClear = QtWidgets.QPushButton(self.tab)
        self.btnMethodClear.setObjectName("btnMethodClear")
        self.verticalLayout_2.addWidget(self.btnMethodClear)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.listMethod = QtWidgets.QListWidget(self.groupBox_6)
        self.listMethod.setObjectName("listMethod")
        self.gridLayout_13.addWidget(self.listMethod, 1, 0, 1, 1)
        self.txtMethod = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtMethod.setObjectName("txtMethod")
        self.gridLayout_13.addWidget(self.txtMethod, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.gridLayout_14.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_14.addWidget(self.groupBox_7, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuAttach = QtWidgets.QMenu(self.menuedit)
        self.menuAttach.setObjectName("menuAttach")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionabort = QtWidgets.QAction(MainWindow)
        self.actionabort.setObjectName("actionabort")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionspwan = QtWidgets.QAction(MainWindow)
        self.actionspwan.setObjectName("actionspwan")
        self.actionAttach = QtWidgets.QAction(MainWindow)
        self.actionAttach.setObjectName("actionAttach")
        self.actionAttachName = QtWidgets.QAction(MainWindow)
        self.actionAttachName.setObjectName("actionAttachName")
        self.actionSpawn = QtWidgets.QAction(MainWindow)
        self.actionSpawn.setObjectName("actionSpawn")
        self.actionClearTmp = QtWidgets.QAction(MainWindow)
        self.actionClearTmp.setObjectName("actionClearTmp")
        self.actionClearLogs = QtWidgets.QAction(MainWindow)
        self.actionClearLogs.setObjectName("actionClearLogs")
        self.actionClearOutlog = QtWidgets.QAction(MainWindow)
        self.actionClearOutlog.setObjectName("actionClearOutlog")
        self.actionPushFartSo = QtWidgets.QAction(MainWindow)
        self.actionPushFartSo.setObjectName("actionPushFartSo")
        self.actionClearHookJson = QtWidgets.QAction(MainWindow)
        self.actionClearHookJson.setObjectName("actionClearHookJson")
        self.actionPullDumpDexRes = QtWidgets.QAction(MainWindow)
        self.actionPullDumpDexRes.setObjectName("actionPullDumpDexRes")
        self.actionPushFridaServer = QtWidgets.QAction(MainWindow)
        self.actionPushFridaServer.setObjectName("actionPushFridaServer")
        self.actionPullFartRes = QtWidgets.QAction(MainWindow)
        self.actionPullFartRes.setObjectName("actionPullFartRes")
        self.actionFrida32Start = QtWidgets.QAction(MainWindow)
        self.actionFrida32Start.setObjectName("actionFrida32Start")
        self.actionFrida64Start = QtWidgets.QAction(MainWindow)
        self.actionFrida64Start.setObjectName("actionFrida64Start")
        self.menufile.addAction(self.actionClearTmp)
        self.menufile.addAction(self.actionClearLogs)
        self.menufile.addAction(self.actionClearOutlog)
        self.menufile.addAction(self.actionClearHookJson)
        self.menuAttach.addAction(self.actionAttach)
        self.menuAttach.addAction(self.actionAttachName)
        self.menuAttach.addAction(self.actionSpawn)
        self.menuedit.addAction(self.menuAttach.menuAction())
        self.menuedit.addAction(self.actionStop)
        self.menuedit.addAction(self.actionFrida32Start)
        self.menuedit.addAction(self.actionFrida64Start)
        self.menuhelp.addAction(self.actionabort)
        self.menu.addAction(self.actionPushFridaServer)
        self.menu.addAction(self.actionPushFartSo)
        self.menu.addAction(self.actionPullDumpDexRes)
        self.menu.addAction(self.actionPullFartRes)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.groupLogs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "fridaUiTools"))
        self.groupBox.setTitle(_translate("MainWindow", "功能(附加进程后使用)"))
        self.btnDumpPtr.setText(_translate("MainWindow", "dump指定地址"))
        self.btnFart.setText(_translate("MainWindow", "Fart"))
        self.btnDumpDex.setText(_translate("MainWindow", "dump_dex加载class后调用"))
        self.btnDumpSo.setText(_translate("MainWindow", "dump so"))
        self.btnWallbreaker.setText(_translate("MainWindow", "WallBreaker"))
        self.btnCallFunction.setText(_translate("MainWindow", "函数重放"))
        self.groupBox_2.setTitle(_translate("MainWindow", "hook多选(附加进程前使用)"))
        self.chkLibArt.setText(_translate("MainWindow", "libArt"))
        self.chkJavaEnc.setText(_translate("MainWindow", "java加解密"))
        self.chkNetwork.setText(_translate("MainWindow", "r0capture"))
        self.chkRegisterNative.setText(_translate("MainWindow", "RegisterNative"))
        self.chkSslPining.setText(_translate("MainWindow", "ssl pining"))
        self.chkJni.setText(_translate("MainWindow", "jnitrace"))
        self.chkArtMethod.setText(_translate("MainWindow", "ArtMethod"))
        self.btnMatchMethod.setText(_translate("MainWindow", "ZenTracer"))
        self.btnNatives.setText(_translate("MainWindow", "批量native"))
        self.btnStalker.setText(_translate("MainWindow", "stalker"))
        self.btnTuoke.setText(_translate("MainWindow", "脱壳"))
        self.btnCustom.setText(_translate("MainWindow", "自定义"))
        self.btnPatch.setText(_translate("MainWindow", "Patch"))
        self.groupLogs.setTabText(self.groupLogs.indexOf(self.tab_3), _translate("MainWindow", "操作日志"))
        self.groupLogs.setTabText(self.groupLogs.indexOf(self.tab_5), _translate("MainWindow", "输出日志"))
        self.label.setText(_translate("MainWindow", "别名："))
        self.btnSaveHooks.setText(_translate("MainWindow", "保存列表"))
        self.btnImportHooks.setText(_translate("MainWindow", "导入JSON"))
        self.label_2.setText(_translate("MainWindow", "别名："))
        self.btnLoadHooks.setText(_translate("MainWindow", "加载记录"))
        self.btnClearHooks.setText(_translate("MainWindow", "清空列表"))
        self.groupLogs.setTabText(self.groupLogs.indexOf(self.tab_4), _translate("MainWindow", "当前hook列表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "主界面"))
        self.groupBox_3.setTitle(_translate("MainWindow", "module列表"))
        self.btnExport.setText(_translate("MainWindow", "Export"))
        self.btnSymbol.setText(_translate("MainWindow", "Symbol"))
        self.btnSymbolClear.setText(_translate("MainWindow", "清空"))
        self.groupBox_5.setTitle(_translate("MainWindow", "符号"))
        self.groupBox_4.setTitle(_translate("MainWindow", "java类列表"))
        self.btnMethod.setText(_translate("MainWindow", "查询函数"))
        self.btnMethodClear.setText(_translate("MainWindow", "清空"))
        self.groupBox_6.setTitle(_translate("MainWindow", "java函数"))
        self.groupBox_7.setTitle(_translate("MainWindow", "其他信息（todo）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "应用信息"))
        self.menufile.setTitle(_translate("MainWindow", "文件"))
        self.menuedit.setTitle(_translate("MainWindow", "执行"))
        self.menuAttach.setTitle(_translate("MainWindow", "附加进程"))
        self.menuhelp.setTitle(_translate("MainWindow", "帮助"))
        self.menu.setTitle(_translate("MainWindow", "上传与下载"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionabort.setText(_translate("MainWindow", "关于我"))
        self.actionStop.setText(_translate("MainWindow", "停止"))
        self.action.setText(_translate("MainWindow", "附加当前进程"))
        self.action_2.setText(_translate("MainWindow", "附加指定进程"))
        self.actionspwan.setText(_translate("MainWindow", "spwan附加"))
        self.actionAttach.setText(_translate("MainWindow", "附加当前进程"))
        self.actionAttachName.setText(_translate("MainWindow", "附加指定进程"))
        self.actionSpawn.setText(_translate("MainWindow", "spawn附加"))
        self.actionClearTmp.setText(_translate("MainWindow", "清空缓存数据"))
        self.actionClearLogs.setText(_translate("MainWindow", "清空日志文件"))
        self.actionClearOutlog.setText(_translate("MainWindow", "清空输出日志"))
        self.actionPushFartSo.setText(_translate("MainWindow", "上传fart.so到设备"))
        self.actionClearHookJson.setText(_translate("MainWindow", "清空json列表"))
        self.actionPullDumpDexRes.setText(_translate("MainWindow", "下载dump_dex结果"))
        self.actionPushFridaServer.setText(_translate("MainWindow", "上传frida-server-14-2"))
        self.actionPullFartRes.setText(_translate("MainWindow", "下载fart脱壳结果"))
        self.actionFrida32Start.setText(_translate("MainWindow", "启动frida-server for 32"))
        self.actionFrida64Start.setText(_translate("MainWindow", "启动frida-server for 64"))

