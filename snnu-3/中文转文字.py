"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/9/20 17:16
    @Author : south(南风)
    @File : 中文转文字.py
    Describe:
    -*- coding: utf-8 -*-
"""
import re


def getSrt1():
    print("开始加载识别模型")
    import subprocess
    from vosk import Model, KaldiRecognizer, SetLogLevel
    SAMPLE_RATE = 16000
    SetLogLevel(-1)
    # 解压的模型文件，英文，中文用对应model
    getCn = "vosk-model-cn-0.22"
    model = Model(getCn)
    print("模型加载完毕,开始识别...")
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    # 修改需要识别的语音文件路径
    wavPath = "何明家-四声歌（慢速）.mp3"
    rec.SetWords(True)
    result = []
    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                           wavPath,
                           "-ar", str(SAMPLE_RATE), "-ac", "1", "-f", "s16le", "-"],
                          stdout=subprocess.PIPE).stdout as stream:
        word = rec.SrtResult(stream)
        result.append(word)
    output = open('9月20日.txt', 'w', encoding="utf-8")
    output.write("\n".join(result))
    output.close()
    with open("9月20日.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        new_data = []
        for i in data:
            new_data.append(i.replace(" ", ""))
    txt1 = ""
    for i in new_data:
        match_zi = re.findall(r'[\u4e00-\u9fa5]+', i)
        if len(match_zi) != 0:
            match_zi[0] += "\n"
            txt1 += match_zi[0]

    with open("9月20日.txt", "w", encoding="utf-8") as f:
        f.write(txt1)
    print("中文识别转文字完成")


getSrt1()
