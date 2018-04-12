from PyQt5 import QtCore, QtGui, QtWidgets
import sys, xlwt,datetime,os
import pandas as pd
from netmiko import ConnectHandler
import time, os
from netmiko import redispatch
import logging

logger=logging.getLogger('')
logger.propogate=False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.tick2=QtCore.pyqtSignal(str,name="rsa")
        self.tick3=QtCore.pyqtSignal(str,name="rsa_receiver")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\ks854x\\Desktop\\SCRIPTS\\scripts\\fb2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tray_icon=QtWidgets.QSystemTrayIcon()
        self.tray_icon.setIcon(icon)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font2 = QtGui.QFont()
        font2.setBold(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_lbl = QtWidgets.QLabel(self.centralwidget)
        self.password_lbl.setObjectName("password_lbl")
        self.horizontalLayout_2.addWidget(self.password_lbl)
        self.pass_le = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_le.setObjectName("pass_le")
        self.horizontalLayout_2.addWidget(self.pass_le)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.export_dir_lbl = QtWidgets.QLabel(self.centralwidget)
        self.export_dir_lbl.setObjectName("export_dir_lbl")
        self.horizontalLayout_4.addWidget(self.export_dir_lbl)
        self.export_directory_le = QtWidgets.QLineEdit(self.centralwidget)
        self.export_directory_le.setObjectName("export_directory_le")
        self.horizontalLayout_4.addWidget(self.export_directory_le)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")
        self.horizontalLayout_4.addWidget(self.browse)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 0, 1, 3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.enable_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.enable_chk.setObjectName("enable_chk")
        self.horizontalLayout_7.addWidget(self.enable_chk)
        self.enable_le = QtWidgets.QLineEdit(self.centralwidget)
        self.enable_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enable_le.setObjectName("enable_le")
        self.horizontalLayout_7.addWidget(self.enable_le)
        self.enable_le.setEnabled(False)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 10, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.user_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.user_lbl.setObjectName("user_lbl")
        self.horizontalLayout.addWidget(self.user_lbl)
        self.user_le = QtWidgets.QLineEdit(self.centralwidget)
        self.user_le.setObjectName("user_le")
        self.horizontalLayout.addWidget(self.user_le)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 3)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.backup_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.backup_chk.setObjectName("backup_chk")
        self.verticalLayout_3.addWidget(self.backup_chk)
        self.post_backup_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.post_backup_chk.setObjectName("post_backup_chk")
        self.verticalLayout_3.addWidget(self.post_backup_chk)
        


        self.bulk_config_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.bulk_config_chk.setObjectName("bulk_config_chk")
        self.verticalLayout_3.addWidget(self.bulk_config_chk)

        self.host_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.host_chk.setObjectName("host_chk")
        self.verticalLayout_3.addWidget(self.host_chk)

        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.cpu_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.cpu_chk.setObjectName("cpu_chk")
        self.horizontalLayout_15.addWidget(self.cpu_chk)
        self.cpu_le = QtWidgets.QLineEdit(self.centralwidget)
        self.cpu_le.setObjectName("cpu_le")
        self.horizontalLayout_15.addWidget(self.cpu_le)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.memory_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.memory_chk.setObjectName("memory_chk")
        self.horizontalLayout_16.addWidget(self.memory_chk)
        self.rsa_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.rsa_chk.setObjectName("rsa_chk")
        self.verticalLayout_3.addWidget(self.rsa_chk)
        self.jumpserver_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.jumpserver_chk.setObjectName("jumpserver_chk")
        self.verticalLayout_3.addWidget(self.jumpserver_chk)
        self.memory_le = QtWidgets.QLineEdit(self.centralwidget)
        self.memory_le.setObjectName("memory_le")
        self.horizontalLayout_16.addWidget(self.memory_le)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.delay_seconds_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.delay_seconds_chk.setObjectName("delay_seconds_chk")
        self.horizontalLayout_17.addWidget(self.delay_seconds_chk)
        self.delay_seconds_le = QtWidgets.QLineEdit(self.centralwidget)
        self.backup_only_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.backup_only_chk.setObjectName("backup_only_chk")
        self.verticalLayout_3.addWidget(self.backup_only_chk)
        self.show_commands_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.show_commands_chk.setObjectName("show_commands_chk")
        self.verticalLayout_3.addWidget(self.show_commands_chk)
        self.cpu_le.setObjectName("delay_seconds_le")
        self.horizontalLayout_17.addWidget(self.delay_seconds_le)
        
        
        #self.empty_lbl = QtWidgets.QLabel(self.centralwidget)
        #self.empty_lbl.setText("")
        #self.empty_lbl.setObjectName("empty_lbl")
        #self.verticalLayout_3.addWidget(self.empty_lbl)
        self.gridLayout.addLayout(self.verticalLayout_3, 10, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.location_lbl = QtWidgets.QLabel(self.centralwidget)
        self.location_lbl.setObjectName("location_lbl")
        self.horizontalLayout_3.addWidget(self.location_lbl)
        self.device_file_text = QtWidgets.QLineEdit(self.centralwidget)
        self.device_file_text.setObjectName("device_file_text")
        self.horizontalLayout_3.addWidget(self.device_file_text)
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setStyleSheet("blue")
        self.upload.setObjectName("upload")
        self.horizontalLayout_3.addWidget(self.upload)
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setStyleSheet("blue")
        self.START.setObjectName("START")
        self.horizontalLayout_3.addWidget(self.START)
        self.gridLayout.addLayout(self.horizontalLayout_3, 9, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.export_lbl = QtWidgets.QLabel(self.centralwidget)
        self.export_lbl.setText("")
        self.export_lbl.setFont(font2)
        self.export_lbl.setObjectName("export_lbl")
        self.verticalLayout_2.addWidget(self.export_lbl)
        self.progress_lbl = QtWidgets.QLabel(self.centralwidget)
        self.progress_lbl.setText("")
        self.progress_lbl.setFont(font2)
        self.progress_lbl.setObjectName("progress_lbl")
        self.verticalLayout_2.addWidget(self.progress_lbl)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_2, 11, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lcd_lbl = QtWidgets.QLabel(self.centralwidget)
        self.horizontalLayout_6.addWidget(self.lcd_lbl)
        self.lcd_lbl = QtWidgets.QLabel(self.centralwidget)

        self.lcd_lbl.setFont(font)
        self.lcd_lbl.setObjectName("lcd_lbl")
        self.horizontalLayout_6.addWidget(self.lcd_lbl)
        self.device_counter = QtWidgets.QLCDNumber(self.centralwidget)
        self.device_counter.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.device_counter.setStyleSheet(" background-color: black;\n"
"color: yellow;")
        self.device_counter.setObjectName("device_counter")
        self.horizontalLayout_6.addWidget(self.device_counter)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sys_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sys_user_lbl.setObjectName("sys_user_lbl")
        self.horizontalLayout_11.addWidget(self.sys_user_lbl)
        self.sys_user_le = QtWidgets.QLineEdit(self.centralwidget)
        self.sys_user_le.setObjectName("sys_user_le")
        self.horizontalLayout_11.addWidget(self.sys_user_le)
        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.sys_pass_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sys_pass_lbl.setObjectName("sys_pass_lbl")
        self.horizontalLayout_12.addWidget(self.sys_pass_lbl)
        self.sys_pass_le = QtWidgets.QLineEdit(self.centralwidget)
        self.sys_pass_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sys_pass_le.setObjectName("sys_pass_le")
        self.horizontalLayout_12.addWidget(self.sys_pass_le)
        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.syslog_ip_lbl = QtWidgets.QLabel(self.centralwidget)
        self.syslog_ip_lbl.setObjectName("syslog_ip_lbl")
        self.horizontalLayout_7.addWidget(self.syslog_ip_lbl)
        self.syslog_ip_le = QtWidgets.QLineEdit(self.centralwidget)
        self.syslog_ip_le.setObjectName("syslog_ip_le")
        self.horizontalLayout_7.addWidget(self.syslog_ip_le)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.sys_user_le, self.sys_pass_le)
        MainWindow.setTabOrder(self.sys_pass_le, self.syslog_ip_le)
        MainWindow.setTabOrder(self.syslog_ip_le, self.user_le)
        MainWindow.setTabOrder(self.user_le, self.pass_le)
        MainWindow.setTabOrder(self.pass_le, self.enable_chk)
        MainWindow.setTabOrder(self.enable_chk, self.enable_le)
        MainWindow.setTabOrder(self.enable_le, self.export_directory_le)
        MainWindow.setTabOrder(self.export_directory_le, self.browse)
        MainWindow.setTabOrder(self.browse, self.backup_chk)
        MainWindow.setTabOrder(self.backup_chk, self.post_backup_chk)
        MainWindow.setTabOrder(self.post_backup_chk, self.bulk_config_chk)
        MainWindow.setTabOrder(self.bulk_config_chk, self.host_chk)
        MainWindow.setTabOrder(self.host_chk, self.cpu_chk)
        MainWindow.setTabOrder(self.cpu_le, self.memory_chk)
        MainWindow.setTabOrder(self.memory_chk, self.memory_le)
        MainWindow.setTabOrder(self.memory_le, self.delay_seconds_chk)
        MainWindow.setTabOrder(self.delay_seconds_chk, self.delay_seconds_le)
        MainWindow.setTabOrder(self.delay_seconds_le, self.backup_only_chk)
        MainWindow.setTabOrder(self.backup_only_chk, self.show_commands_chk)
        MainWindow.setTabOrder(self.show_commands_chk, self.rsa_chk)
        MainWindow.setTabOrder(self.rsa_chk, self.jumpserver_chk)
        MainWindow.setTabOrder(self.jumpserver_chk, self.upload)
        MainWindow.setTabOrder(self.upload,self.START)
        MainWindow.setTabOrder(self.START, self.device_file_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Implementer"))
        self.password_lbl.setText(_translate("MainWindow", "Password"))
        self.export_dir_lbl.setText(_translate("MainWindow", " Export Directory "))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.enable_chk.setText(_translate("MainWindow", "enable password( (if not same as password)"))
        self.user_lbl.setText(_translate("MainWindow", "Username"))
        self.backup_chk.setText(_translate("MainWindow", " Export Pre config backup"))
        self.post_backup_chk.setText(_translate("MainWindow", " Export Post config backup"))
        self.bulk_config_chk.setText(_translate("MainWindow", " Single file multiple devices"))
        self.host_chk.setText(_translate("MainWindow", " Verify hostname"))
        self.cpu_chk.setText(_translate("MainWindow", " CPU Threshold      "))
        self.memory_chk.setText(_translate("MainWindow", " Memory Threshold"))
        self.delay_seconds_chk.setText(_translate("MainWindow", " Delay Seconds"))
        self.backup_only_chk.setText(_translate("MainWindow", " Backup only (NO IMPLEMENTATION!)"))
        self.show_commands_chk.setText(_translate("MainWindow", " Show commands only (NO IMPLEMENTATION!)"))
        self.rsa_chk.setText(_translate("MainWindow", " Device requires RSA"))   
        self.jumpserver_chk.setText(_translate("MainWindow", " Jumpserver requires RSA"))     
        self.location_lbl.setText(_translate("MainWindow", "Devices File "))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.START.setText(_translate("MainWindow", "START"))
        self.label.setText(_translate("MainWindow", "                                                                           support: Kalif (ks854x@att.com)"))
        self.lcd_lbl.setText(_translate("MainWindow", "   Devices Touched"))
        self.sys_pass_lbl.setText(_translate("MainWindow", "Jumpserver password "))
        self.sys_user_lbl.setText(_translate("MainWindow", "Jumpserver username "))
        self.syslog_ip_lbl.setText(_translate("MainWindow", "Jumpserver IP"))
        self.enable_chk.pressed.connect(self.get_enable)
        self.browse.pressed.connect(self.select_directory)
        self.upload.pressed.connect(self.upload_device_file)

        
        self.START.pressed.connect(self.button_press)
        self.bulk_config_chk.pressed.connect(self.disable_hostname_check)
        self.cpu_le.setEnabled(False)
        self.memory_le.setEnabled(False)
        self.cpu_chk.pressed.connect(self.cpu_threshold_entry)
        self.memory_chk.pressed.connect(self.memory_threshold_entry)
        self.delay_seconds_le.setEnabled(False)
        self.delay_seconds_chk.pressed.connect(self.enable_delay_second_le)
        self.backup_only_chk.pressed.connect(self.backup_only_check)




    def getRSA(self,comment):
        self.localcomment = "NF"
        self.localcomment = comment
        self.rsa = 'Not found'
    
        try:
            if "need RSA" in comment:
                self.rsa, okPressed =QtWidgets.QInputDialog.getText(MainWindow,"RSA Password","Enter RSA Token or Password", QtWidgets.QLineEdit.Password, "")
                time.sleep(3)
                if okPressed:
                    #self.rsa_chk.emit(self.rsa)
                    self.workerThread.rsaTick.emit(self.rsa)
                
        except Exception as e:
            print("Error:{0}".format(e))

    def cpu_threshold_entry(self):
        #print(self.host_chk.isChecked())
        if self.cpu_chk.isChecked():
            self.cpu_le.setEnabled(False)
        else:
            self.cpu_le.setEnabled(True)

    def memory_threshold_entry(self):
        if self.memory_chk.isChecked():
            self.memory_le.setEnabled(False)
        else:
            self.memory_le.setEnabled(True)
    def enable_delay_second_le(self):
        #print(self.host_chk.isChecked())
        if self.delay_seconds_chk.isChecked():
            self.delay_seconds_le.setEnabled(False)
        else:
            self.delay_seconds_le.setEnabled(True)

    def disable_hostname_check(self):
        #print(self.host_chk.isChecked())
        if self.host_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                self.host_chk.setCheckState(False)
                self.host_chk.setEnabled(False)
        if self.bulk_config_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                #self.host_chk.setCheckState(True)
                if self.host_chk.setEnabled(True):
                    self.host_chk.setEnabled(False)
        else:
            self.host_chk.setEnabled(False)

    def backup_only_check(self):
        #print(self.host_chk.isChecked())
        if self.host_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                self.host_chk.setCheckState(False)
                self.host_chk.setEnabled(False)
        if self.backup_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                self.backup_chk.setCheckState(False)
                self.backup_chk.setEnabled(False)

        if self.post_backup_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                self.post_backup_chk.setCheckState(False)
                self.post_backup_chk.setEnabled(False)

        if self.bulk_config_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                self.bulk_config_chk.setCheckState(False)
                self.bulk_config_chk.setEnabled(False)

        


        if self.backup_only_chk.isChecked():
                #self.host_chk.setCheckState(False)
                #QtWidgets.QMessageBox.information(MainWindow,'info',"Please uncheck hostname verification for bulk config file")
                #self.host_chk.setCheckState(True)
                if self.host_chk.setEnabled(True):
                    self.host_chk.setEnabled(False)
                if self.backup_chk.setEnabled(True):
                    self.backup_chk.setEnabled(False)
                if self.post_backup_chk.setEnabled(True):
                    self.post_backup_chk.setEnabled(False)
                if self.delay_seconds_chk.setEnabled(True):
                    self.delay_seconds_chk.setEnabled(False)
                    self.delay_seconds_le.setEnabled(False)
                if self.bulk_config_chk.setEnabled(True):
                    self.bulk_config_chk.setEnabled(False)
        else:
            self.host_chk.setEnabled(False)
            self.backup_chk.setEnabled(False)
            self.post_backup_chk.setEnabled(False)
            
            self.bulk_config_chk.setEnabled(False)

        #print(self.host_chk.isChecked())
    
    def get_enable(self):
        if self.enable_chk.isChecked():
            self.enable_le.setEnabled(False)
        else:
            self.enable_le.setEnabled(True)
        
    def select_directory(self):
        self.export_directory=QtWidgets.QFileDialog.getExistingDirectory(MainWindow,'select Directory')
        self.export_directory_le.setText(self.export_directory)

    def upload_device_file(self):
        try:
            self.file=QtWidgets.QFileDialog.getOpenFileName(MainWindow,'Open File',os.getenv('C:\\Users\\'))
            self.device_file_text.setText(self.file[0])
        except Exception as e:
            print(str(e))



    def button_press(self):

        if self.enable_le.text():
            self.enable_passwd=self.enable_le.text()
        else:
            self.enable_passwd=None
            
        if not self.export_directory_le.text():
            QtWidgets.QMessageBox.information(MainWindow,'info',"Export directory missing! please select before executing device file.")
            self.export_directory=QtWidgets.QFileDialog.getExistingDirectory(MainWindow,'select Directory')
            self.export_directory_le.setText(self.export_directory)

        userid=str(self.user_le.text())
        passwd=str(self.pass_le.text())


        if self.cpu_chk.isChecked():
            try:
                cpu_threshold=int(self.cpu_le.text())
                if cpu_threshold >99 or cpu_threshold <1:
                    QtWidgets.QMessageBox.information(MainWindow,'info',"Incorrect CPU Threshold! Please Enter correct value between 1 to 99")
                    return
            except Exception as e:
                QtWidgets.QMessageBox.information(MainWindow,"Invalid input","CPU Threshold missing, Please Enter correct value between 1 to 99".format(e))
                return
        if self.memory_chk.isChecked():
            try:
                memory_threshold=int(self.memory_le.text())
                if memory_threshold >99 or memory_threshold <1:
                    QtWidgets.QMessageBox.information(MainWindow,'info',"Incorrect memory Threshold ! Please Enter correct value between 1 to 99")
                    return
            except Exception as e:
                QtWidgets.QMessageBox.information(MainWindow,"Invalid input","Memory Threshold missing, Please Enter correct value between 1 to 99".format(e))
                return

        if self.delay_seconds_chk.isChecked():
            try:
                delay_value=int(self.delay_seconds_le.text())
                if delay_value >600 or delay_value <1:
                    QtWidgets.QMessageBox.information(MainWindow,'info',"Incorrect Delay value ! Please Enter correct value between 1 to 600 seconds")
                    return
            except Exception as e:
                QtWidgets.QMessageBox.information(MainWindow,"Invalid input","Incorrect Delay value or missing ! Please Enter correct value between 1 to 300 seconds".format(e))
                return


        if not userid or not passwd:
            QtWidgets.QMessageBox.information(MainWindow,"Invalid input","Incorrect Username or Password !")
        else:
            try:
                from colorama import Fore, Back, Style
                from colorama import init
                init() 

                if self.START.text()=='STOP':                 
                
                    time.sleep(2) 
                    self.START.setText('START')
                    self.export_lbl.setText('Program Terminated!!')
                    self.progress_lbl.setText('Program Stopped by User')
                    self.workerThread.terminate()
                    print(Fore.RED,"PROGRAM TERMINATED!!")


                else:
                    
                    self.workerThread = WorkerThread(self.file,self.backup_chk.isChecked(),self.post_backup_chk.isChecked(),self.progressBar,self.progress_lbl,self.device_file_text,userid,passwd,self.device_counter,self.export_lbl,self.export_directory,self.enable_passwd,self.syslog_ip_le.text(),self.sys_user_le.text(),self.sys_pass_le.text(),self.bulk_config_chk.isChecked(),self.host_chk.isChecked(),self.cpu_chk.isChecked(),self.cpu_le.text(),self.memory_chk.isChecked(),self.memory_le.text(),self.delay_seconds_chk.isChecked(),self.delay_seconds_le.text(),self.START,self.rsa_chk.isChecked(),self.jumpserver_chk.isChecked(),self.backup_only_chk.isChecked(),self.show_commands_chk.isChecked())
                    self.workerThread.setTerminationEnabled(True)
                    self.START.setText('STOP')    
                    # Pass the function to execute
                    self.workerThread.start()
                    self.workerThread.tick.connect(self.progressBar.setValue)
                    self.workerThread.rsaTick.connect(self.getRSA )
            except Exception as e:
                self.progress_lbl.text(str(e))

            





class WorkerThread(QtCore.QThread):
    
    tick=QtCore.pyqtSignal(int,name="changed")
    rsaTick = QtCore.pyqtSignal(str,name="RSA_rec")
    def stop(self):
        sys.exit()
    
    def __init__(self,file,backup,post_backup,progress,lbl_progress,le,userid,passwd,counter,lbl_export,export_dir,enable_pass,syslog_ip,syslog_user,syslog_pass,bulk_chk,host_chk,cpu_chk,cpu_le,memory_chk,memory_le,delay_chk,delay_le,START,rsa_chk,jumpserver_chk,backup_only_chk,show_commands_chk, parent=None):
        super(QtCore.QThread, self).__init__(parent)
        self.file=file
        self.backup=backup
        self.post_backup=post_backup        
        self.progress=progress
        self.lbl_progress=lbl_progress
        self.le=le
        self.username=userid
        self.password=passwd
        self.enable_passwd=enable_pass
        self.counter=counter
        self.lbl_export=lbl_export
        self.export_dir=export_dir
        self.syslog_ip=syslog_ip
        self.sys_username=syslog_user
        self.sys_password=syslog_pass
        self.bulk_chk=bulk_chk
        self.host_chk=host_chk
        self.cpu_chk=cpu_chk
        self.cpu_le=cpu_le
        self.memory_chk=memory_chk
        self.memory_le=memory_le
        self.delay_chk=delay_chk
        self.backup_only_chk=backup_only_chk
        self.show_commands_chk=show_commands_chk
        self.delay_le=delay_le
        self.rsa_chk=rsa_chk 
        self.jumpserver_chk=jumpserver_chk 
        self.START=START
        self.rsa_key = "NF"
        self.change_success="no"

        

        os.system('cls')
        #os.system('color 70')
        os.system('mode con:cols=90 lines=12000')
        

        
        if self.delay_chk:
            self.delay_value=int(self.delay_le)
        else:
            self.delay_value=50

        if self.cpu_chk:
            self.cpu_value=int(self.cpu_le)
        else:
            self.cpu_value=30
        if self.memory_chk:
            self.memory_value=int(self.memory_le)
        else:
            self.memory_value=70

    

    

    def whatisRSAvalue(self,keyvalue):
            
            self.rsa_key = keyvalue
            
            #print("Given RSA key is :  ",self.rsa_key)

    def run(self):
        import time,datetime
        date_today,time_now,=str(datetime.datetime.now()).split()
        time_now,junk=time_now.split('.')
        from colorama import Fore, Back, Style
        from colorama import init
        init() 
        
        start_time = time.time()
        time_now=time_now.replace(':','-')


        def decorate(color,message,char):
            print(color+Style.BRIGHT+'\n'+char*len(message))
            print(color+Style.BRIGHT+message)
            print(color+Style.BRIGHT+char*len(message)+'\n')
        
        def health_check(cisco,ip,device_type):
            self.lbl_export.setText('Checking CPU and Memory utilization..')
            if device_type=='cisco_asa':
                output=cisco.send_command_expect('sh cpu usa | in second',delay_factor=5)
                log_file.write(output+'\n')
                output=output.split()
                per,semi=output[9].split('%')
                cpu=float(per)
                #print(cpu)
                output=cisco.send_command_expect('sh memory | in Used',delay_factor=5)
                log_file.write(output+'\n')
                output=output.split('(')
                #print(output[-1])
                mem1=output[-1].rstrip()
                mem1,mem2=mem1.split('%')
                mem1=mem1.rstrip().lstrip()
                #print(mem1)
                #print(output)
                mem=str(mem1).lstrip()
                #print(mem)
                memory=int(mem)
                return (cpu,memory)
            if device_type=='cisco_ios':
                output=cisco.send_command_expect('sh process cpu sort | in CPU',delay_factor=5)
                log_file.write(output+'\n')
                output=output.split()
                per,semi=output[8].split('%')
                cpu=int(per)
                output=cisco.send_command_expect('sh processes memory sorted | in Used',delay_factor=5)
                log_file.write(output+'\n')
                output=output.split()
                used=(int(output[5])/int(output[3]))*100
                memory=int(used)
                return (cpu,memory)
            if device_type=='cisco_nxos':
                cisco.send_command('\n')
                output=cisco.send_command_expect("sh system resources | in 'CPU states'",delay_factor=5)
                try:
                    log_file.write(output+'\n')
                    output=output.split()
                    #per,semi=output[4].split('%')
                    cpu_free=output[7].split('%')
                    cpu=100-float(cpu_free[0])

                    #print(cpu)
                    cisco.send_command_expect('\n')
                    output=cisco.send_command_expect('show system resources | in Memory',delay_factor=5)
                    log_file.write(output+'\n')
                    output=output.split('K')
                    #print(output)

                    total_mem=output[0].split()
                    total_mem=int(total_mem[2])
                    #print("Total Memory:{0}".format(total_mem))
                    used_mem=output[1].split()
                    used_mem=int(used_mem[1])
                    #print("Used Memory:{0}".format(used_mem))
                    
                    used_per=(used_mem/total_mem)*100
                    #print(used_per)
                    memory=int(used_per)
                except Exception as e:
                    print(Fore.RED+'Error: \n{0}'.format(str(e)))
                return (cpu,memory)
        
        def update_progress(index,last_item):
            self.valuep=round(index/last_item*100, 2)
            self.tick.emit(self.valuep)
            time.sleep(1.5)
        def check_failover(cisco,ip,device_type):
            if device_type=='cisco_asa':
                role=cisco.send_command_expect('sh fail | in This',delay_factor=20).split()
                #print(role)
                #print("I am here!")                
                if not role:
                    pass
                elif role[1]=='context:':
                    return str(role[2])
                elif role[4]=='Standby':
                    return str(role[4])
                else:
                    pass
        
        #print(Back.DIM)
        

        def configure_device(cisco,ip,device_type,filename):
            
            self.change_success="no"
            
            if '/' in hostname:
                hostname2=hostname.replace('/','_')
                asa_type="context"
            else:
                asa_type="normal"
                hostname2=hostname

            if self.backup_only_chk:
                   
                    self.lbl_export.setStyleSheet("QLabel {color: brown}") 
                    self.lbl_export.setText('Exporting config backup..(may take a while for bigger file)')
                    f = open(self.export_dir+'/{0}_backup_{1}_{2}.log'.format(hostname2,date_today,time_now),'w')   
                    if device_type=='cisco_nxos' or asa_type=="context":            
                        backup=cisco.send_command_expect('sh run',delay_factor=self.delay_value)
                    else:
                        backup=cisco.send_command_expect('more system:running-config',delay_factor=self.delay_value)
                        
                    f.write(backup)
                    f.close()
                    config_list.append('No')

                    return self.change_success

            if self.backup:
                     

                    self.lbl_export.setStyleSheet("QLabel {color: brown}") 
                    self.lbl_export.setText('Exporting pre config..(may take a while for bigger file)')
                    f = open(self.export_dir+'/{0}_Pre_{1}_{2}.log'.format(hostname2,date_today,time_now),'w')                    
                    if device_type=='cisco_nxos' or asa_type=="context": 
                        backup=cisco.send_command_expect('sh run',delay_factor=self.delay_value)
                    else:
                        backup=cisco.send_command_expect('more system:running-config',delay_factor=self.delay_value)
                    f.write(backup)
                    f.close()

            try:

                if filename: 
                        cmd_file=open(self.export_dir+'/{0}_Prov_{1}_{2}.log'.format(hostname2,date_today,time_now),'w')
                        #time.sleep(1)
                        if self.show_commands_chk:
                            f=open('{0}/{1}.txt'.format(self.export_dir,filename))
                            show_commands=f.readlines()
                            config_list.append('No')
                            self.lbl_export.setStyleSheet("QLabel {color: brown}") 
                            self.lbl_export.setText('sending show commands...')
                             
                            decorate(Fore.WHITE,"START OF SHOW COMMANDS:","+")
                            for cmd in show_commands:                             

                                print(Fore.GREEN,cmd)
                                cmd_file.write(cmd+"\n")
                                output=cisco.send_command_expect(cmd)
                                if not output:
                                    cmd_file.write("\n")
                                else:                        
                                    cmd_file.write(output)
                                print(Fore.GREEN,output)
                            
                            decorate(Fore.WHITE,"END OF SHOW COMMANDS","+")
                        else:
                            self.lbl_export.setStyleSheet("QLabel {color: brown}") 
                            self.lbl_export.setText('implementing...')
                            #print("I am just before config push")                      
                            output=cisco.send_config_from_file(config_file='{0}/{1}.txt'.format(self.export_dir,filename))
                            decorate(Fore.WHITE,"START OF IMPLEMENTATION:","+")
                            print(Fore.GREEN,output)
                            if not output:
                                cmd_file.write("\n")
                                config_list.append('No')
                                cmd_file.close()
                                return
                            else:                        
                                cmd_file.write(output)
                            self.lbl_export.setText('')
                            config_list.append('Yes')
                            self.lbl_export.setText('Saving Config')
                            if device_type=='cisco_nxos':
                                output=cisco.send_command_expect('copy run start')
                                #if 'complete' in output:
                                 #   print(output)
                            else:
                                cisco.send_command_expect('end')
                                output=cisco.send_command_expect('wr mem',delay_factor=30)
                                print(output)
                            cmd_file.write(output)
                            self.change_success="success"
                            decorate(Fore.WHITE,"END OF IMPLEMENTATION","+")

                        
                        '''ip_txt=open('{0}/{1}.txt'.format(self.export_dir,ip))
                        config_commands=ip_txt.readlines()
                        output=cisco.send_config_set(config_commands,delay_factor=30)'''
                        
                        
                        
                        cmd_file.close()
                        
                        if self.post_backup:
                            
                            self.lbl_export.setText('Exporting post config..(may take a while for bigger file)')
                            #time.sleep(5)
                            f = open(self.export_dir+'/{0}_Post_{1}_{2}.log'.format(hostname2,date_today,time_now),'w')                    
                            cisco.send_command('term page 0')
                            if device_type=='cisco_nxos' or asa_type=="context": 
                                backup=cisco.send_command_expect('sh run',delay_factor=self.delay_value)
                            else:
                                backup=cisco.send_command_expect('more system:running-config',delay_factor=self.delay_value)
                            f.write(backup)
                            f.close()

                else:
                    self.lbl_export.setText('Config file: {0}.txt or bulk_config is missing'.format(ip))
                    config_list.append('No')                            
                    time.sleep(1)
            except Exception as e:
                    self.lbl_export.setStyleSheet("QLabel {color: red}") 
                    self.lbl_export.setText('{0}'.format(e))
                    print(Fore.RED+'\n{0}'.format(str(e)))
                    config_list.append('No')
                    log_file.write(str(e)+'\n')
                    if cmd_file:
                        #cmd_file.write(output)
                        cmd_file.close()
                    time.sleep(3)
                    self.change_success="no"
            return self.change_success


        try:
            script_error=open(self.export_dir+'/'+'tool_error_log-'+str(date_today)+'_'+str(time_now)+'.txt','w')
            #file=QtWidgets.QFileDialog.getOpenFileName(MainWindow,'Open File',os.getenv('C:\\Users\\'))
            file=self.file
            self.le.setText(file[0]) 

            devices=pd.read_excel(file[0])
            self.last_item=int(devices.index.size)
            #print(self.last_item)
            ip_list=[]
            config_list=[]
            host_list=[]
            cpu_list=[]
            memory_list=[]
            joiner=' '
            count=0
            log_file=open(self.export_dir+'/'+'error_log-'+str(date_today)+'_'+str(time_now)+'.txt','w')
            
            if self.enable_passwd:
                self.enable_secret=self.enable_passwd
            else:
                self.enable_secret=self.password

            import time
            auth_count=0
            auth_failure=False

            decorate(Fore.WHITE,'IMPLEMENTER TOOL','-')
            print(Fore.YELLOW+"DATE: {1} - TIME: {0}".format(time_now.replace('-',':'),date_today))

            
            if self.show_commands_chk:
                print(Back.CYAN+Style.BRIGHT+Fore.WHITE+'MODE: SHOW COMMANDS ONLY (supported in bulk (ex: asa.txt) or in multi config mode(ip.txt))')
                print(Back.RESET)
            elif self.backup_only_chk:
                print(Back.CYAN+Style.BRIGHT+Fore.WHITE+'MODE: BACKUP ONLY MODE')
                print(Back.RESET)
            elif self.bulk_chk:
                print(Back.CYAN+Style.BRIGHT+Fore.WHITE+'MODE: BULK CONFIG MODE (files needed: asa.txt,ios.txt,nexus.txt)')
                print(Back.RESET)
            else:
                print(Back.CYAN+Style.BRIGHT+Fore.WHITE+'MODE: MULTI CONFIG MODE (files needed: ip.txt)')
                print(Back.RESET)
           




            self.tick.emit(0)
            

            self.lbl_export.setText('')
            update_progress(0,100)
            for index,row in devices.iterrows():


                
                ip=row.values[0]
                device_type=row.values[1].lower()
                jumpserver=row.values[2].lower()

                
                
                
                if jumpserver=='yes':
                    
                    '''if not self.sys_username or not self.sys_password or not self.syslog_ip:
                        self.lbl_export.setStyleSheet("QLabel {color: red}") 
                        self.lbl_export.setText("Syslog credentials missing! device: {0} requires jumpserver".format(ip))
                        conn_log=str("Device: {0}".format(ip))
                        log_file.write('\n'+"-"*len(conn_log)+'\n')
                        log_file.write(conn_log+'\n')                        
                        log_file.write("-"*len(conn_log)+'\n')
                        log_file.write("Syslog credentials missing! device: {0} requires jumpserver".format(ip))
                        time.sleep(1.5)
                        update_progress(index,self.last_item)
                        auth_failure=False
                        continue
                    else:
                        pass'''
                        #print("Entering through syslog")
                                        
                    try:
                        if self.jumpserver_chk:
                            self.rsaTick.emit("need RSA")
                            time.sleep(3)
                            self.rsaTick.connect(self.whatisRSAvalue)
                            time.sleep(8)                            
                            self.sys_password = self.rsa_key
                                
                        else:
                            pass
                        self.lbl_progress.setStyleSheet("QLabel {color: black}") 
                        self.lbl_progress.setText("Logging to Jumpserver {0}".format(self.syslog_ip))
                        self.lbl_export.setText('')

                        syslog={'device_type':'linux','ip':self.syslog_ip,'username':self.sys_username,'secret':self.enable_secret,'password':self.sys_password,'port':22,'global_delay_factor':4,}
                        cisco=ConnectHandler(**syslog)
                        time.sleep(2)
                        self.lbl_progress.setText("Connected to Jumpserver {0}".format(self.syslog_ip))

                        #print("SSH from Syslog:{0}".format(self.syslog_ip))
                        #print (cisco.find_prompt())
                        #output=cisco.read_channel()
                        #print(output)
                        #log_file.write(output)

                        self.lbl_progress.setStyleSheet("QLabel {color: black}") 
                        self.lbl_progress.setText("Connecting to {0}".format(ip))
                        conn_log=str("Device: {0}".format(ip))
                        log_file.write('\n'+"-"*len(conn_log)+'\n')
                        log_file.write(conn_log+'\n')                        
                        log_file.write("-"*len(conn_log)+'\n')
                        try:
                        
                            if self.rsa_chk:
                        
                                self.rsaTick.emit("need RSA")
                                time.sleep(3)
                                self.rsaTick.connect(self.whatisRSAvalue)
                                time.sleep(7)                            
                                self.password = self.rsa_key
                                self.enable_secret = self.rsa_key                                
                            else:
                                pass

                            cisco.write_channel("ssh -o StrictHostKeyChecking=no {0}@{1}\n".format(self.username,ip))
                            conn_log=str("Device: {0}".format(ip))
                            time.sleep(6)
                            output=cisco.read_channel()
                            if 'ssword' in output:
                                cisco.write_channel(self.password+'\n')
                            else:
                                time.sleep(10)
                                output=cisco.read_channel()
                                if 'ssword' in output:
                                    cisco.write_channel(self.password+'\n')
                                    self.lbl_progress.setStyleSheet("QLabel {color: red}") 
                                    #print('output-text->'+output+'<-output-text')
                                    output=cisco.write_channel("ssh -o StrictHostKeyChecking=no {0}@{1}\n".format(self.username,ip))
                                    #print('output-text->'+output+'<-output-text')
                                    if not output:
                                        cisco.write_channel('\x03')
                                        self.lbl_progress.setText("Connection to {0} timed out".format(ip))
                                        log_file.write("\nAccess to device:{0} -> Timed out \n".format(ip,output))
                                        time.sleep(2)
                                        auth_failure=False
                                        update_progress(index,self.last_item)
                                        if self.rsa_chk or self.jumpserver_chk:
                                            time.sleep(12)
                                        continue
                                    else:
                                        cisco.write_channel('\x03')
                                        self.lbl_progress.setText("Unable to access device {0}, details are logged".format(ip))
                                        log_file.write("\nUnable to access device:{0} -> {1} \n".format(ip,output))
                                        time.sleep(2)
                                        auth_failure=False
                                        update_progress(index,self.last_item)
                                        if self.rsa_chk or self.jumpserver_chk:
                                            time.sleep(14)
                                        continue
                            out=cisco.read_channel()
                            log_file.write(out)              
                            self.lbl_progress.setStyleSheet("QLabel {color: green}") 
                            self.lbl_progress.setText("Connected to {0}".format(ip))
                            
                            #IOS and ASA Seperation
                            
                            redispatch(cisco, device_type=device_type)
                            '''output=cisco.send_command('enable',auto_find_prompt=False)
                            time.sleep(7)
                            if 'ssword' in output:
                                cisco.send_command_expect(self.password)'''


                            if cisco.check_enable_mode():
                                #print("In enable mode already!, skipping enable command")
                                pass
                            else:
                                try:
                                    #redispatch(cisco, device_type='linux')
                                    cisco.enable()
                                except Exception as e:
                                    log_file.write(str(e))
                                    print('{0}'.format(str(e)))
                                    config_list.append('No')
                                    update_progress(index,self.last_item)
                                    if self.rsa_chk or self.jumpserver_chk:
                                        time.sleep(14)
                                    continue
                                #cisco.write_channel('enable\n')
                                #time.sleep(6)
                            
                            #output=cisco.read_channel()
                            #print(output,output[-1])
                            '''if str(output[-1])=='>':
                                cisco.write_channel('enable\n')
                                output=cisco.read_channel()
                                time.sleep(7)
                                if 'ssword' in output:
                                    cisco.write_channel(self.password+'\n')
                                else:
                                    self.lbl_progress.setText("Unable to enable mode, timed out!".format(ip))
                                    log_file.write("\nUnable to enter enable mode:{0} -> {1} \n".format(ip,output))
                                    time.sleep(2)
                                    auth_failure=False
                                    update_progress(index,self.last_item)
                                    continue
                            redispatch(cisco, device_type=device_type)'''
                            
                            hostname=cisco.find_prompt()
                            hostname=hostname[:-1]
                            
                            decorate(Fore.CYAN,"Device: {0} -{2} from Jumpserver: {1}".format(ip,self.syslog_ip,hostname.upper()),"*")
                            auth_failure=False
                            auth_count=0


                            if self.bulk_chk:
                                if device_type =='cisco_asa':
                                    filename="asa"
                                    
                                elif device_type=='cisco_ios':
                                    filename="ios"
                                elif device_type=='cisco_nxos':
                                    filename="nexus"
                            else:
                                filename=ip

                            
                                
                            if self.host_chk:
                                if '{0}/{1}.txt'.format(self.export_dir,filename):
                                    f=open("{0}/{1}.txt".format(self.export_dir,filename))
                                    
                                    file_list1=f.readlines()
                                    #print(file_list)
                                    file_hostname=file_list[0][1:].rstrip()
                                    file_hostname=file_hostname.lower()
                                    #print(file_hostname)
                                    if hostname.lower()!=file_hostname:
                                        self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                        self.lbl_export.setText("hostname mismatch! <{0}> doesn't match with device hostname: <{1}> ...ABORTING!!..".format(file_hostname.lower(),hostname.lower()))
                                        log_file.write("\nhostname mismatch! <{0}> doesn't match with device <{1}> ...ABORTING!!..".format(file_hostname.lower(),hostname.lower()))
                                        print(Fore.RED+"\nhostname mismatch! <{0}> doesn't match with device <{1}> ...ABORTING!!..".format(file_hostname.lower(),hostname.lower()))
                                        host_list.append(hostname)
                                        config_list.append('No (Hostname mismatch)')
                                        cpu_list.append('NA')
                                        ip_list.append(ip)
                                        memory_list.append('NA')
                                        time.sleep(2)
                                        auth_failure=False
                                        update_progress(index,self.last_item)
                                        if self.rsa_chk or self.jumpserver_chk:
                                            time.sleep(10)
                                        continue
                                    else:
                                        pass
                                else:
                                    self.lbl_export.setText("File {0}.txt not found in directory:{1}".format(self.export_dir,ip))
                                    auth_failure=False
                                    update_progress(index,self.last_item)
                                    if self.rsa_chk or self.jumpserver_chk:
                                        time.sleep(10)
                                    continue    

                            host_list.append(hostname)
                            
                            cpu,memory=health_check(cisco,ip,device_type)
                            
                            
                            print(Back.BLUE+Fore.WHITE+"Current CPU  Usage  : {0}%".format(cpu))
                            print(Back.BLUE+Fore.WHITE+"Current Memory used : {0}%".format(memory))
                            print(Back.RESET)
                            #print(cpu,memory)
                            cpu_list.append(cpu)
                            ip_list.append(ip)
                            memory_list.append(memory)
                            
                            if cpu >self.cpu_value or memory>self.memory_value:
                                self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                self.lbl_export.setText('CPU or Memory is high! CPU:{0}% Memory:{1}% ..aborting...'.format(cpu,memory))
                                log_file.write('\nCPU or Memory is high! CPU:{0}% Memory:{1}% ..aborting...\n'.format(cpu,memory))
                                print(Fore.RED+'\nCPU or Memory is high! CPU:{0}% Memory:{1}% ..aborting...\n'.format(cpu,memory))
                                config_list.append('No')
                                self.lbl_export.setStyleSheet("QLabel {color: brown}")   
                                update_progress(index,self.last_item)
                                if self.rsa_chk or self.jumpserver_chk:
                                    time.sleep(10)
                                continue
                            else:
                                if device_type=='cisco_asa':
                                   
                                    role=check_failover(cisco,ip,device_type)
                                    if role=='Standby':
                                        self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                        self.lbl_export.setText('Standby ASA firewall. aborting... ')
                                        log_file.write('Standby ASA firewall. aborting... ')
                                        print(Fore.RED+'\nStandby ASA firewall. aborting...')
                                        config_list.append('No')
                                        update_progress(index,self.last_item)
                                        if self.rsa_chk or self.jumpserver_chk:
                                            time.sleep(10)
                                        continue
                                #config_file=open('{0}/{1}.txt'.format(self.export_dir,ip),'r')
                                #self.input_cmd=config_file.readlines()
                                # SET PAGER
                                
                                self.change_success=configure_device(cisco,ip,device_type,filename)
                                if self.change_success=="success":

                                    count+=1
                                    self.counter.display(count)
                                output=cisco.write_channel('logout\n')
                                #print(output)
                                redispatch(cisco,device_type='linux')
                                cisco.disconnect()
                                auth_failure=False
                                update_progress(index,self.last_item)

                        except Exception as e:
                            if 'Authentication failure' in str(e):
                                auth_count=auth_count+1
                                #print(auth_count)
                                
                                if auth_count>2:
                                    self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                    self.lbl_export.setText(" Program terminated!!")

                                    self.lbl_progress.setStyleSheet("QLabel {color: red}")
                                    self.lbl_progress.setText("Authentication Failure in more than 2 devices..  Program Terminated!!")
                                    print(Fore.RED+"\nAuthentication Failure in more than 2 consecutive devices..  Program Terminated!!")
                                    log_file.close()
                                    self.START.setStyleSheet("blue")
                                    self.START.setText('START')
                                    break
                                
                                self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                self.lbl_export.setText(" Login failure  device: {0}".format(ip))

                                self.lbl_progress.setStyleSheet("QLabel {color: red}")
                                self.lbl_progress.setText("Authentication Failure ! ")
                                auth_failure=True
                                log_file.write(str(e))
                                print(Fore.RED+Style.BRIGHT+'\n{0}'.format(str(e)))
                                continue
                            else:
                                auth_failure=False
                                auth_count=0
                            self.lbl_progress.setStyleSheet("QLabel {color: red}")
                            self.lbl_progress.setText("Error: {0}".format(e))
                            print('{0}'.format(str(e)))
                            log_file.write('\n')                        
                            log_file.write(str(e))
                            log_file.write('\n')
                            time.sleep(2)
                            
                    except Exception as e:
                            if 'Authentication failure' in str(e):
                                auth_count=auth_count+1
                                #print(auth_count)
                                
                                if auth_count>2:
                                    self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                    self.lbl_export.setText(" Program terminated!!")

                                    self.lbl_progress.setStyleSheet("QLabel {color: red}")
                                    self.lbl_progress.setText("Authentication Failure in more than 2 devices..  Program Terminated!!")
                                    log_file.close()
                                    self.START.setStyleSheet("blue")
                                    self.START.setText('START')
                                    print(Fore.RED+"\nAuthentication Failure in more than 2 consecutive devices..  Program Terminated!!")
                                    break
                                
                                self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                self.lbl_export.setText(" Login failure  device: {0}".format(ip))

                                self.lbl_progress.setStyleSheet("QLabel {color: red}")
                                self.lbl_progress.setText("Authentication Failure ! ")

                                auth_failure=True
                                log_file.write(str(e))
                                print(Fore.RED+Style.BRIGHT+'\n{0}'.format(str(e)))
                                continue
                            else:
                                auth_failure=False
                                auth_count=0
                                conn_log=str("Device: {0}".format(ip))
                                log_file.write('\n'+"-"*len(conn_log)+'\n')
                                log_file.write(conn_log+'\n')                        
                                log_file.write("-"*len(conn_log)+'\n')
                                log_file.write('\n\n')                        
                                log_file.write(str(e))
                                log_file.write('\n')
                                print(Fore.RED+'\n{0}'.format(str(e)))

                else:
                    try:
                        
                        if self.rsa_chk:
                                
                                    self.rsaTick.emit("need RSA")
                                    time.sleep(3)
                                    self.rsaTick.connect(self.whatisRSAvalue)
                                    time.sleep(7)                            
                                    self.password = self.rsa_key
                                    self.enable_secret = self.rsa_key
                            

                        
                            
                            
                        else:
                            pass

                        dev={'device_type':device_type, 'ip':ip,'username':self.username,'password':self.password,'port':22,'secret':self.enable_secret,'global_delay_factor':2}
                        conn_log=str("Device: {0}".format(ip))
                        log_file.write('\n'+"-"*len(conn_log)+'\n')
                        log_file.write(conn_log+'\n')                        
                        log_file.write("-"*len(conn_log)+'\n')
                        self.lbl_progress.setStyleSheet("QLabel {color: black}") 
                        
                        self.lbl_progress.setText("Connecting to {0}".format(ip))
                        cisco=ConnectHandler(**dev)
                        if cisco.check_enable_mode():
                            #print("In enable mode already!, skipping enable command")
                            pass
                        else:
                            cisco.enable()
                        hostname=cisco.find_prompt()
                        hostname=hostname[:-1]
                        decorate(Fore.CYAN,"Device: {0} - {1}".format(ip,hostname.upper()),"*")
                        auth_failure=False
                        auth_count=0
                        #print("Host:{0}".format(hostname))

                        if self.bulk_chk:
                            if device_type =='cisco_asa':
                                filename="asa"
                                
                            elif device_type=='cisco_ios':
                                filename="ios"
                            elif device_type=='cisco_nxos':
                                filename="nexus"
                        else:
                            filename=ip


                        if self.host_chk:
                            if '{0}/{1}.txt'.format(self.export_dir,filename):
                                f=open("{0}/{1}.txt".format(self.export_dir,filename))
                                file_list=f.readlines()
                                #print(file_list)
                                file_hostname=file_list[0][1:].rstrip()
                                file_hostname=file_hostname.lower()
                                #print(file_hostname)
                                if hostname.lower()!=file_hostname:
                                    self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                    self.lbl_export.setText("hostname mismatch! <{0}> doesn't match with device  <{1}> ...ABORTING!!..".format(file_hostname.lower(),hostname.lower()))
                                    log_file.write("\nhostname mismatch! <{0}> doesn't match with device  <{1}> ...ABORTING!!..".format(file_hostname.lower(),hostname.lower()))
                                    print(Fore.RED+"\nhostname mismatch! <{0}> doesn't match with device <{1}> ...ABORTING!!..".format(file_hostname.lower(),hostname.lower()))

                                    time.sleep(2)
                                    f.close()
                                    update_progress(index,self.last_item)
                                    if self.rsa_chk or self.jumpserver_chk:
                                        time.sleep(10)
                                    continue
                                else:
                                    f.close()
                                    pass
                            else:
                                self.lbl_export.setText("File {0}.txt not found in directory:{1}".format(self.export_dir,ip))
                                update_progress(index,self.last_item)
                                if self.rsa_chk or self.jumpserver_chk:
                                    time.sleep(10)
                                continue                                                    
                        time.sleep(1)                       
                        self.lbl_progress.setStyleSheet("QLabel {color: green}") 
                        self.lbl_progress.setText("Connected to {0}".format(ip))
                        
                        cpu,memory=health_check(cisco,ip,device_type)
                        print(Back.BLUE+Fore.WHITE+"Current CPU  Usage  : {0}%".format(cpu))
                        print(Back.BLUE+Fore.WHITE+"Current Memory used : {0}%".format(memory))
                        print(Back.RESET)
                        host_list.append(hostname)
                        ip_list.append(ip)
                        cpu_list.append(cpu)
                        memory_list.append(memory)
                        #print(host_list,ip_list,memory_list,cpu_list)
                        #print(type(cpu),type(memory))
                        if cpu >self.cpu_value or memory >self.memory_value:
                            self.lbl_export.setStyleSheet("QLabel {color: red}") 
                            self.lbl_export.setText('CPU or Memory is high! CPU:{0}% Memory:{1}%..aborting...'.format(cpu,memory))
                            log_file.write('\nCPU or Memory is high! CPU:{0}% Memory:{1}% ..aborting...\n'.format(cpu,memory))
                            print(Fore.RED+'\nCPU or Memory is high! CPU:{0}% Memory:{1}% ..aborting...\n'.format(cpu,memory))
                            config_list.append('No')
                            self.lbl_export.setStyleSheet("QLabel {color: brown}")
                            update_progress(index,self.last_item)
                            if self.rsa_chk or self.jumpserver_chk:
                                time.sleep(10)
                            continue
                        else:
                            if device_type=='cisco_asa':
                                role=check_failover(cisco,ip,device_type)
                                if role=='Standby':
                                    self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                    self.lbl_export.setText('Standby ASA firewall. aborting... ')
                                    log_file.write('Standby ASA firewall. aborting... ')
                                    print(Fore.RED,'\nStandby ASA firewall. aborting')
                                    config_list.append('No')
                                    update_progress(index,self.last_item)
                                    if self.rsa_chk or self.jumpserver_chk:
                                        time.sleep(10)
                                    continue
                            
                            self.change_success=configure_device(cisco,ip,device_type,filename)
                            #config_file=open('{0}/{1}.txt'.format(self.export_dir,ip),'r')
                            #self.input_cmd=config_file.readlines()
                            # SET PAGER
                            if self.change_success=="success":
                                count+=1
                                self.counter.display(count)
                            update_progress(index,self.last_item)
                            
                    #except NetMikoAuthenticationException:
                     #       self.lbl_progress.setStyleSheet("QLabel {color: red}")
                      #      self.lbl_progress.setText("Authentication Failure ! Program terminated!")
                       #     self.upload.setText('Upload && Run')
                        #    auth_failure=True

                         #   break 
                    except Exception as e:
                            if 'Authentication failure' in str(e):
                                auth_count=auth_count+1
                                #print(auth_count)
                                
                                if auth_count>2:
                                    self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                    self.lbl_export.setText(" Program terminated!!")

                                    self.lbl_progress.setStyleSheet("QLabel {color: red}")
                                    self.lbl_progress.setText("Authentication Failure in more than 2 consecutive devices..  Program Terminated!!")
                                    print(Fore.RED+"\nAuthentication Failure in more than 2 consecutive devices..  Program Terminated!!")
                                    log_file.close()
                                    self.START.setStyleSheet("blue")
                                    self.START.setText('START')
                                    break
                                
                                self.lbl_export.setStyleSheet("QLabel {color: red}") 
                                self.lbl_export.setText(" Login failure  device: {0}".format(ip))
                                print(Fore.RED+Style.BRIGHT+'\n{0}'.format(str(e)))

                                self.lbl_progress.setStyleSheet("QLabel {color: red}")
                                self.lbl_progress.setText("Authentication Failure ! ")
                                auth_failure=True
                                log_file.write(str(e))
                                
                                continue
                            else:
                                auth_failure=False
                                auth_count=0

                            self.lbl_progress.setStyleSheet("QLabel {color: red}")
                            self.lbl_progress.setText("Error: {0}".format(e))
                            print(Fore.RED+'\n{0}'.format(str(e)))
                            log_file.write(str(e))
                            log_file.write('\n')
                            time.sleep(2)
                            update_progress(index,self.last_item)
                            if self.rsa_chk or self.jumpserver_chk:
                                time.sleep(10)
                            continue
                
                #auth_failure=False
                



            if auth_failure:
                #print("Authentication Failure! program terminated!!")
                #self.START.setStyleSheet("blue")

                self.START.setText('START')
                update_progress(100,100)
                pass
            #print(host_list,ip_list,config_list,cpu_list,memory_list)
            
            else:         
                collect_df=pd.DataFrame({'Hostname': host_list})    
                collect_df['IP']=ip_list
                collect_df['Config Pushed?']=config_list
                collect_df['CPU %']=cpu_list
                collect_df['Memory%']=memory_list

                collect_df.index=list(range(1,len(collect_df)+1))

                collect_df.to_excel(self.export_dir+'/Implementation_report-{0}_{1}.xlsx'.format(date_today,time_now))
                #imp_report.to_excel(self.export_dir+'/Implementation_report.xlsx')
                #self.lbl_export.setStyleSheet("QLabel {color: blue}")
                self.lbl_export.setText('Output saved in: {0}'.format(self.export_dir))

                #self.lbl_progress.setStyleSheet("QLabel {color: brown}")
                self.lbl_progress.setText('Done! Implementing devices.')
                end_time = time.time()
                elapsed = end_time - start_time
                elapsed=str(datetime.timedelta(seconds=elapsed))
                decorate(Fore.WHITE,'!! DONE. Elapsed Time: {0}'.format(elapsed),'#')
                #self.lbl_export.setStyleSheet("QLabel {color: blue}")
                #self.START.setStyleSheet("blue")
                
                self.START.setText('START')
                log_file.close()

        except FileNotFoundError:
            #print("File is either missing or selection cancelled!")
            self.lbl_progress.setText("Devices file is missing or selection cancelled!")
            print(Fore.RED+"Devices file is missing or selection cancelled!")
            #self.START.setStyleSheet("blue")
            self.START.setText('START')

        except Exception as e:
            self.lbl_progress.setText("Error: {0}".format(e))
            print(Fore.RED+'\n{0}'.format(str(e)))

            script_error.write(str(e))
            script_error.write('\n')
            #self.START.setStyleSheet("blue")
            self.START.setText('START')
        script_error.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

