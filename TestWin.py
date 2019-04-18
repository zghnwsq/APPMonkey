import sys
from PyQt5.QtCore import pyqtSlot, QFileInfo, QUrl
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
# from AppMonkey import *
import os
import time
import subprocess


class GetStat:
    def __init__(self):
        self.cpu = 0
        self.acpu = 0
        self.amem = 0
        self.mem = 0

    def run(self, app):
        # p = os.popen('adb shell top -m 1 -n 1 -t | grep System')
        if app.strip():
            cmd = 'adb shell top -n 1 | grep -e System -e ' + app
        else:
            cmd = 'adb shell top -n 1 | grep -e System'
        p = os.popen(cmd)
        a = p.readline()
        b = a.split(',')
        user = b[0].strip().split(' ')[1].replace('%', '')
        system = b[1].strip().split(' ')[1].replace('%', '')
        try:
            self.cpu = float(user) + float(system)
            print('cpu:'+str(self.cpu))
        except Exception as e:
            pass
        if app.strip():
            try:
                a1 = p.readline().strip()
                b1 = a1.split()[4]
                self.acpu = float(b1.strip().replace('%', ''))
            except Exception as e:
                pass
            print('acpu:'+str(self.acpu))

        # p2 = os.popen('adb shell dumpsys meminfo|grep  -e calculator -e "Total RAM"')
        # a2 = p2.readline().strip().split()
        # try:
        #     self.amem = a2[0].replace(',', '').replace('K:', '')
        #     p2.readline()
        #     b2 = p2.readline().strip().split()[2].replace(',', '').replace('K', '')
        #     self.mem = int(b2)
        #     print('amem:'+str(self.amem))
        # except Exception as e:
        #     pass

        # p1 = os.popen('adb shell dumpsys cpuinfo |grep  calculator')
        # a1 = p1.read().strip()
        # b1 = a1.split(' ')[0]
        # try:
        #     self.acpu = float(b1.strip().replace('%', ''))
        # except Exception as e:
        #     pass
        # print(self.acpu)


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
        # self.flag = 1
        print(value)
        t0 = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        if not os.path.isdir('./report/'):
            os.mkdir('./report/')
        sel = 'adb shell monkey '+value+' 1>./report/' + t0 + '_info.txt 2>./report/' + t0 + '_error.txt '
        print(sel)
        self.p = subprocess.Popen(sel, shell=True)
        # while self.flag:
        #     if p.poll() == 0:
        #         self.flag = 0

    @pyqtSlot(str, result=list)
    def Cpu(self, app):
        print('CPU')
        # thd = MyThread()
        # ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(ti)
        # t = ti.split(' ')[1]
        # thd.start()
        # thd.join()
        # c = thd.get_cpu()
        # print([t, str(c)])
        # # return [t, str(c)]
        # return str(c)
        g = GetStat()
        g.run(app)
        return [str(g.cpu), str(g.acpu)]


class MainWindow(QMainWindow):
    def __init__(self):
        self.value = ''
        super(QMainWindow, self).__init__()
        self.setWindowTitle("APP Monkey")
        #  相当于初始化这个加载web的控件
        self.view = QWebEngineView(self)
        #  加载外部页面，调用
        url = QFileInfo('.\\Monkey.html').absoluteFilePath()
        print(url)
        # self.view.load(QUrl('file:///'+url))
        self.view.load(QUrl(url))
        self.setCentralWidget(self.view)
        self.resize(1000, 600)


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

