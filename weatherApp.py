import sys
import random
import mysql.connector

from PyQt5.uic import loadUi
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QLabel, QTableWidget, QTableWidgetItem, QComboBox, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPointF
from datetime import datetime
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("buttontable.ui",self)
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.setFixedWidth(700)
        self.setFixedHeight(800)
        self.radioButton
        self.label_4.setText("Temperature displayed in Fahrenheit")
        self.create_linechart()

    def create_linechart(self):
        series = QLineSeries(self)

        series.append(0,10)
        series.append(1,50)
        series.append(2,90)

        series << QPointF(11,1)<<QPointF(13,3)<<QPointF(17,6)

        chart =  QChart()
 
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
 
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartview)
        

    def button1_clicked(self):
        #Connect to MySQL
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="weather"
        )
        
                 
        mycursor = mydb.cursor()
        if self.radioButton.isChecked():
            #Display temps in Celsius
            tempin = str(int(((random.randint(-20, 100)-32))*(5/9)))
            self.label_4.setText("Note: Temperatures displayed in degrees Celsius")
        else: 
            tempin = str(random.randint(-20, 100))     
        humin = str(random.randint(0, 100))
        now = datetime.now()
        timein = str(now.strftime("%H:%M:%S"))
        sql = "INSERT INTO weather (temperature, humidity, timestamp) VALUES (%s, %s, %s)"
        val = (tempin, humin, timein)
        mycursor.execute(sql, val)
        mydb.commit()

        if(int(tempin)>int(self.comboBox.currentText())):
            msg = QMessageBox()
            msg.setWindowTitle("Temperature alert!")
            msg.setText("Temperature is above set value!")
            x = msg.exec()
        
        if(int(humin)>int(self.comboBox_2.currentText())):
            hmsg = QMessageBox()
            hmsg.setWindowTitle("Humidity alert!")
            hmsg.setText("Humidity above set value!")
            x = hmsg.exec()

        mycursor.execute("SELECT * from weather ORDER BY id DESC LIMIT 1")
        myresult = mycursor.fetchall()
        
        self.tableWidget_2.setRowCount(1)
        tablerow=0
        for row in myresult:
            self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            tablerow+=1
          

    def button2_clicked(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="weather"
        )
        
        self.create_linechart()
        mycursor = mydb.cursor()        
        mycursor.execute("SELECT * from weather ORDER BY id DESC LIMIT 10")
        myresult = mycursor.fetchall()
        
        self.tableWidget.setRowCount(10)
        tablerow=0
        for row in myresult:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            tablerow+=1
    
# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")