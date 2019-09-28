# -*- coding: utf-8 -*-
'''
Created on 2018年9月27日

@author: uidq1501
'''
import pyaudio
import wave
import time
import settings.DIR_PATH as path
import os


# r = sr.Recognizer()
# mic = sr.Microphone(device_index=1)   #input1

def get_audio():
    input_filename = time.strftime("%Y-%m-%d-%H-%M-%S") + ".wav"  # 麦克风采集的语音输入
    input_filepath = path.record_file  # 输入文件的path
    in_path = input_filepath + input_filename
    CHUNK = 256  # 256kb
    FORMAT = pyaudio.paInt16  # 录音格式
    CHANNELS = 1  # 声道数
    RATE = 11025  # 采样率
    RECORD_SECONDS = 8  # 录音时长
    WAVE_OUTPUT_FILENAME = in_path
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=CHUNK)

    print(str("*" * 6 + "开始录音：录制8秒内输入的语音"))
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print(str("*" * 6 + "录音结束\n"))

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    with open(path.currtxt_path, 'w') as f:
        f.write(in_path)
    os.system("python "+path.web_path)

    # print("录音已保存在"+in_path)
    # result = shibie(in_path)
    # print(result)
    # with open(r'../record_files/result.txt','w') as f:
    #     if result:
    #         f.write(result)
    #     else:
    #         f.write("None")



    # XF_text(in_path, 16000)

if __name__ == '__main__':
    get_audio()

    # print(time.strftime("%Y-%M-%D %X"))
