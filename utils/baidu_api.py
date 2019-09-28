# -*- coding: utf-8 -*-
from aip import AipSpeech

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def shibie(file):
    # 识别本地文件
    """ 你的 APPID AK SK """
    APP_ID = '16919370'
    API_KEY = 'dF4sP7jIo9UmjCIEGebt4NhO'
    SECRET_KEY = 'lqsQLa8vWbROErNxfdmxHlqGnvuGuter'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.asr(get_file_content(file), 'wav', 16000, {
        'dev_pid': 1536,
    })
    if result["err_no"] == 0:
        # print(result)
        return result["result"][0]
    else:
        print(result["err_no"])

if __name__ == "__main__":
    result = shibie("2019-07-31-15-13-30.wav")
    print(result)