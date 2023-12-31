

from PyQt5 import QtCore, QtGui, QtWidgets
from preprocessing import *
from userend import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(40, 20, 981, 141))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        self.titlelabel.setFont(font)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setWordWrap(True)
        self.titlelabel.setObjectName("titlelabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 180, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.user_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.user_ip.setGeometry(QtCore.QRect(400, 170, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.user_ip.setFont(font)
        self.user_ip.setObjectName("user_ip")
        self.preproc_button = QtWidgets.QPushButton(self.centralwidget)
        self.preproc_button.setGeometry(QtCore.QRect(400, 320, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.preproc_button.setFont(font)
        self.preproc_button.setObjectName("preproc_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 410, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.preprocess_op = QtWidgets.QLabel(self.centralwidget)
        self.preprocess_op.setGeometry(QtCore.QRect(400, 390, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.preprocess_op.setFont(font)
        self.preprocess_op.setFrameShape(QtWidgets.QFrame.Box)
        self.preprocess_op.setText("")
        self.preprocess_op.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.preprocess_op.setWordWrap(True)
        self.preprocess_op.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.preprocess_op.setObjectName("preprocess_op")
        self.preprocess_op_2 = QtWidgets.QLabel(self.centralwidget)
        self.preprocess_op_2.setGeometry(QtCore.QRect(400, 540, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.preprocess_op_2.setFont(font)
        self.preprocess_op_2.setFrameShape(QtWidgets.QFrame.Box)
        self.preprocess_op_2.setText("")
        self.preprocess_op_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.preprocess_op_2.setWordWrap(True)
        self.preprocess_op_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.preprocess_op_2.setObjectName("preprocess_op_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 560, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.run_class_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_class_button.setGeometry(QtCore.QRect(400, 700, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.run_class_button.setFont(font)
        self.run_class_button.setObjectName("run_class_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.preproc_button.clicked.connect(self.preproc_click)
        #self.run_class_button.clicked.connect(self.run_click)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titlelabel.setText(_translate("MainWindow", "Word Sense Disambiguation using Neural Networks"))
        self.label_2.setText(_translate("MainWindow", "Enter Input Text:"))
        self.preproc_button.setText(_translate("MainWindow", "PREPROCESS"))
        self.label_3.setText(_translate("MainWindow", "Preprocessed Word List:"))
        self.label_4.setText(_translate("MainWindow", "Ambiguous Word List:"))
        self.run_class_button.setText(_translate("MainWindow", "RUN CLASSIFIER ON WORDS"))

    def run_click(self):
        exec(open("WSD_UI_1_2.py").read())
        
    def preproc_click(self):
        ipsent=self.user_ip.toPlainText()
        wordlist=preprocess(ipsent)
        wlist=""
        for i in wordlist:
            wlist=wlist+i+", "
        self.preprocess_op.setText(wlist)
        awords=findambiwords(wordlist)
        alist=""
        for i in awords:
            alist=alist+i+", "
        self.preprocess_op_2.setText(alist)
        
        
if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


