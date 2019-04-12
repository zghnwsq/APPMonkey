
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
# p = subprocess.Popen('adb shell monkey '
#                      '-p com.miui.calculator '
#                      '-v -v -v '
#                      '--throttle 100 '
#                      '-s 26 '
#                      # '1>D:\\monkeyinfo.txt 2>D:\\monkeyerror.txt '
#                      '100')
# flag = 1
# while flag:
#     # print(1)
#     if p.poll() == 0:
#         flag = 0

p = os.popen('adb shell top -m 1 -n 1 -t | grep System')
a = p.read()
print(a)
b = a.split(',')
user = b[0].strip().split(' ')[1].replace('%', '')
system = b[1].strip().split(' ')[1].replace('%', '')
print(user)
print(system)




