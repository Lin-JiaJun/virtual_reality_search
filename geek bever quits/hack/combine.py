
import re
from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup as sp
from aip import AipImageClassify
 
""" 你的 APPID AK SK """
APP_ID = 'e7a84200634b4a8abd54f94fc7099dde'
API_KEY = '1dac20288ed94f00b62ebf5aa1c65fc0'
SECRET_KEY = '43f51333beb042b69fdd83ea2e677e83 '

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
    
def get_file(filePath):
    image = get_file_content(filePath)
    """ 调用通用物体识别 """
    client.advancedGeneral(image)

    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5

    """ 带参数调用通用物体识别 """
    temp = client.advancedGeneral(image,options)['result']
    # print(temp[0]['keyword'])
    # print(temp[0]['baike_info']['description'])
    named = temp[0]['keyword']
    return named,temp[0]['baike_info']['description']
"""
    n = len(temp)
    print(temp[0]['root'])
    for i in range(5):
        
        print("可能性" + str(i + 1) + ":" + temp[i]['keyword'])
        print("描述:" + temp[i]['baike_info']['description'])
 """
# print(temp)
# print(temp[0])
# print(temp[0]['keyword'])
# print(temp[0]['root'])
# print(temp[0]['baike_info'])
# print(temp[0]['baike_info']['description'])
# print(temp[1]['keyword'])
# print(temp[1]['baike_info']['description'])

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
bracket = re.compile(r'\[\d*]')


def look_up(entry):
    url = "https://baike.baidu.com/item/" + quote(entry)

    req = request.Request(url, headers=header)

    html = request.urlopen(req).read()
    soup = sp(html, "html.parser")
    le2=(soup.select('.para-title.'+'level-2 '))

    le2=(soup.findAll('h2',{'class':"title-text"}))
    #print(le2)
    x=1
    msg = []
    msg1 = []
    for l in le2:
        msg.append(l.text.replace(\
         '<bound method Tag.get_text of <h2 class="title-text"><span class="title-prefix">','').replace('</span>','').replace('</h2>>',''))
        msg1.append(url+"#"+str(x))
        x=x+1
    
    le3=(soup.select(".para-title\0level-3 "))

    content=soup.findAll('div',{'class':'para'})
    for i in content:
        i=i.get_text()
        i=i.replace('\n','')
        i=i.replace('\r','')
        i=re.sub(bracket,'',i)
    #    print(i)
    
    # for k in range(len(msg) - 1):
    #     return msg[k]
    # for f in range(len(msg1) - 1):
    #     return msg1[f]
    return msg,msg1
