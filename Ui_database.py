# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\duhua\Desktop\database\database.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main_Foram_Dialog(object):
    def setupUi(self, Main_Foram_Dialog):
        Main_Foram_Dialog.setObjectName("Main_Foram_Dialog")
        Main_Foram_Dialog.resize(823, 572)
        #Main_Foram_Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Main_Foram_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.select__groupBox = QtWidgets.QGroupBox(Main_Foram_Dialog)
        self.select__groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.select__groupBox.setFont(font)
        self.select__groupBox.setObjectName("select__groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.select__groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.selected_listWidget = QtWidgets.QListWidget(self.select__groupBox)
        self.selected_listWidget.setObjectName("selected_listWidget")
        self.horizontalLayout_6.addWidget(self.selected_listWidget)
        self.gridLayout.addWidget(self.select__groupBox, 0, 2, 1, 1)
        self.mat_groupBox = QtWidgets.QGroupBox(Main_Foram_Dialog)
        self.mat_groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mat_groupBox.setFont(font)
        self.mat_groupBox.setObjectName("mat_groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mat_groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mat_type_listWidget = QtWidgets.QListWidget(self.mat_groupBox)
        self.mat_type_listWidget.setObjectName("mat_type_listWidget")
        self.horizontalLayout_5.addWidget(self.mat_type_listWidget)
        self.gridLayout.addWidget(self.mat_groupBox, 0, 0, 1, 1)
        self.mat_content_groupBox = QtWidgets.QGroupBox(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mat_content_groupBox.setFont(font)
        self.mat_content_groupBox.setObjectName("mat_content_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mat_content_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.content_tableWidget = QtWidgets.QTableWidget(self.mat_content_groupBox)
        self.content_tableWidget.setObjectName("content_tableWidget")
        self.content_tableWidget.setColumnCount(0)
        self.content_tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.content_tableWidget)
        self.gridLayout.addWidget(self.mat_content_groupBox, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_pushButton = QtWidgets.QPushButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout_3.addWidget(self.add_pushButton)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.del_pushButton = QtWidgets.QPushButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.del_pushButton.setFont(font)
        self.del_pushButton.setObjectName("del_pushButton")
        self.horizontalLayout_3.addWidget(self.del_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.fresh_Button = QtWidgets.QPushButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.fresh_Button.setFont(font)
        self.fresh_Button.setObjectName("fresh_Button")
        self.horizontalLayout_3.addWidget(self.fresh_Button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Main_Foram_Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lib_comboBox = QtWidgets.QComboBox(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lib_comboBox.setFont(font)
        self.lib_comboBox.setObjectName("lib_comboBox")
        self.lib_comboBox.addItem("")
        self.lib_comboBox.addItem("")
        self.lib_comboBox.addItem("")
        self.lib_comboBox.addItem("")
        self.lib_comboBox.addItem("")
        self.lib_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.lib_comboBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(13, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MCNP_radioButton = QtWidgets.QRadioButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.MCNP_radioButton.setFont(font)
        self.MCNP_radioButton.setChecked(True)
        self.MCNP_radioButton.setObjectName("MCNP_radioButton")
        self.horizontalLayout.addWidget(self.MCNP_radioButton)
        self.RMC_radioButton = QtWidgets.QRadioButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RMC_radioButton.setFont(font)
        self.RMC_radioButton.setObjectName("RMC_radioButton")
        self.horizontalLayout.addWidget(self.RMC_radioButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_ok = QtWidgets.QPushButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setAutoFillBackground(True)
        self.pushButton_ok.setIconSize(QtCore.QSize(20, 16))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cacel = QtWidgets.QPushButton(Main_Foram_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cacel.setFont(font)
        self.pushButton_cacel.setObjectName("pushButton_cacel")
        self.horizontalLayout.addWidget(self.pushButton_cacel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        self.layoutWidget = QtWidgets.QWidget(Main_Foram_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(Main_Foram_Dialog)
        self.pushButton_cacel.clicked.connect(Main_Foram_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Main_Foram_Dialog)

    def retranslateUi(self, Main_Foram_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Main_Foram_Dialog.setWindowTitle(_translate("Main_Foram_Dialog", "材料卡生成器"))
        self.select__groupBox.setTitle(_translate("Main_Foram_Dialog", "已选择"))
        self.mat_groupBox.setTitle(_translate("Main_Foram_Dialog", "材料库"))
        self.mat_content_groupBox.setTitle(_translate("Main_Foram_Dialog", "材料成分"))
        self.add_pushButton.setText(_translate("Main_Foram_Dialog", "添加材料"))
        self.del_pushButton.setText(_translate("Main_Foram_Dialog", "删除材料"))
        self.fresh_Button.setText(_translate("Main_Foram_Dialog", "刷新"))
        self.label.setText(_translate("Main_Foram_Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">选择数据库：</span></p></body></html>"))
        self.lib_comboBox.setItemText(0, _translate("Main_Foram_Dialog", ".21c"))
        self.lib_comboBox.setItemText(1, _translate("Main_Foram_Dialog", ".30c"))
        self.lib_comboBox.setItemText(2, _translate("Main_Foram_Dialog", ".31c"))
        self.lib_comboBox.setItemText(3, _translate("Main_Foram_Dialog", "42.c"))
        self.lib_comboBox.setItemText(4, _translate("Main_Foram_Dialog", "49.c"))
        self.lib_comboBox.setItemText(5, _translate("Main_Foram_Dialog", "50.c"))
        self.MCNP_radioButton.setText(_translate("Main_Foram_Dialog", "MCNP"))
        self.RMC_radioButton.setText(_translate("Main_Foram_Dialog", "RMC"))
        self.pushButton_ok.setText(_translate("Main_Foram_Dialog", "生成材料卡"))
        self.pushButton_cacel.setText(_translate("Main_Foram_Dialog", "退出"))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Foram_Dialog = QtWidgets.QWidget()
    ui = Ui_Main_Foram_Dialog()
    ui.setupUi(Main_Foram_Dialog)
    Main_Foram_Dialog.show()
    sys.exit(app.exec_())