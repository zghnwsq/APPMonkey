# coding:utf8

import os
import subprocess
import time
import threading


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.cpu = 0

    def run(self):
        p = os.popen('adb shell top -m 1 -n 1 -t | grep System')
        a = p.read()
        b = a.split(',')
        user = b[0].strip().split(' ')[1].replace('%', '')
        system = b[1].strip().split(' ')[1].replace('%', '')
        self.cpu = int(user) + int(system)

    def get_res(self):
        return self.cpu


if __name__ == '__main__':
    p = subprocess.Popen('adb shell monkey '
                         '-p com.miui.calculator '
                         '-v -v -v '
                         '--throttle 100 '
                         '-s 26 '
                         # '1>D:\\monkeyinfo.txt 2>D:\\monkeyerror.txt '
                         '1000')
    cpu = []
    flag = 1
    while flag:
        if p.poll() == 0:
            flag = 0
        ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        t = ti.split(' ')[1]
        thd = MyThread()
        thd.start()
        thd.join()
        # cpu.append(str(thd.get_res()))
        cpu.append([t, thd.get_res()])
    print(cpu)
    html = open('.\\LineGraph.html', mode='r', encoding='utf-8').read()
    data = ''
    for i in cpu:
        data += '["'+i[0]+'",'+str(i[1])+']'
        data += ','
    html = html.replace('%data', data)
    t = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    f = open('.\\' + t + '.html', mode='w', encoding='utf-8')
    f.write(html)
    f.close()


