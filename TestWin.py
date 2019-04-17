import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel
from AppMonkey import *
import os
import time


class MyShareObject(QWidget):
    def __init__(self):
        super().__init__()
        self.value = ''
        self.flag = 1

    @pyqtSlot(result=str)
    def QtToWeb(self):
        print('456')
        return 'back to web'

    @pyqtSlot(str, result=str)
    def WebToQt(self, value):
        print(value)
        self.value = value
        return value

    @pyqtSlot(str)
    def Run(self, value):
        self.flag = 1
        print(value)
        t0 = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        sel = 'adb shell monkey '+value+' 1>./report/' + t0 + '_info.txt 2>./report/' + t0 + '_error.txt '
        print(sel)
        p = subprocess.Popen(sel, shell=True)
        while self.flag:
            if p.poll() == 0:
                self.flag = 0

    @pyqtSlot(result=str)
    def Cpu(self):
        print('CPU')
        thd = MyThread()
        ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(ti)
        t = ti.split(' ')[1]
        thd.start()
        thd.join()
        c = thd.get_cpu()
        print([t, str(c)])
        # return [t, str(c)]
        return str(c)


class MainWindow(QMainWindow):
    def __init__(self):
        self.value = ''
        super(QMainWindow, self).__init__()
        self.setWindowTitle("APPMonkey")
        #  相当于初始化这个加载web的控件
        self.view = QWebEngineView(self)
        #  加载外部页面，调用
        url = QFileInfo('./Monkey.html').absoluteFilePath()
        print(url)
        self.view.load(QUrl('file:///'+url))
        self.setCentralWidget(self.view)
        self.resize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    channel = QWebChannel()
    share = MyShareObject()
    # share.con.connect()
    channel.registerObject('share', share)
    win.view.page().setWebChannel(channel)
    win.show()
    sys.exit(app.exec_())

