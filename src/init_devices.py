# -*- coding: utf-8 -*-
import subprocess

subprocess.call("adb connect 192.168.0.2:5555")
cmds = [
    "cd sdcard/txz",
    'touch log_enable_file',
    "exit",#执行退出，重要
]
obj = subprocess.Popen("adb shell", shell= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
info = obj.communicate(("\n".join(cmds) + "\n").encode('utf-8'))
for item in info:
    if item:
        print(item.decode('gbk'))

subprocess.call("adb reboot")
