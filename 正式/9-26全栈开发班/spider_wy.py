import requests
from jsonpath import jsonpath   # dict  // list
import json


def get_data(url):
    headers = {
        'Referer': 'https://news.163.com/',
        'Cookie': '__bid_n=183acbbd9b928151884207; FPTOKEN=30$b18uWiI5KM1XD/f0vaRRkDvzF/29ms7olgZZVWvOLH6eLE'
                  'E/kRBH8j5a/z4f0eMRL9om9jkAsbBgYHinMoJ89kOed+hiuiRcJ2TOpq9pjCESTCHXV/mXzdvmu9b/koNRjB1mpJcsXccoIRZPpFw'
                  'H0hKL2VVwduKvTNbXttPH1Ji06hw7yhbTJHhl2+DNA490akM4In3KkhoYL9oqlsR1OLJgnmsvYA9CYe/fHxr+TuCF3DxiY3F/KRcNwkm'
                  '+EWODoiSB4yg+31qVrJXex5Odr7OmKZdB/J/v86DmLOCf7kuOJMFB3YNRFZlr94WkSKCfLdmp/g/Vy0zX30XViYtTsM9mtrb0cWvJIQ5vN9PBD0C2BffTOBDdY70Lrla643Fd|gGoRRUPVIgGqqBnPeX6L+jTSFxxGC4kOrONpEYzN2jg=|10|ddff8823f6d29564be445269e851ccd7; s_n_f_l_n3=fb5a9d2c354ac0781665059792230; _antanalysis_s_id=1665059792938; BAIDU_SSP_lcr=https://www.baidu.com/link?url=pfPcoXAmHrMdBZT3dHBK3dLx4HpGzFGhlpRloTb5CcS&wd=&eqid=e0750f4f0001be1100000006633ecbcd; NTES_PC_IP=%E9%95%BF%E6%B2%99%7C%E6%B9%96%E5%8D%97; ne_analysis_trace_id=1665061376305; vinfo_n_f_l_n3=fb5a9d2c354ac078.1.1.1665050334678.1665050376911.1665061378983',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    html_data = response.text
    return html_data

def parse_data(html_data):
    text_data_2 = html_data.split('data_callback(')[1]
    # print("uuuu",text_data_2)
    text_data_3 = text_data_2.split(')')[0]
    # print(text_data_3)  # str
    data_josn = json.loads(text_data_3)   # 将python数据类型转为JSON数据类型(指JavaScript中的数组和对象) （str--->dict）
    # print(data_josn)
    print(type(data_josn))
    title = jsonpath(data_josn,'$..title')
    # print(title)
    for i in title:
        print(i)
        print('=====')


if __name__ == '__main__':
    url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

    html_data = get_data(url)
    # print(html_data)
    parse_data(html_data)
    for i in range(2,6):
        print('正在下载第{}页'.format(i))
        page_url = 'https://news.163.com/special/cm_yaowen20200213_0{}/?callback=data_callback'.format(i)
        html_data = get_data(page_url)
        # print(html_data)
        parse_data(html_data)
