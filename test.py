
# 'com.miui.calculator'

import os, subprocess

# if not os.system('adb shell monkey '
#                  '-p com.miui.calculator '
#                  '-v -v -v '
#                  '--throttle 100 '
#                  '-s 26 '
#                  '1>D:\\monkeyinfo.txt 2>D:\\monkeyerror.txt '
#                  '2000'):
#     print(1)
# p = subprocess.Popen('adb shell monkey -p com.miui.calculator -v -v -v --throttle 100 -s 26 100', shell=True)
# flag = 1
# while flag:
#     # print(1)
#     if p.poll() == 0:
#         flag = 0

# p = os.popen('adb shell top -m 1 -n 1 -t | grep System')
# a = p.read()
# print(a)
# b = a.split(',')
# user = b[0].strip().split(' ')[1].replace('%', '')
# system = b[1].strip().split(' ')[1].replace('%', '')
# print(float(user)+float(system))

p = os.popen('adb shell dumpsys meminfo|grep  -e calculator -e "Total RAM"')
a = p.readline().strip().split()
# print(a[0].replace(',', '').replace('K:', ''))
amem = a[0].replace(',', '').replace('K:', '')
p.readline()
t = p.readline().strip().split()[2].replace(',', '').replace('K', '')
print(t)
# print(a.split(' ')[5].replace('K:', '').replace(',', ''))

# p1 = os.popen('adb shell dumpsys cpuinfo |grep  calculator')
# a1 = p1.read().strip()
# print(a1)
# b1 = a1.split(' ')[0]
# print(b1.strip().replace('%', ''))

# p2 = os.popen('adb shell dumpsys meminfo|grep  calculator|head -1')
# a2 = p2.read().strip()
# b2 = a2.split(' ')[0]
# print(b2)
# print(b2.strip().replace('K:', '').replace(',', ''))




