# -*- coding: utf-8 -*-
from utils.play_aidio import play
from utils.record_audio import get_audio
import pyaudio
import threading
import time,os
import settings.DIR_PATH as path


def wake_rate():
    p = pyaudio.PyAudio()
    test_num = 0
    pass_num = 0
    while True:
        test_num +=1
        thread = threading.Thread(target=get_audio,)
        thread.start()
        time.sleep(2)
        play('man_wake_up')
        time.sleep(20)
        with open(path.result_path,"r") as f:
            data = f.read()
            print(data)
            if data != "None":
                print("识别结果：",data)
                if "你好" in data:
                    del_path = path.file_path()
                    os.system("del /F /S /Q "+del_path)
                    pass_num+=1
        print(test_num,pass_num)


def single_wake_rate(i):
    print("第"+str(i)+"次测试")
    pyaudio.PyAudio()
    thread = threading.Thread(target=get_audio,)
    thread.start()
    time.sleep(2)
    play('man_wake_up')
    time.sleep(20)
    with open(path.result_path,"r") as f:
        data = f.read()
        print(data)
        if data != "None":
            print("识别结果：",data)
            if "你好" in data:
                del_path = path.file_path()
                os.system("del /F /S /Q "+del_path)


if __name__ =='__main__':
    wake_rate()