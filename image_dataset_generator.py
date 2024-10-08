from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import os
import PIL
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
import numpy as np
import scipy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 765)
        MainWindow.setMinimumSize(QtCore.QSize(887, 765))
        MainWindow.setMaximumSize(QtCore.QSize(887, 790))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 110, 841, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 240, 361, 231))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 161, 41))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setGeometry(QtCore.QRect(20, 140, 171, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 100, 161, 41))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 821, 221))
        self.frame_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 30, 113, 41))
        self.lineEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(280, 115, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(280, 35, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(630, 175, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(600, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(True)
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 30, 113, 41))
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(570, 35, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(30, 115, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(True)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 110, 113, 41))
        self.lineEdit_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(680, 110, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated.connect(self.combo)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(440, 110, 113, 41))
        self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 35, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(690, 170, 113, 41))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 30, 113, 41))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(380, 240, 451, 231))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(True)
        self.label_9.setObjectName("label_9")
        self.spinBox = QtWidgets.QSpinBox(self.frame_5)
        self.spinBox.setGeometry(QtCore.QRect(310, 31, 61, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(20, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 75, 261, 41))
        self.lineEdit_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.textChanged.connect(self.validation_1)
        self.lineEdit_8.setText('./generated_images')
        self.lineEdit_8.setDisabled(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.getFolder_1)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 190, 93, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Apply)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 190, 93, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Cancel)
        self.pushButton_4.setDisabled(True)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 841, 81))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(620, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getFolder)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(8, 30, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.validation)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(True)
        self.label_11.setObjectName("label_11")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 640, 841, 81))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setTabStopWidth(4)
        self.plainTextEdit.setMaximumBlockCount(0)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 600, 721, 31))
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 600, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def Message(self,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle("Warning")
        msg.exec_()

    def combo(self):
        if str(self.comboBox.currentText())!='Constant':
            self.lineEdit_3.setDisabled(True)
            self.lineEdit_3.setText('0.0')
        else:
            self.lineEdit_3.setDisabled(False)

    def getFolder(self):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(None,'Select a directory',os.getcwd())
        if foo_dir=='':
            self.Message("Please select Dataset folder!")
        else:
            self.lineEdit.setText(foo_dir)
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(False)
            self.lineEdit_8.setDisabled(False)
            self.lineEdit_8.setText(self.lineEdit_8.text()+'/'+self.lineEdit.text().split('/')[-1].capitalize())

    def getFolder_1(self):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(None,'Select a directory',os.getcwd())
        if foo_dir=='':
            self.Message("Please select Dataset folder!")
        else:
            self.lineEdit_8.setText(foo_dir+'/'+self.lineEdit.text().split('/')[-1].capitalize())

    def Apply(self):
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(False)

        self.progressBar.setMaximum(100)
        self.progressBar.setFormat("%p%, %v/%m")
        self.progressBar.setValue(0)

        if not os.path.isdir('generated_images'):
            os.mkdir('generated_images')

        if self.lineEdit.text()!='':
            if os.path.isdir(self.lineEdit.text()):
                try:
                    rotate_range =  int(self.lineEdit_2.text())
                except ValueError:
                    self.Message("Please specify correct Rotate Range value!")
                    return

                try:
                    shear_range =  float(self.lineEdit_7.text())
                except ValueError:
                    self.Message("Please specify correct Shear Range value!")
                    return

                try:
                    cval = int(self.lineEdit_3.text())
                except ValueError:
                    try:
                        cval = float(self.lineEdit_3.text())
                    except ValueError:
                        self.Message("Please specify correct CVal!")
                        return
                
                try:
                    width_shift_range = int(self.lineEdit_5.text())
                except ValueError:
                    try:
                        width_shift_range = float(self.lineEdit_5.text())
                    except ValueError:
                        try:
                            width_shift_range = [int(i) for i in self.lineEdit_5.text().split(',')]
                        except ValueError:
                            self.Message("Please specify correct Width Shift Range!")
                            return

                try:
                    height_shift_range = int(self.lineEdit_6.text())
                except ValueError:
                    try:
                        height_shift_range = float(self.lineEdit_6.text())
                    except ValueError:
                        try:
                            height_shift_range = [int(i) for i in self.lineEdit_6.text().split(',')]
                        except ValueError:
                            self.Message("Please specify correct Height Shift Range!")
                            return

                try:
                    zoom_range = float(self.lineEdit_4.text())
                except ValueError:
                    try:
                        zoom_range = [int(i) for i in self.lineEdit_4.text().split(',')]
                        if len(zoom_range)==2:
                            pass
                        else:
                            self.Message('Please specify upper and lower limit only!')
                            return
                    except ValueError:
                        self.Message("Please specify correct Zoom Range!")
                        return

                aug = ImageDataGenerator(
                    featurewise_center=self.checkBox.isChecked(),
                    zca_whitening=self.checkBox_4.isChecked(),
                    rotation_range=rotate_range,
                    width_shift_range=width_shift_range,
                    height_shift_range=height_shift_range,
                    shear_range=shear_range,
                    zoom_range=zoom_range,
                    fill_mode=self.comboBox.currentText().lower(),
                    cval=0.0 if self.comboBox.currentText().lower()!='constant' else cval,
                    horizontal_flip=self.checkBox_3.isChecked(),
                    vertical_flip=self.checkBox_2.isChecked(),
                )
                self.plainTextEdit.appendPlainText('Rotation Range:-'+ str(rotate_range))
                self.plainTextEdit.appendPlainText('Width Shift Range:-'+str(width_shift_range))
                self.plainTextEdit.appendPlainText('Height Shift Range:-'+str(height_shift_range))
                self.plainTextEdit.appendPlainText('Shear Range:-'+str(shear_range))
                self.plainTextEdit.appendPlainText('Zoom Range:-'+str(zoom_range))
                self.plainTextEdit.appendPlainText('Horizontal Flip:-'+str(self.checkBox_3.isChecked()))
                self.plainTextEdit.appendPlainText('Vertical Flip:-'+str(self.checkBox_2.isChecked()))
                
                img_list = [i for i in os.listdir(self.lineEdit.text()) if i.endswith(('.jpg','.jpeg','.webp'))]
                if len(img_list)>0:
                    if self.lineEdit_8.text().startswith('./generated_images'):
                        path = 'generated_images/'+self.lineEdit.text().split('/')[-1].capitalize()
                    else:
                        path = self.lineEdit_8.text()
                    try:
                        os.mkdir(path)
                    except FileExistsError:
                        pass
                    self.progressBar.setMaximum(len(img_list))

                    for i,j in enumerate(img_list):
                        image = load_img(self.lineEdit.text()+'/'+ j)
                        image = img_to_array(image)
                        image = np.expand_dims(image, axis=0)
                        self.plainTextEdit.appendPlainText("[INFO] generating images for "+j)
                        imageGen = aug.flow(image, batch_size=32, save_to_dir=path,
                            save_prefix="image", save_format="jpg")
                        self.progressBar.setMaximum(len(img_list))
                        self.progressBar.setFormat("%p%, %v/%m")
                        self.progressBar.setValue(i)
                        total = 0
                        print("[INFO] generating images for "+j)
                        for image in imageGen:
                            total += 1
                            if total == int(self.spinBox.text()):
                                break
                    self.progressBar.setMaximum(len(img_list))
                    self.progressBar.setFormat("%p%, %v/%m")
                    self.progressBar.setValue(len(img_list)) 
                    self.pushButton_3.setDisabled(False)               
                else:
                    self.Message("Please specify correct Dataset Folder with Images!")
                
            else:
                self.Message("Please specify correct Dataset folder!")
        else:
            self.Message("Please select Dataset folder!")

    def Cancel(self):
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(True)

    def validation(self):
        if self.lineEdit.text()=='':
            self.pushButton.setDisabled(False)
            self.pushButton_2.setDisabled(True)
            self.lineEdit_8.setDisabled(True)

    def validation_1(self):
        if self.lineEdit_8.text()=='':
            self.lineEdit_8.setText('./generated_images')
            self.pushButton.setDisabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dataset Generator"))
        self.checkBox_2.setToolTip(_translate("MainWindow", "Boolean. Randomly flip inputs vertically."))
        self.checkBox_2.setStatusTip(_translate("MainWindow", "Boolean. Randomly flip inputs vertically."))
        self.checkBox_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Boolean. Randomly flip inputs vertically.</p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "Vertical Flip"))
        self.checkBox.setToolTip(_translate("MainWindow", "Boolean. Set input mean to 0 over the dataset, feature-wise."))
        self.checkBox.setStatusTip(_translate("MainWindow", "Boolean. Set input mean to 0 over the dataset, feature-wise."))
        self.checkBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Boolean. Set input mean to 0 over the dataset, feature-wise.</p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Featurewise Center"))
        self.checkBox_4.setToolTip(_translate("MainWindow", "Boolean. Apply ZCA whitening."))
        self.checkBox_4.setStatusTip(_translate("MainWindow", "Boolean. Apply ZCA whitening."))
        self.checkBox_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Boolean. Apply ZCA whitening.</p></body></html>"))
        self.checkBox_4.setText(_translate("MainWindow", "ZCA Whitening"))
        self.checkBox_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Boolean. Randomly flip inputs horizontally.</p></body></html>"))
        self.checkBox_3.setStatusTip(_translate("MainWindow", "Boolean. Randomly flip inputs horizontally."))
        self.checkBox_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Boolean. Randomly flip inputs horizontally.</p></body></html>"))
        self.checkBox_3.setText(_translate("MainWindow", "Horizontal Flip"))
        self.lineEdit_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float: fraction of total width. - 1-D array-like: random elements from the array. - int:<span style=\" font-family:\'Courier New\';\">(-width_shift_range +width_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">width_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).</p></body></html>"))
        self.lineEdit_5.setStatusTip(_translate("MainWindow", "1-D array-like or int - float: fraction of total width. - 1-D array-like: random elements from the array. - int:(-width_shift_range +width_shift_range)[-1, 0, +1], while with width_shift_range=1.0 possible values are floats in the interval [-1.0, +1.0)."))
        self.lineEdit_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float: fraction of total width. - 1-D array-like: random elements from the array. - int:<span style=\" font-family:\'Courier New\';\">(-width_shift_range +width_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">width_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).</p></body></html>"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.2"))
        self.label_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float. - 1-D array-like: random elements from the array. - int: integer number of pixels from interval <span style=\" font-family:\'Courier New\';\">(-height_shift_range, +height_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">height_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).(Float)</p></body></html>"))
        self.label_6.setStatusTip(_translate("MainWindow", "1-D array-like or int - float. - 1-D array-like: random elements from the array. - int: integer number of pixels from interval (-height_shift_range, +height_shift_range)[-1, 0, +1], while with height_shift_range=1.0 possible values are floats in the interval [-1.0, +1.0).(Float)"))
        self.label_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float. - 1-D array-like: random elements from the array. - int: integer number of pixels from interval <span style=\" font-family:\'Courier New\';\">(-height_shift_range, +height_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">height_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).(Float)</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Height Shift Range:-"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float: fraction of total width. - 1-D array-like: random elements from the array. - int:<span style=\" font-family:\'Courier New\';\">(-width_shift_range +width_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">width_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).</p></body></html>"))
        self.label_5.setStatusTip(_translate("MainWindow", "1-D array-like or int - float. - 1-D array-like: random elements from the array. - int:(-width_shift_range +width_shift_range)[-1, 0, +1], while with width_shift_range=1.0 possible values are floats in the interval [-1.0, +1.0)."))
        self.label_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float: fraction of total width. - 1-D array-like: random elements from the array. - int:<span style=\" font-family:\'Courier New\';\">(-width_shift_range +width_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">width_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Width Shift Range:-"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Value used for points outside the boundaries when <span style=\" font-family:\'Courier New\';\">fill_mode = &quot;constant&quot;</span>. (Float or Int) </p></body></html>"))
        self.label_3.setStatusTip(_translate("MainWindow", "Value used for points outside the boundaries when fill_mode = \"constant\". (Float or Int) "))
        self.label_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Value used for points outside the boundaries when <span style=\" font-family:\'Courier New\';\">fill_mode = &quot;constant&quot;</span>. (Float or Int) </p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "CVal:-"))
        self.label_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>One of {&quot;constant&quot;, &quot;nearest&quot;, &quot;reflect&quot; or &quot;wrap&quot;}. Default is \'nearest\'. Points outside the boundaries of the input are filled according to the given mode: - \'constant\': kkkkkkkk|abcd|kkkkkkkk (cval=k) - \'nearest\': aaaaaaaa|abcd|dddddddd - \'reflect\': abcddcba|abcd|dcbaabcd - \'wrap\': abcdabcd|abcd|abcdabcd</p></body></html>"))
        self.label_8.setStatusTip(_translate("MainWindow", "One of {\"constant\", \"nearest\", \"reflect\" or \"wrap\"}. Default is \'nearest\'. Points outside the boundaries of the input are filled according to the given mode: - \'constant\': kkkkkkkk|abcd|kkkkkkkk (cval=k) - \'nearest\': aaaaaaaa|abcd|dddddddd - \'reflect\': abcddcba|abcd|dcbaabcd - \'wrap\': abcdabcd|abcd|abcdabcd"))
        self.label_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>One of {&quot;constant&quot;, &quot;nearest&quot;, &quot;reflect&quot; or &quot;wrap&quot;}. Default is \'nearest\'. Points outside the boundaries of the input are filled according to the given mode: - \'constant\': kkkkkkkk|abcd|kkkkkkkk (cval=k) - \'nearest\': aaaaaaaa|abcd|dddddddd - \'reflect\': abcddcba|abcd|dcbaabcd - \'wrap\': abcdabcd|abcd|abcdabcd</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Fill Mode:-"))
        self.lineEdit_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Float or [lower, upper]. Range for random zoom. If a float, <span style=\" font-family:\'Courier New\';\">[lower, upper] = [1-zoom_range, 1+zoom_range]</span>.</p></body></html>"))
        self.lineEdit_4.setStatusTip(_translate("MainWindow", "Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range]."))
        self.lineEdit_4.setWhatsThis(_translate("MainWindow", "Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range]."))
        self.lineEdit_4.setText(_translate("MainWindow", "0.15"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Float or [lower, upper]. Range for random zoom. If a float, <span style=\" font-family:\'Courier New\';\">[lower, upper] = [1-zoom_range, 1+zoom_range]</span>.</p></body></html>"))
        self.label_4.setStatusTip(_translate("MainWindow", "Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range]."))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Float or [lower, upper]. Range for random zoom. If a float, <span style=\" font-family:\'Courier New\';\">[lower, upper] = [1-zoom_range, 1+zoom_range]</span>.</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Zoom Range:-"))
        self.label_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shear Intensity (Shear angle in counter-clockwise direction in degrees).(Float)</p></body></html>"))
        self.label_7.setStatusTip(_translate("MainWindow", "Shear Intensity (Shear angle in counter-clockwise direction in degrees).(Float)"))
        self.label_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Shear Intensity (Shear angle in counter-clockwise direction in degrees).(Float)</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Shear Range:-"))
        self.lineEdit_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shear Intensity (Shear angle in counter-clockwise direction in degrees).(Float)</p></body></html>"))
        self.lineEdit_7.setStatusTip(_translate("MainWindow", "Shear Intensity (Shear angle in counter-clockwise direction in degrees).(Float)"))
        self.lineEdit_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Shear Intensity (Shear angle in counter-clockwise direction in degrees).(Float)</p></body></html>"))
        self.lineEdit_7.setText(_translate("MainWindow", "0.15"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Nearest"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Constant"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Reflect"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Wrap"))
        self.lineEdit_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>1-D array-like or int - float. - 1-D array-like: random elements from the array. - int: integer number of pixels from interval <span style=\" font-family:\'Courier New\';\">(-height_shift_range, +height_shift_range)[-1, 0, +1]</span>, while with <span style=\" font-family:\'Courier New\';\">height_shift_range=1.0</span> possible values are floats in the interval [-1.0, +1.0).(Float)</p></body></html>"))
        self.lineEdit_6.setStatusTip(_translate("MainWindow", "1-D array-like or int - float. - 1-D array-like: random elements from the array. - int: integer number of pixels from interval (-height_shift_range, +height_shift_range)[-1, 0, +1], while with height_shift_range=1.0 possible values are floats in the interval [-1.0, +1.0).(Float)"))
        self.lineEdit_6.setText(_translate("MainWindow", "0.2"))
        self.label_2.setToolTip(_translate("MainWindow", "Degree range for random rotations.(Integer)"))
        self.label_2.setStatusTip(_translate("MainWindow", "Degree range for random rotations.(Integer)"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Degree range for random rotations.(Integer)</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Rotation Range:-"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Value used for points outside the boundaries when <span style=\" font-family:\'Courier New\';\">fill_mode = &quot;constant&quot;</span>. (Float or Int) </p></body></html>"))
        self.lineEdit_3.setStatusTip(_translate("MainWindow", "Value used for points outside the boundaries when fill_mode = \"constant\". (Float or Int) "))
        self.lineEdit_3.setText(_translate("MainWindow", "0.0"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "Degree range for random rotations.(Integer)"))
        self.lineEdit_2.setStatusTip(_translate("MainWindow", "Degree range for random rotations.(Integer)"))
        self.lineEdit_2.setText(_translate("MainWindow", "30"))
        self.label_9.setToolTip(_translate("MainWindow", "<html><head/><body><p>Range from 1 to 50. Default 10</p></body></html>"))
        self.label_9.setStatusTip(_translate("MainWindow", "Range from 1 to 50. Default 10"))
        self.label_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Range from 1 to 50. Default 10</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Max number of images per Images:-"))
        self.spinBox.setToolTip(_translate("MainWindow", "Range from 1 to 50. Default 10"))
        self.spinBox.setStatusTip(_translate("MainWindow", "Range from 1 to 50. Default 10"))
        self.spinBox.setWhatsThis(_translate("MainWindow", "Range from 1 to 50. Default 10"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Degree range for random rotations.(Integer)</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Destination Folder:-"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton_3.setText(_translate("MainWindow", "Apply"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Degree range for random rotations.(Integer)</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Select Dataset Folder:-"))
        self.label.setText(_translate("MainWindow", "Total Progress:-"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())