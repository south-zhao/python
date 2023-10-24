"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/9/18 13:00
    @Author : south(南风)
    @File : test.py
    Describe:
    -*- coding: utf-8 -*-
"""
from moviepy.editor import AudioFileClip
import subprocess
from vosk import Model, KaldiRecognizer, SetLogLevel


def get():
    # name = input("请输入当前目录下视频的名字:")
    # my_audio = AudioFileClip(name)
    # my_audio.write_audiofile(name.split(".")[0] + ".wav")
    print("开始加载语音识别模型")
    SAMPLE_RATE = 16000
    SetLogLevel(-1)
    # 解压的模型文件，英文，中文用对应model
    # getCn = "vosk-model-en-us-0.22"
    getCn = "vosk-model-cn-0.22"
    model = Model(getCn)
    print("模型加载完毕,开始识别...")
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    # 修改需要识别的语音文件路径
    # wavPath = name.split(".")[0] + ".wav"
    wavPath = "1.wav"
    rec.SetWords(True)
    result = []
    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                           wavPath,
                           "-ar", str(SAMPLE_RATE), "-ac", "1", "-f", "s16le", "-"],
                          stdout=subprocess.PIPE).stdout as stream:
        word = rec.SrtResult(stream)
        result.append(word)
    print("开始生成srt文件")
    # 生成srt文件
    # output = open(name.split(".")[0] + '.srt', 'w')
    output = open('1.srt', 'w')
    output.write("\n".join(result))
    output.close()
    print("srt输出完成")


if __name__ == '__main__':
    get()
