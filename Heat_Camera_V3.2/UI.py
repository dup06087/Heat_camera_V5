from PyQt5 import QtCore, QtGui, QtWidgets

import Server
import initial_data
from Cam_number import camera_num


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.Outer_Layout = QtWidgets.QGridLayout()
        self.Outer_Layout.setSpacing(0)
        self.Outer_Layout.setContentsMargins(0,0,0,0)
        # self.Outer_Layout.setMargin(0)
        self.Outer_Layout.setObjectName("Outer_Layout")

        self.Line1 = QtWidgets.QHBoxLayout()
        self.Line1.setObjectName("Line1")
        self.Line2 = QtWidgets.QHBoxLayout()
        self.Line2.setObjectName("Line2")
        self.Line3 = QtWidgets.QHBoxLayout()
        self.Line3.setObjectName("Line3")
        self.Line4 = QtWidgets.QHBoxLayout()
        self.Line4.setObjectName("Line4")


        self.CAM_Layout = []
        self.CAM_LHP = []


        self.btn1 = QtWidgets.QPushButton()
        self.btn2 = QtWidgets.QPushButton()
        self.btn3 = QtWidgets.QPushButton()
        self.btn4 = QtWidgets.QPushButton()
        self.btn5 = QtWidgets.QPushButton()
        self.btn6 = QtWidgets.QPushButton()
        self.btn7 = QtWidgets.QPushButton()
        self.btn8 = QtWidgets.QPushButton()
        self.btn9 = QtWidgets.QPushButton()
        self.btn10 = QtWidgets.QPushButton()
        self.btn11 = QtWidgets.QPushButton()
        self.btn12 = QtWidgets.QPushButton()
        self.btn13 = QtWidgets.QPushButton()
        self.btn14 = QtWidgets.QPushButton()
        self.btn15 = QtWidgets.QPushButton()
        self.btn16 = QtWidgets.QPushButton()
        self.lbl_CAM_Num = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16]
        self.chart = []
        self.CAM_RHP = []
        self.lbl_prob_chk = []
        self.lbl_temp = []
        self.lbl_volt1 = []
        self.lbl_volt2 = []
        self.lbl_current = []
        self.scrollArea = []
        self.scroll_layout = []
        self.status = []
        self.status_label = []

        self.btn1.clicked.connect(lambda: self.buttonClick(self.btn1))  ### push button클릭시 번호
        self.btn2.clicked.connect(lambda: self.buttonClick(self.btn2))  ### push button클릭시 번호
        self.btn3.clicked.connect(lambda: self.buttonClick(self.btn3))  ### push button클릭시 번호
        self.btn4.clicked.connect(lambda: self.buttonClick(self.btn4))  ### push button클릭시 번호

        self.btn5.clicked.connect(lambda: self.buttonClick(self.btn5))  ### push button클릭시 번호
        self.btn6.clicked.connect(lambda: self.buttonClick(self.btn6))  ### push button클릭시 번호
        self.btn7.clicked.connect(lambda: self.buttonClick(self.btn7))  ### push button클릭시 번호
        self.btn8.clicked.connect(lambda: self.buttonClick(self.btn8))  ### push button클릭시 번호

        self.btn9.clicked.connect(lambda: self.buttonClick(self.btn9))  ### push button클릭시 번호
        self.btn10.clicked.connect(lambda: self.buttonClick(self.btn10))  ### push button클릭시 번호
        self.btn11.clicked.connect(lambda: self.buttonClick(self.btn11))  ### push button클릭시 번호
        self.btn12.clicked.connect(lambda: self.buttonClick(self.btn12))  ### push button클릭시 번호

        self.btn13.clicked.connect(lambda: self.buttonClick(self.btn13))  ### push button클릭시 번호
        self.btn14.clicked.connect(lambda: self.buttonClick(self.btn14))  ### push button클릭시 번호
        self.btn15.clicked.connect(lambda: self.buttonClick(self.btn15))  ### push button클릭시 번호
        self.btn16.clicked.connect(lambda: self.buttonClick(self.btn16))  ### push button클릭시 번호

        for i in range(camera_num):

            self.CAM_Layout.append(QtWidgets.QHBoxLayout())
            self.CAM_Layout[i].setSpacing(0)
            # self.CAM_Layout[i].setMargin(0)
            self.CAM_Layout[i].setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            self.CAM_Layout[i].setObjectName("CAM{num}_Layout".format(num=i))
            self.CAM_LHP.append(QtWidgets.QVBoxLayout())
            self.CAM_Layout[i].setSpacing(0)
            self.CAM_Layout[i].setContentsMargins(0,0,0,0)
            self.CAM_LHP[i].setObjectName("CAM{num}_LHP".format(num = i))


            ### cam label
            # self.lbl_CAM_Num.append()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            self.lbl_CAM_Num[i].setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.lbl_CAM_Num[i].setFont(font)
            self.lbl_CAM_Num[i].setAccessibleName("{}".format(i))
            self.lbl_CAM_Num[i].setObjectName("lbl_CAM_Num{num}".format(num = i))
            self.CAM_LHP[i].addWidget(self.lbl_CAM_Num[i])

            #cam label end
            # self.lbl_CAM_Num[i].clicked.connect(self.show_new_window)

            #canvas
            self.chart.append(QtWidgets.QVBoxLayout())
            try:
                self.chart[i].addWidget(Server.canvas[i])
                # self.chart[i].addWidget(.canvas[i])
                self.chart[i].setSpacing(0)
                self.chart[i].setContentsMargins(0,0,0,0)
                self.chart[i].setObjectName("chart{num}".format(num = i))
                self.CAM_LHP[i].addLayout(self.chart[i])
                self.CAM_Layout[i].addLayout(self.CAM_LHP[i])
            except:
                # print("drawing fail2 : ", i)
                pass

            self.CAM_RHP.append(QtWidgets.QVBoxLayout())
            self.CAM_RHP[i].setObjectName("CAM_RHP{num}".format(num = i))
            self.lbl_prob_chk.append(QtWidgets.QLabel(self.centralwidget))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            # sizePolicy.setHeightForWidth(self.lbl_prob_chk[i].sizePolicy().hasHeightForWidth())
            self.lbl_prob_chk[i].setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(13)
            self.lbl_prob_chk[i].setFont(font)
            self.lbl_prob_chk[i].setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lbl_prob_chk[i].setFrameShape(QtWidgets.QFrame.WinPanel)
            self.lbl_prob_chk[i].setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_prob_chk[i].setObjectName("lbl_prob_chk{num}".format(num = i))
            self.CAM_RHP[i].addWidget(self.lbl_prob_chk[i])

            ### 밑에부터 scroll area

            self.scrollArea.append(QtWidgets.QScrollArea()) ##스크롤 영역 생성
            self.scrollArea[i].setWidgetResizable(True)
            self.scroll_layout.append(QtWidgets.QVBoxLayout()) ## 스크롤 넣을 layout >>> scroll
            initial_value = QtWidgets.QLabel("No_signal\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.status_label.append(initial_value) ### 동적으로 초기화가 안 됨


            font_status = QtGui.QFont()
            font_status.setPointSize(15)
            self.status_label[i].setFont(font_status)
            self.status.append(self.status_label[i]) ### scroll >>> Qlabel
            self.scrollArea[i].setWidget(self.status[i])
            self.scroll_layout[i].addWidget(self.scrollArea[i])
            self.CAM_RHP[i].addLayout(self.scroll_layout[i])

            self.CAM_Layout[i].addLayout(self.CAM_RHP[i])
            self.CAM_Layout[i].setStretch(0, 3)
            self.CAM_Layout[i].setStretch(1, 1)

            if camera_num - 1 < 4:
                list_x = [0,0,1,1]
                list_y = [0,1,0,1]
                self.Outer_Layout.addLayout(self.CAM_Layout[i], list_x[i], list_y[i])

            elif camera_num - 1 < 9:
                list_x = [0,0,0,1,1,1,2,2,2]
                list_y = [0,1,2,0,1,2,0,1,2]
                self.Outer_Layout.addLayout(self.CAM_Layout[i], list_x[i], list_y[i])

            else:
                list_x = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
                list_y = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
                self.Outer_Layout.addLayout(self.CAM_Layout[i], list_x[i], list_y[i])

        self.gridLayout.addLayout(self.Outer_Layout, 0, 0)

        self.Tool_Bar = QtWidgets.QVBoxLayout()
        self.Tool_Bar.setSpacing(0)
        self.Tool_Bar.setContentsMargins(0,0,0,0)
        # self.Outer_Layout.setMargin(0)
        self.Tool_Bar.setObjectName("ToolBar")

        self.lbl_logo = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(initial_data.init_Logo_Location)
        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio) ### tool bar width
        self.lbl_logo.setPixmap(QtGui.QPixmap(pixmap))
        self.Tool_Bar.addWidget(self.lbl_logo)


        ## tool bar : settings
        self.set = QtWidgets.QPushButton()
        self.set.setText("Settings")
        self.set.clicked.connect(self.open_settings)

        self.Tool_Bar.addWidget(self.set)

        ## tool bar : addstretch
        self.Tool_Bar.addStretch()

        self.gridLayout.addLayout(self.Tool_Bar, 0, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtWidgets.QApplication.processEvents()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Form = QtWidgets.QWidget()
        self.child = Ui_Form()
        self.child.setupUi(self.Form)

        QtWidgets.QApplication.processEvents()
        MainWindow.ui=None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "전력제어반 이상 모니터링 시스템"))
        MainWindow.setWindowIcon(QtGui.QIcon("Window_Icon.png"))
        for i in range(camera_num):
            self.lbl_CAM_Num[i].setText(_translate("MainWindow", "CAM{num}".format(num = i + 1)))
            self.lbl_prob_chk[i].setText(_translate("MainWindow", "문제 발생"))

    def buttonClick(self, button):

        for i in range(camera_num):
            if self.lbl_CAM_Num[i] == button:
                # print("index = ", i)
                self.clicked_num = i

        if MainWindow.ui is None:
            MainWindow.ui = AnotherWindow()
        if MainWindow.ui is not None:
            MainWindow.ui.__init__()

        MainWindow.ui.show()

    def open_settings(self):
        self.Form.show()

class AnotherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWindowTitle(initial_data.Cam_names[ui.clicked_num]) ##########################################################
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.CAM1_Layout_2 = QtWidgets.QHBoxLayout()
        self.CAM1_Layout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.CAM1_Layout_2.setObjectName("CAM1_Layout_2")
        self.CAM1_LHP_2 = QtWidgets.QVBoxLayout()
        self.CAM1_LHP_2.setObjectName("CAM1_LHP_2")

        ### cam label

        self.lbl_CAM_Num_2 = QtWidgets.QLabel() ###
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.lbl_CAM_Num_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_CAM_Num_2.setFont(font)
        self.lbl_CAM_Num_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_CAM_Num_2.setObjectName("lbl_CAM_Num_2")
        self.CAM1_LHP_2.addWidget(self.lbl_CAM_Num_2)

        ###cam label end
        self.chart1_2 = QtWidgets.QVBoxLayout()
        self.chart1_2.setObjectName("chart1_2")
        self.chart1_2.addWidget(Server.child_canvas[ui.clicked_num])
        # self.chart1_2.addWidget(main_threadings.child_canvas)
        self.CAM1_LHP_2.addLayout(self.chart1_2)
        self.CAM1_Layout_2.addLayout(self.CAM1_LHP_2)


        self.CAM2_RHP_2 = QtWidgets.QVBoxLayout()
        self.CAM2_RHP_2.setObjectName("CAM2_RHP_2")
        self.lbl_prob_chk_2 = QtWidgets.QLabel() ###
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_prob_chk_2.sizePolicy().hasHeightForWidth())
        self.lbl_prob_chk_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_prob_chk_2.setFont(font)
        self.lbl_prob_chk_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_prob_chk_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbl_prob_chk_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_prob_chk_2.setObjectName("lbl_prob_chk_2")

        _translate = QtCore.QCoreApplication.translate
        self.lbl_prob_chk_2.setText(_translate("Mainwindow", "문제 발생"))

        self.CAM2_RHP_2.addWidget(self.lbl_prob_chk_2)

        self.scrollArea = QtWidgets.QScrollArea()  ##스크롤 영역 생성
        self.scrollArea.setWidgetResizable(True)
        self.scroll_layout =QtWidgets.QVBoxLayout()  ## 스크롤 넣을 layout >>> scroll
        self.initial_value = QtWidgets.QLabel("No_signal\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.status_label = self.initial_value  ### 동적으로 초기화가 안 됨

        font_status = QtGui.QFont()
        font_status.setPointSize(15)
        self.status_label.setFont(font_status)
        self.status = self.status_label  ### scroll >>> Qlabel
        self.scrollArea.setWidget(self.status)
        self.scroll_layout.addWidget(self.scrollArea)
        self.CAM2_RHP_2.addLayout(self.scroll_layout)

        self.CAM1_Layout_2.addLayout(self.CAM2_RHP_2)
        self.CAM1_Layout_2.setStretch(0, 3)
        self.CAM1_Layout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.CAM1_Layout_2)
        self.setLayout(self.verticalLayout)

        # quit.triggered.connect(self.close_window)
        ###새로

        # self.label = QtWidgets.QLabel("another window") ###원래 있던 것
        # layout.addWidget(self.label) ### 원래 있던 것
        # self.setLayout(layout) ### 원래 있던 것

        # MainWindow.closeEvent()

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif e.key() == QtCore.Qt.Key_F:
            self.showFullScreen()
        elif e.key() == QtCore.Qt.Key_N:
            self.showNormal()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 501)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab1_scrollArea = QtWidgets.QScrollArea(self.tab1)
        self.tab1_scrollArea.setWidgetResizable(True)
        self.tab1_scrollArea.setObjectName("tab1_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 734, 718))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tab1_verticalLayout = QtWidgets.QVBoxLayout()
        self.tab1_verticalLayout.setObjectName("tab1_verticalLayout")
        # self.tab1_verticalLayout.setSpacing(0)

        self.lbl_cam1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam1.sizePolicy().hasHeightForWidth())
        self.lbl_cam1.setSizePolicy(sizePolicy)
        self.lbl_cam1.setObjectName("lbl_cam1")
        self.tab1_verticalLayout.addWidget(self.lbl_cam1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.tab1_verticalLayout.addWidget(self.lineEdit_1)
        self.lbl_cam2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam2.sizePolicy().hasHeightForWidth())
        self.lbl_cam2.setSizePolicy(sizePolicy)
        self.lbl_cam2.setObjectName("lbl_cam2")
        self.tab1_verticalLayout.addWidget(self.lbl_cam2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tab1_verticalLayout.addWidget(self.lineEdit_2)
        self.lbl_cam3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam3.sizePolicy().hasHeightForWidth())
        self.lbl_cam3.setSizePolicy(sizePolicy)
        self.lbl_cam3.setObjectName("lbl_cam3")
        self.tab1_verticalLayout.addWidget(self.lbl_cam3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tab1_verticalLayout.addWidget(self.lineEdit_3)
        self.lbl_cam4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam4.sizePolicy().hasHeightForWidth())
        self.lbl_cam4.setSizePolicy(sizePolicy)
        self.lbl_cam4.setObjectName("lbl_cam4")
        self.tab1_verticalLayout.addWidget(self.lbl_cam4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tab1_verticalLayout.addWidget(self.lineEdit_4)
        self.lbl_cam5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam5.sizePolicy().hasHeightForWidth())
        self.lbl_cam5.setSizePolicy(sizePolicy)
        self.lbl_cam5.setObjectName("lbl_cam5")
        self.tab1_verticalLayout.addWidget(self.lbl_cam5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.tab1_verticalLayout.addWidget(self.lineEdit_5)
        self.lbl_cam6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam6.sizePolicy().hasHeightForWidth())
        self.lbl_cam6.setSizePolicy(sizePolicy)
        self.lbl_cam6.setObjectName("lbl_cam6")
        self.tab1_verticalLayout.addWidget(self.lbl_cam6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tab1_verticalLayout.addWidget(self.lineEdit_6)
        self.lbl_cam7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam7.sizePolicy().hasHeightForWidth())
        self.lbl_cam7.setSizePolicy(sizePolicy)
        self.lbl_cam7.setObjectName("lbl_cam7")
        self.tab1_verticalLayout.addWidget(self.lbl_cam7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tab1_verticalLayout.addWidget(self.lineEdit_7)
        self.lbl_cam8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam8.sizePolicy().hasHeightForWidth())
        self.lbl_cam8.setSizePolicy(sizePolicy)
        self.lbl_cam8.setObjectName("lbl_cam8")
        self.tab1_verticalLayout.addWidget(self.lbl_cam8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.tab1_verticalLayout.addWidget(self.lineEdit_8)
        self.lbl_cam9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam9.sizePolicy().hasHeightForWidth())
        self.lbl_cam9.setSizePolicy(sizePolicy)
        self.lbl_cam9.setObjectName("lbl_cam9")
        self.tab1_verticalLayout.addWidget(self.lbl_cam9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.tab1_verticalLayout.addWidget(self.lineEdit_9)
        self.lbl_cam10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam10.sizePolicy().hasHeightForWidth())
        self.lbl_cam10.setSizePolicy(sizePolicy)
        self.lbl_cam10.setObjectName("lbl_cam10")
        self.tab1_verticalLayout.addWidget(self.lbl_cam10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.tab1_verticalLayout.addWidget(self.lineEdit_10)
        self.lbl_cam11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam11.sizePolicy().hasHeightForWidth())
        self.lbl_cam11.setSizePolicy(sizePolicy)
        self.lbl_cam11.setObjectName("lbl_cam11")
        self.tab1_verticalLayout.addWidget(self.lbl_cam11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.tab1_verticalLayout.addWidget(self.lineEdit_11)
        self.lbl_cam12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam12.sizePolicy().hasHeightForWidth())
        self.lbl_cam12.setSizePolicy(sizePolicy)
        self.lbl_cam12.setObjectName("lbl_cam12")
        self.tab1_verticalLayout.addWidget(self.lbl_cam12)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.tab1_verticalLayout.addWidget(self.lineEdit_12)
        self.lbl_cam13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam13.sizePolicy().hasHeightForWidth())
        self.lbl_cam13.setSizePolicy(sizePolicy)
        self.lbl_cam13.setObjectName("lbl_cam13")
        self.tab1_verticalLayout.addWidget(self.lbl_cam13)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.tab1_verticalLayout.addWidget(self.lineEdit_13)
        self.lbl_cam14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam14.sizePolicy().hasHeightForWidth())
        self.lbl_cam14.setSizePolicy(sizePolicy)
        self.lbl_cam14.setObjectName("lbl_cam14")
        self.tab1_verticalLayout.addWidget(self.lbl_cam14)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.tab1_verticalLayout.addWidget(self.lineEdit_14)
        self.lbl_cam15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam15.sizePolicy().hasHeightForWidth())
        self.lbl_cam15.setSizePolicy(sizePolicy)
        self.lbl_cam15.setObjectName("lbl_cam15")
        self.tab1_verticalLayout.addWidget(self.lbl_cam15)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.tab1_verticalLayout.addWidget(self.lineEdit_15)
        self.lbl_cam16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lbl_cam16.sizePolicy().hasHeightForWidth())
        self.lbl_cam16.setSizePolicy(sizePolicy)
        self.lbl_cam16.setObjectName("lbl_cam16")
        self.tab1_verticalLayout.addWidget(self.lbl_cam16)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.tab1_verticalLayout.addWidget(self.lineEdit_16)
        self.Empty_space = QtWidgets.QLabel()
        self.tab1_verticalLayout.addWidget(self.Empty_space)
        self.verticalLayout_5.addLayout(self.tab1_verticalLayout)

        self.tab1_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.tab1_scrollArea)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tab_2_verticalLayout = QtWidgets.QVBoxLayout()
        self.tab_2_verticalLayout.setObjectName("tab_2_verticalLayout")
        self.lbl_Logo = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Logo.sizePolicy().hasHeightForWidth())
        self.lbl_Logo.setSizePolicy(sizePolicy)
        self.lbl_Logo.setObjectName("lbl_Logo")
        self.tab_2_verticalLayout.addWidget(self.lbl_Logo)
        self.lineEdit_URL = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_URL.setObjectName("lineEdit_URL")
        self.tab_2_verticalLayout.addWidget(self.lineEdit_URL)
        self.horizontalLayout_FileOpen = QtWidgets.QHBoxLayout()
        self.horizontalLayout_FileOpen.setObjectName("horizontalLayout_FileOpen")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_FileOpen.addItem(spacerItem)

        self.Btn_File_Open = QtWidgets.QPushButton(self.tab_2)
        self.Btn_File_Open.setObjectName("Btn_File_Open")
        self.Btn_File_Open.clicked.connect(self.URL_get_clicked)

        self.horizontalLayout_FileOpen.addWidget(self.Btn_File_Open)
        self.tab_2_verticalLayout.addLayout(self.horizontalLayout_FileOpen)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tab_2_verticalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.tab_2_verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        ### button ok, cancle
        self.buttonBox.accepted.connect(lambda : self.change_cam_label())
        self.buttonBox.rejected.connect(Form.close)

        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.cam_LineEdit = [self.lineEdit_1, self.lineEdit_2,self.lineEdit_3,self.lineEdit_4,self.lineEdit_5,self.lineEdit_6,self.lineEdit_7,self.lineEdit_8,self.lineEdit_9,self.lineEdit_10,
                             self.lineEdit_11,self.lineEdit_12,self.lineEdit_13,self.lineEdit_14,self.lineEdit_15,self.lineEdit_16]
        self.cam_LineEdit_Text=["CAM{}".format(i) for i in range((camera_num))]

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        for i in range(camera_num):
            self.cam_LineEdit[i].setText(initial_data.Cam_names[i])

        self.lineEdit_URL.setText(_translate("Form", initial_data.init_Logo_Location))
        self.lbl_cam1.setText(_translate("Form", "CAM1"))
        self.lbl_cam2.setText(_translate("Form", "CAM2"))
        self.lbl_cam3.setText(_translate("Form", "CAM3"))
        self.lbl_cam4.setText(_translate("Form", "CAM4"))
        self.lbl_cam5.setText(_translate("Form", "CAM5"))
        self.lbl_cam6.setText(_translate("Form", "CAM6"))
        self.lbl_cam7.setText(_translate("Form", "CAM7"))
        self.lbl_cam8.setText(_translate("Form", "CAM8"))
        self.lbl_cam9.setText(_translate("Form", "CAM9"))
        self.lbl_cam10.setText(_translate("Form", "CAM10"))
        self.lbl_cam11.setText(_translate("Form", "CAM11"))
        self.lbl_cam12.setText(_translate("Form", "CAM12"))
        self.lbl_cam13.setText(_translate("Form", "CAM13"))
        self.lbl_cam14.setText(_translate("Form", "CAM14"))
        self.lbl_cam15.setText(_translate("Form", "CAM15"))
        self.lbl_cam16.setText(_translate("Form", "CAM16"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "CAM name"))
        self.lbl_Logo.setText(_translate("Form", "Logo 위치"))
        self.Btn_File_Open.setText(_translate("Form", "File Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Logo"))

    def change_cam_label(self):
        _translate = QtCore.QCoreApplication.translate
        for i in range(camera_num):
            if not self.cam_LineEdit[i].text() == "":
                self.cam_LineEdit_Text[i] = self.cam_LineEdit[i].text()
                ### txt open and write and save

                ui.lbl_CAM_Num[i].setText(_translate("Form", self.cam_LineEdit_Text[i]))

        with open('cam_names.txt', 'w') as f:
            f.writelines("\n".join(self.cam_LineEdit_Text))
            f.close()

        with open('URL.txt', 'w') as f:
            new_url = self.lineEdit_URL.text()
            f.writelines(new_url)
            f.close()
        self.lineEdit_URL.setText(_translate("Form", new_url))

        ui.pixmap = QtGui.QPixmap(new_url)
        ui.pixmap = ui.pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio) ### tool bar width
        ui.lbl_logo.setPixmap(QtGui.QPixmap(ui.pixmap))

    def URL_get_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        Url = QtWidgets.QFileDialog.getOpenFileName()
        # print(Url)

        f = open("URL.txt", 'w')
        f.write(Url[0])
        f.close()
        self.lineEdit_URL.setText(_translate("Form", Url[0]))
        self.change_cam_label()
        # self.change_cam_label()

# if __name__ == "__main__":
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.child.change_cam_label()
MainWindow.show()
# sys.exit(app.exec_()) # 이거하면 이 뒤로 안 먹음