# Form implementation generated from reading ui file 'testing_vote.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 530)
        MainWindow.setMinimumSize(QtCore.QSize(680, 530))
        MainWindow.setMaximumSize(QtCore.QSize(680, 530))
        font = QtGui.QFont()
        font.setFamily("Tiro Bangla")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(130, 15, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.halloween_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.halloween_image.setEnabled(True)
        self.halloween_image.setGeometry(QtCore.QRect(10, 80, 171, 191))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.halloween_image.setFont(font)
        self.halloween_image.setText("")
        self.halloween_image.setPixmap(QtGui.QPixmap("pumpkin.png"))
        self.halloween_image.setScaledContents(True)
        self.halloween_image.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.halloween_image.setObjectName("halloween_image")
        self.christmas_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.christmas_image.setGeometry(QtCore.QRect(300, 60, 161, 211))
        self.christmas_image.setText("")
        self.christmas_image.setPixmap(QtGui.QPixmap("tree.png"))
        self.christmas_image.setScaledContents(True)
        self.christmas_image.setObjectName("christmas_image")
        self.left_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.left_label.setGeometry(QtCore.QRect(60, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.left_label.setFont(font)
        self.left_label.setText("")
        self.left_label.setObjectName("left_label")
        self.vote_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vote_button.setGeometry(QtCore.QRect(175, 440, 91, 41))
        self.vote_button.setObjectName("vote_button")
        self.right_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.right_label.setGeometry(QtCore.QRect(350, 281, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.right_label.setFont(font)
        self.right_label.setText("")
        self.right_label.setObjectName("right_label")
        self.or_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.or_label.setGeometry(QtCore.QRect(210, 280, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.or_label.setFont(font)
        self.or_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.or_label.setObjectName("or_label")
        self.user_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(15, 450, 151, 21))
        self.user_input.setObjectName("user_input")
        self.typebelow_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.typebelow_label.setGeometry(QtCore.QRect(15, 420, 91, 21))
        self.typebelow_label.setObjectName("typebelow_label")
        self.reset_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tiro Bangla")
        self.reset_button.setFont(font)
        self.reset_button.setAutoFillBackground(False)
        self.reset_button.setObjectName("reset_button")
        self.vote_message_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.vote_message_label.setGeometry(QtCore.QRect(140, 370, 171, 61))
        self.vote_message_label.setText("")
        self.vote_message_label.setObjectName("vote_message_label")
        self.results_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.results_button.setGeometry(QtCore.QRect(275, 440, 151, 41))
        self.results_button.setObjectName("results_button")
        self.results_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.results_label.setGeometry(QtCore.QRect(430, 320, 241, 161))
        self.results_label.setText("")
        self.results_label.setObjectName("results_label")
        self.exception_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.exception_label.setGeometry(QtCore.QRect(20, 330, 311, 81))
        self.exception_label.setText("")
        self.exception_label.setObjectName("exception_label")
        self.holiday_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.holiday_button.setGeometry(QtCore.QRect(550, 70, 191, 20))
        self.holiday_button.setObjectName("holiday_button")
        self.season_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.season_button.setGeometry(QtCore.QRect(550, 100, 191, 20))
        self.season_button.setObjectName("season_button")
        self.sun_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.sun_image.setEnabled(True)
        self.sun_image.setGeometry(QtCore.QRect(10, 90, 191, 181))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sun_image.setFont(font)
        self.sun_image.setText("")
        self.sun_image.setPixmap(QtGui.QPixmap("sun.png"))
        self.sun_image.setScaledContents(True)
        self.sun_image.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.sun_image.setObjectName("sun_image")
        self.snowman_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.snowman_image.setGeometry(QtCore.QRect(290, 60, 181, 211))
        self.snowman_image.setText("")
        self.snowman_image.setPixmap(QtGui.QPixmap("snowman.png"))
        self.snowman_image.setScaledContents(True)
        self.snowman_image.setObjectName("snowman_image")
        self.poll_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.poll_image.setGeometry(QtCore.QRect(110, 110, 271, 241))
        self.poll_image.setText("")
        self.poll_image.setPixmap(QtGui.QPixmap("poll.png"))
        self.poll_image.setScaledContents(True)
        self.poll_image.setObjectName("poll_image")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 50, 121, 16))
        self.label.setObjectName("label")
        self.instructions_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.instructions_label.setGeometry(QtCore.QRect(480, 160, 191, 91))
        self.instructions_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.instructions_label.setWordWrap(True)
        self.instructions_label.setObjectName("instructions_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting Menu"))
        self.title_label.setText(_translate("MainWindow", "Voting Menu - Select a Poll!"))
        self.vote_button.setText(_translate("MainWindow", "VOTE"))
        self.or_label.setText(_translate("MainWindow", "OR"))
        self.typebelow_label.setText(_translate("MainWindow", "Type Below:"))
        self.reset_button.setText(_translate("MainWindow", "RESET DATA"))
        self.results_button.setText(_translate("MainWindow", "SHOW RESULTS"))
        self.holiday_button.setText(_translate("MainWindow", "Holidays"))
        self.season_button.setText(_translate("MainWindow", "Seasons"))
        self.label.setText(_translate("MainWindow", "Select Below:"))
        self.instructions_label.setText(_translate("MainWindow", "Welcome to the voting menu! Select the options above and start voting!"))


