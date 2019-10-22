# -*- coding: utf-8 -*-
#
# Created by: DuHua 2018-7-5
#
# The main function of this GUI is generate MCNP material cards
"""
Module implementing vol_fra_input_Dialog.
"""
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QFont,QColor,QBrush,QPalette
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QMessageBox,QApplication,QTableWidgetItem,QTableWidget,QHeaderView,QFileDialog
from Ui_database import Ui_Main_Foram_Dialog
from Ui_input import Ui_vol_fra_input_Dialog
from Ui_database_input import Ui_Database_Dialog
import os
import os.path
import sqlite3
import re

class Main_Foram_Dialog(QtWidgets.QWidget):
	"""
	Class documentation goes here.
	"""
	def __init__(self, parent=None):
		"""
		Constructor
		@param parent reference to the parent widget
		@type QWidget
		"""
		super(Main_Foram_Dialog, self).__init__(parent)
		self.UI=Ui_Main_Foram_Dialog()
		self.UI.setupUi(self)
		#设置背景
		self.main_p = QPalette()
		self.main_p.setColor(QPalette.Background,QColor('#87CEFA'))
		self.setAutoFillBackground(True)
		self.setPalette(self.main_p)
		self.material_content=[]
		
		#初始化mat_type_listWidget
		self.update_database()		
		# if items in mat_type_listWidget are selected, get_item is activated
		self.UI.add_pushButton.clicked.connect(lambda: self.add_item_to_database())
		self.UI.mat_type_listWidget.itemClicked.connect(lambda: self.get_item())
		self.UI.pushButton_ok.clicked.connect(lambda: self.write_result())
		self.UI.fresh_Button.clicked.connect(lambda: self.fresh())
		self.UI.mat_type_listWidget.itemClicked.connect(lambda: self.set_content_tableWidget())
		self.UI.del_pushButton.clicked.connect(lambda: self.del_database())
	
	#弹出添加数据库窗口	
	def add_item_to_database(self):
		self.db_input=Ui_Database_Dialog()
		self.main_db_input = QtWidgets.QWidget()
		self.db_input.setupUi(self.main_db_input)
		self.main_db_input.show()
		self.main_db_input.resize(470,540)
		self.main_db_input.setFixedSize(470,540)
		#设置背景
		self.main_p = QPalette()
		self.main_p.setColor(QPalette.Background,QColor('#C1CDCD'))
		self.main_db_input.setAutoFillBackground(True)
		self.main_db_input.setPalette(self.main_p)
		#在content_tableWidget中设置表头
		horizontalHeader = ['ZAID','Nuclide_Name','Ion_Density']
		self.db_input.db_tableWidget.setColumnCount(len(horizontalHeader))              #设置列数
		self.db_input.db_tableWidget.setHorizontalHeaderLabels(horizontalHeader)	#添加表头
		
		#self.db_input.db_ok_pushButton.setEnabled(False)
		self.db_input.import_excel_pushButton.clicked.connect(lambda: self.set_db_tab_widget_from_excel())
		self.db_input.db_cacel_pushButton.clicked.connect(self.main_db_input.close)		
		self.db_input.db_ok_pushButton.clicked.connect(lambda: self.add_database())
		self.db_input.add_pushButton.clicked.connect(lambda: self.addrow())
		self.db_input.del_pushButton.clicked.connect(lambda: self.delrow())
	
	#在数据库窗口中添加行
	def addrow(self):
		current_row=self.db_input.db_tableWidget.currentRow()
		if current_row== -1:
			current_row=self.db_input.db_tableWidget.rowCount()
		self.db_input.db_tableWidget.insertRow(current_row)
	
	#在数据库窗口中删除行
	def delrow(self):
		current_row=self.db_input.db_tableWidget.currentRow()
		if current_row != -1:
			self.db_input.db_tableWidget.removeRow(current_row)
			
	#db_tableWidget数据是否合法
	def judge_format_correct(self):
		flag=True
		for i in range(self.db_input.db_tableWidget.rowCount()):
			try:
				ZAID=self.db_input.db_tableWidget.item(i,0).text()
				Nuclide_Name=self.db_input.db_tableWidget.item(i,1).text()
				Ion_Density=self.db_input.db_tableWidget.item(i,2).text()
				float_Ion_Density=float(Ion_Density)
			except:
				flag=False
			else:
				if not ZAID or not Nuclide_Name or not float_Ion_Density:
					flag=False
		return flag
	
	#删除数据库
	def del_database(self):
		table_name=self.UI.mat_type_listWidget.currentItem().text()
		reply = QMessageBox.question(self,'提示','确定要删除材料: %s '%table_name, QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			conn = sqlite3.connect('data.db')
			cur = conn.cursor()
			sql='DROP TABLE %s'%table_name
			cur.execute(sql)		
			cur.close()
			conn.commit()
			conn.close()
			#更新mat_type_listWidget列表
			self.update_database()
			self.UI.content_tableWidget.setColumnCount(0)     #清空content_tableWidget
			self.UI.content_tableWidget.setRowCount	(0) 
		else:
			pass
		
	#更新数据库
	def update_database(self):
		#初始化mat_type_listWidget
		self.UI.mat_type_listWidget.clear()
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		sql="SELECT name FROM sqlite_master WHERE type='table' order by name"
		cur.execute(sql)
		item=cur.fetchall()
		for lst in item:
			self.UI.mat_type_listWidget.addItem(lst[0])
		cur.close()
		conn.commit()
		conn.close()
	
	#警告对话框
	def warning_dlg(self,text):
		msgBox = QMessageBox()
		msgBox.setWindowTitle('警告')
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setText("%s"%text)
		msgBox.setStandardButtons(QMessageBox.Ok)
		reply = msgBox.exec()
	
	#数据库窗口，从Excel中读取数据，并写去到db_tableWidget
	def set_db_tab_widget_from_excel(self):
		db_text=self.db_input.db_name_lineEdit.text()
		try:
			database_name=db_text
			insert_data=self.read_txt(db_text)	
			#在content_tableWidget中写数据
			horizontalHeader = ['ZAID','Nuclide_Name','Ion_Density']
			self.db_input.db_tableWidget.setColumnCount(len(horizontalHeader))              #设置列数
			self.db_input.db_tableWidget.setRowCount(len(insert_data[0]))                   #设置行数
			self.db_input.db_tableWidget.setHorizontalHeaderLabels(horizontalHeader)	#添加表头
			for i in range(self.db_input.db_tableWidget.rowCount()):
				for j in range(self.db_input.db_tableWidget.columnCount()):
					self.db_input.db_tableWidget.setItem(i,j, QTableWidgetItem(insert_data[j][i])) #写入数据
			flag=self.judge_format_correct()
			if flag and db_text:
				self.db_input.db_name_lineEdit.setEnabled(False)

			#设置tableWidget格式		
			for index in range(self.db_input.db_tableWidget.columnCount()):
				headItem = self.db_input.db_tableWidget.horizontalHeaderItem(index)
				headItem.setFont(QFont("song", 12, QFont.Bold))
				headItem.setForeground(QColor(60,60,60))
				headItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
				self.db_input.db_tableWidget.resizeColumnsToContents()  
				self.db_input.db_tableWidget.resizeRowsToContents()
				self.db_input.db_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #自适应窗口
		except:
			self.warning_dlg("材料名称为空，请输入材料名称")		
		
	# 读取db_tableWidget数据，并写入到database中
	def add_database(self):
		flag=self.judge_format_correct()
		db_text=self.db_input.db_name_lineEdit.text()
		if db_text:
			if flag:
				table_name=db_text
				ZAID=[]
				Nuclide_Name=[]
				Ion_Density=[]			
				for i in range(self.db_input.db_tableWidget.rowCount()):
					ZAID.append(self.db_input.db_tableWidget.item(i,0).text())
					Nuclide_Name.append(self.db_input.db_tableWidget.item(i,1).text())
					Ion_Density.append(self.db_input.db_tableWidget.item(i,2).text())
				#连接数据库，创建游标
				conn = sqlite3.connect('data.db')
				cur = conn.cursor()
				sql="SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{0}'".format(table_name)
				cur.execute(sql)
				judge_if_exits_tab=cur.fetchall()[0][0] #如果存在返回1，否则返回0
				if judge_if_exits_tab:
					#sql='replace into %s(ZAID TEXT,NAME TEXT,Ion_Density REAL) values(?,?,?)'%table_name
					#cur.executemany(sql, self.generate_tuple_data(ZAID,Nuclide_Name,Ion_Density))
					#如果表存在，先删除
					sql='DROP TABLE %s'%table_name
					cur.execute(sql)
					sql='CREATE TABLE %s(ZAID TEXT,NAME TEXT,Ion_Density REAL)'%table_name
					cur.execute(sql)
					#批量导入，减少提交事务的次数，可以提高速度
					sql = 'INSERT INTO %s VALUES(?,?,?)'%table_name
					cur.executemany(sql, self.generate_tuple_data(ZAID,Nuclide_Name,Ion_Density))
					cur.close()
					conn.commit()
					conn.close()				
				else:				
					sql='CREATE TABLE IF NOT EXISTS %s(ZAID TEXT,NAME TEXT,Ion_Density REAL)'%table_name
					cur.execute(sql)
					#批量导入，减少提交事务的次数，可以提高速度
					sql = 'INSERT INTO %s VALUES(?,?,?)'%table_name
					cur.executemany(sql, self.generate_tuple_data(ZAID,Nuclide_Name,Ion_Density))
					cur.close()
					conn.commit()
					conn.close()
				self.UI.mat_type_listWidget.addItem(table_name)
				self.main_db_input.close()    #关闭窗口
			else:
				self.warning_dlg("核子密度格式有误，请重新输入")
		else:
			self.warning_dlg("材料名称为空，请重新输入")

	#读取文本文件
	def read_txt(self,table_name):
		ZAID=[]
		Nuclide_Name=[]
		Ion_Density=[]			
		file_dir=os.getcwd()
		filename, _ = QFileDialog.getOpenFileName(self, 'Open file', './')
		with open(filename, 'r') as f:
			pattern=re.compile(r'(\w+)\s+(\w+)\s+(\d{1,}(\.\d{1,})?([E,e][-]?\d*)?)')
			for line in f:
				line=line.strip()
				serch_mark=pattern.search(line)
				try:
					ZAID.append(serch_mark.group(1))
					Nuclide_Name.append(serch_mark.group(2))
					Ion_Density_str = "{:<.8e}".format(float(serch_mark.group(3)))
					Ion_Density.append(Ion_Density_str)
				except:
					continue
			insert_data=[ZAID,Nuclide_Name,Ion_Density]
			f.close()
			return insert_data				
		
		#读取Excel文件	
		#wb = openpyxl.load_workbook(filename,data_only=True)  #data_only=True可以将公式转化为数值
		#ws = wb.get_sheet_by_name(table_name)
		#contents=[]
		#for column in list(ws.columns):
			#contents.append(column)
		#ZAID_item=contents[0][1:]            #第1列
		#Nuclide_Name_item=contents[1][1:]    #第2列
		#Ion_Density_item=contents[2][1:]     #第3列
		#ZAID=[]
		#Nuclide_Name=[]
		#Ion_Density=[]			
		#for i in range(len(ZAID_item)):
			#ZAID.append(str(ZAID_item[i].value))
			#Nuclide_Name.append(str(Nuclide_Name_item[i].value))
			#Ion_Density_str='{:.5e}'.format(Ion_Density_item[i].value) 
			#Ion_Density.append(Ion_Density_str)	
		#insert_data=[ZAID,Nuclide_Name,Ion_Density]
		#return insert_data
		
		
	def generate_tuple_data(self,ZAID,Nuclide_Name,Ion_Density):
		for i in range(len(ZAID)):
			row=ZAID[i],Nuclide_Name[i],Ion_Density[i]
			yield tuple(row)		
	
	# pop sub dialog, and complete Interaction with main window
	def get_item(self):
		#str1=self.UI.mat_type_listWidget.currentItem().text()
		self.input_dialg=Ui_vol_fra_input_Dialog()
		self.dilag_main = QtWidgets.QWidget()
		self.input_dialg.setupUi(self.dilag_main)
		self.dilag_main.show()
		self.dilag_main.setFixedSize(400,180)
		self.input_dialg.ok_volume_pushButton.clicked.connect(lambda: self.get_LineEdit_content(self.input_dialg.volume_input_lineEdit.text()))
		self.input_dialg.cacel_volume_pushButton_2.clicked.connect(self.dilag_main.close)
	
	#get contents in input_dialg, and check if it is effective
	def get_LineEdit_content(self,item):
		is_digit_mark=re.match(r'\d{1,}(\.\d{1,})?',item)
		try:
			match_item=is_digit_mark.group(0)
			if len(match_item) == len(item):
				self.material_content.append(float(item))  #get contents ininput_dialg
				#print('material is {:<6.4f}'.format(float(item)))
				#self.ok_volume_pushButton.clicked.connect(lambda: self.set_material_content(material_content))
				self.dilag_main.close()       #hide sub window
				self.UI.selected_listWidget.addItem(self.UI.mat_type_listWidget.currentItem().text()) #set selected_listWidget item
				
			else:
				msgBox = QMessageBox()
				msgBox.setWindowTitle('警告')
				msgBox.setIcon(QMessageBox.Warning)
				msgBox.setText("输入数据类型错误，请重新输入一个数")
				msgBox.setStandardButtons(QMessageBox.Ok)
				reply = msgBox.exec()
				self.input_dialg.volume_input_lineEdit.setText('')  #if fail, set null 
		except:
			self.warning_dlg("输入数据类型错误，请重新输入一个数")		
	
	#从数据库读取数据并写到tableWidget中	
	def set_content_tableWidget(self):
		table_name=self.UI.mat_type_listWidget.currentItem().text()
		ZAID,Nuclide_Name,Ion_Density=self.read_database(table_name) #从数据库读取每个表
		insert_data=[ZAID,Nuclide_Name,Ion_Density] 
		#在content_tableWidget中写数据
		horizontalHeader = ['ZAID','Nuclide_Name','Ion_Density']
		self.UI.content_tableWidget.setColumnCount(len(horizontalHeader))       #设置列数
		self.UI.content_tableWidget.setRowCount(len(ZAID))                      #设置行数
		self.UI.content_tableWidget.setHorizontalHeaderLabels(horizontalHeader)	#添加表头
		for i in range(self.UI.content_tableWidget.rowCount()):
			for j in range(self.UI.content_tableWidget.columnCount()):
				self.UI.content_tableWidget.setItem(i,j, QTableWidgetItem(insert_data[j][i])) #写入数据
		#设置tableWidget格式		
		for index in range(self.UI.content_tableWidget.columnCount()):
			headItem = self.UI.content_tableWidget.horizontalHeaderItem(index)
			headItem.setFont(QFont("song", 12, QFont.Bold))
			headItem.setForeground(QColor(60,60,60))
			headItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
			self.UI.content_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers) #内容无法编辑
			self.UI.content_tableWidget.resizeColumnsToContents()  
			self.UI.content_tableWidget.resizeRowsToContents()
			self.UI.content_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #自适应窗口
	
	#结果写入到输出文件
	def write_result(self):
		if self.UI.MCNP_radioButton.isChecked():
			self.to_MCNP()
		elif self.UI.RMC_radioButton.isChecked():
			self.to_RMC()
	
	def to_RMC(self):
		Componet_material=[]
		Total_tad=0
		library_mark=self.UI.lib_comboBox.currentText()                      #获取lib_comboBox的内容
		b=self.UI.selected_listWidget.count()
		total_text=''
		for i in range(0, self.UI.selected_listWidget.count()):              #获取selected_listWidget中的所有内容
			table_name=self.UI.selected_listWidget.item(i).text()
			ZAID,Nuclide_Name,Ion_Density=self.read_database(table_name,self.material_content[i]) #从数据库读取每个表中的数据	
			Componet_material.append(table_name)
			Total_tad=Total_tad+eff_tad
			comment=['        // ********************************************//','        // ***      %s'%table_name,
			         '        // ***  volume fraction [%] - {0}'.format(self.material_content[i]),'        // ***  t.a.d. =  {:.5e}'.format(tad),
			         '        // ***  eff.tad = {:.5e}'.format(eff_tad),'        // ********************************************//\n']
			text='\n'.join(comment)
			#获取每种成分的数据
			for j in range(len(ZAID)):
				item=['        ', ZAID[j]+library_mark, Ion_Density[j],'//', Nuclide_Name[j]]
				line=' '.join(item)+'\n' 
				text=text+line
			#获取总的数据
			total_text=total_text+text
		num_componet=len(Componet_material)
		total_comment=['//  --------------------------------------------------------------------',
		               '//  Total has  {}  Componets material  '.format(num_componet),
		               '//  Total eff t.a.d   =   {:.8e}'.format(Total_tad),
		               '//  --------------------------------------------------------------------',
		               '        density = {:.8e}'.format(Total_tad),'        @zaid.xxx        fraction\n']
		total_comment='\n'.join(total_comment)
		output=total_comment+total_text
		path=os.getcwd()+'\output'
		folder = os.path.exists(path)
		if not folder:
			os.makedirs(path) 
		else:
			pass
		save_dir=path+'\output.txt'
		with open(save_dir, 'w') as fou:
			fou.write(output)
			fou.close()	
	
	def to_MCNP(self):
		Componet_material=[]
		Total_tad=0
		library_mark=self.UI.lib_comboBox.currentText()                      #获取lib_comboBox的内容
		b=self.UI.selected_listWidget.count()
		total_text=''
		for i in range(0, self.UI.selected_listWidget.count()):              #获取selected_listWidget中的所有内容
			table_name=self.UI.selected_listWidget.item(i).text()
			ZAID,Nuclide_Name,Ion_Density=self.read_database(table_name,self.material_content[i]) #从数据库读取每个表中的数据	
			Componet_material.append(table_name)
			Total_tad=Total_tad+eff_tad
			comment=['c ********************************************c','c ***      %s'%table_name,
			         'c ***  volume fraction [%] - {0}'.format(self.material_content[i]),'c ***  t.a.d. =  {:.5e}'.format(tad),
			         'c ***  eff.tad = {:.5e}'.format(eff_tad),'c ********************************************c\n']
			text='\n'.join(comment)
			#获取每种成分的数据
			for j in range(len(ZAID)):
				item=['        ', ZAID[j]+library_mark, Ion_Density[j],'$', Nuclide_Name[j]]
				line=' '.join(item)+'\n' 
				text=text+line
			#获取总的数据
			total_text=total_text+text
		num_componet=len(Componet_material)
		total_comment=['c  --------------------------------------------------------------------',
		               'c  Total has  {}  Componets material  '.format(num_componet),
		               'c  Total eff t.a.d   =   {:.8e}'.format(Total_tad),
		               'c  --------------------------------------------------------------------\n']
		total_comment='\n'.join(total_comment)
		output=total_comment+total_text
		path=os.getcwd()+'\output'
		folder = os.path.exists(path)
		if not folder:
			os.makedirs(path) 
		else:
			pass
		save_dir=path+'\output.txt'
		with open(save_dir, 'w') as fou:
			fou.write(output)
			fou.close()		
	
	#判断表是否在数据库中
	def if_exits_database(self,table_name):
		table_names=[]
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		sql="SELECT name FROM sqlite_master WHERE type='table' order by name"
		cur.execute(sql)
		item=cur.fetchall()
		for lst in item:
			table_names.append(lst[0])
		cur.close()
		conn.commit()
		conn.close()
		if table_name in table_names:
			flag=True
		else:
			flag=False
		return flag
		
	#完成从数据库读取每个表中的数据	
	def read_database(self,table_name,a=100):
		flag=self.if_exits_database(table_name)
		if flag:
			colume_frac=a	
			global tad
			global eff_tad		
			ZAID=[]
			Nuclide_Name=[]
			Ion_Density=[]
			tad=0
			eff_tad=0		
			#连接数据库，创建游标
			conn = sqlite3.connect('data.db')
			cur = conn.cursor()
			sql='SELECT * FROM %s'%table_name
			cursor =conn.execute(sql)
			for row in cursor:
				ZAID.append(row[0])
				Nuclide_Name.append(row[1])
				density='{:.8e}'.format(row[2]*colume_frac/100)       #乘以体积份额计算考虑占空比后的核子密度
				Ion_Density.append(density)
				tad=row[2]+tad                                        #计算总核子密度
				eff_tad=row[2]*colume_frac/100+eff_tad                #计算材料总的有效核子密度
			data=[ZAID,Nuclide_Name,Ion_Density]                          #每个表中的元素		
			conn.close()
			return data
		else:
			self.warning_dlg('表不存在')
		
	def fresh(self):
		self.material_content=[]
		self.UI.selected_listWidget.clear()
		self.UI.content_tableWidget.setColumnCount(0)                 #清空content_tableWidget
		self.UI.content_tableWidget.setRowCount(0)         
	
		
if __name__=="__main__":
	import sys
	app=QApplication(sys.argv)
	main_Fram=Main_Foram_Dialog()
	main_Fram.show()
	sys.exit(app.exec_())