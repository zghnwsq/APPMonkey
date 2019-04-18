# coding:utf8

import os
import subprocess
import time
import threading


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.cpu = 0
        self.acpu = 0
        self.amem = 0
        self.mem = 0

    def run(self):
        p = os.popen('adb shell top -m 1 -n 1 -t | grep System')
        a = p.read()
        b = a.split(',')
        user = b[0].strip().split(' ')[1].replace('%', '')
        system = b[1].strip().split(' ')[1].replace('%', '')
        try:
            self.cpu = float(user) + float(system)
            print('acpu:'+self.cpu)
        except Exception as e:
            pass

        p2 = os.popen('adb shell dumpsys meminfo|grep  -e calculator -e "Total RAM"')
        a2 = p2.readline().strip().split()
        try:
            self.amem = a2[0].replace(',', '').replace('K:', '')
            p2.readline()
            b2 = p2.readline().strip().split()[2].replace(',', '').replace('K', '')
            self.mem = int(b2)
            print('amem:'+self.amem)
        except Exception as e:
            pass

        p1 = os.popen('adb shell dumpsys cpuinfo |grep  calculator')
        a1 = p1.read().strip()
        b1 = a1.split(' ')[0]
        try:
            self.acpu = float(b1.strip().replace('%', ''))
        except Exception as e:
            pass
        print('acpu:'+self.acpu)

    def get_cpu(self):
        return self.cpu

    def get_acpu(self):
        return self.acpu

    def get_amem(self):
        return self.amem

    def get_mem(self):
        return self.mem


# if __name__ == '__main__':
#     t0 = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#     #  adb shell settings put global policy_control immersive.full=* 关闭手机的状态栏
#     #  adb shell settings put global policy_control null 开启手机状态栏
#     p = subprocess.Popen('adb shell monkey '
#                          '-p com.miui.calculator '
#                          '-v -v -v '
#                          '--pct-touch 30 '
#                          '--pct-syskeys 0 '
#                          '--pct-appswitch 0 '
#                          '--throttle 100 '
#                          '-s 25 '
#                          '1>./report/' + t0 + '_info.txt '
#                          '2>./report/' + t0 + '_error.txt '
#                          '5000',
#                          shell=True)
#     cpu = []
#     acpu = []
#     amem = []
#     mem = 0
#     flag = 1
#     while flag:
#         if p.poll() == 0:
#             flag = 0
#         thd = MyThread()
#         ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         t = ti.split(' ')[1]
#         thd.start()
#         thd.join()
#         # cpu.append(str(thd.get_res()))
#         cpu.append([t, thd.get_cpu()])
#         acpu.append([t, thd.get_acpu()])
#         amem.append([t, thd.get_amem()])
#         mem = thd.get_mem()
#         # time.sleep(1)
#     # print(cpu)
#     # print(acpu)
#     # print(amem)
#     # print(mem)
#     html = open('./LineGraph.html', mode='r', encoding='utf-8').read()
#     cpu_data = ''
#     for i in cpu:
#         cpu_data += '["'+i[0]+'",'+str(i[1])+']'
#         cpu_data += ','
#     acpu_data = ''
#     for j in acpu:
#         acpu_data += '["' + j[0] + '",' + str(j[1]) + ']'
#         acpu_data += ','
#     amem_data = ''
#     for k in amem:
#         amem_data += '["' + k[0] + '",' + str(k[1]) + ']'
#         amem_data += ','
#     html = html.replace('%cpu%', cpu_data)
#     html = html.replace('%acpu%', acpu_data)
#     html = html.replace('%amem%', amem_data)
#     html = html.replace('%mem%', str(mem))
#     t = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#     f = open('./report/' + t + '.html', mode='w', encoding='utf-8')
#     f.write(html)
#     f.close()


