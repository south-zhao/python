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

my_audio = AudioFileClip("9月20日.mp4")
my_audio.write_audiofile("9月20日.wav")


def getSrt():
    print("提取srt中...")
    print("开始加载识别模型")
    import subprocess
    from vosk import Model, KaldiRecognizer, SetLogLevel
    SAMPLE_RATE = 16000
    SetLogLevel(-1)
    # 解压的模型文件，英文，中文用对应model
    getCn = "vosk-model-en-us-0.22"
    model = Model(getCn)
    print("模型加载完毕,开始识别...")
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    # 修改需要识别的语音文件路径
    wavPath = "9月20日.wav"
    rec.SetWords(True)
    result = []
    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                           wavPath,
                           "-ar", str(SAMPLE_RATE), "-ac", "1", "-f", "s16le", "-"],
                          stdout=subprocess.PIPE).stdout as stream:
        word = rec.SrtResult(stream)
        result.append(word)
        print(word)
    print(result)
    # 生成srt文件
    output = open('9月20日.srt', 'w')
    output.write("\n".join(result))
    output.close()
    print("srt输出完成")


getSrt()
