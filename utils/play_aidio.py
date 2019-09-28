# -*- coding: utf-8 -*-
import pyaudio
import wave
import sounddevice as sd
import time
import settings.DIR_PATH as bpath

def play(name,type):
    chunk = 1024
    #
    path = type+name+'.wav'
    f = wave.open(path,'rb')
    p = pyaudio.PyAudio()

    # print(p.get_device_count())
    # print(p.get_default_output_device_info())
    # print(p.get_device_info_by_index(7))


    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    # output_device_index = 14,
                    output = True,
                    )
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()

if __name__ == "__main__":
    i=1
    while i<11:

        play('woman_wake_up')
        time.sleep(1.5)
        play('man_q'+str(i))
        i+=1
        time.sleep(10)
    # print(sd.query_devices())