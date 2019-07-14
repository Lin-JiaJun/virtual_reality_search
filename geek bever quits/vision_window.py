import os
import easygui
import cv2
import combine
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
# f = input("请输入图片名称:")
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("---new folder...---")
        print("---OK--")
    else:
        print("----This is the folder!")
def main():       
    file = 'C://the hack/web'
    mkdir(file)
    print("文件储存在G://the hack/web")
    photos = ['juice.jpg']#,'phone.jpg','food.jpg','seat.jpg']
    s = input("This is image recognition")
    for l in range(len(photos)):
        if s == '':
            # f = photos[l]
            cap = cv2.VideoCapture(0)
            # get a frame
            
            # show a frame
            while(1):
             ret, frame = cap.read()
             cv2.imshow("C://the hack/web/1.jpg", frame)
             if cv2.waitKey(1) & 0xFF == ord('q'):
              cv2.imwrite("C://the hack/web/1.jpg", frame)
              break
            cap.release() #释放摄像头
            time.sleep(3) 
            cv2.destroyAllWindows()
            f= "C://the hack/web/1.jpg"
            time.sleep(3)
            img=cv2.imread(f,1)
            #waitKey(0);
            title = easygui.msgbox(msg = "该窗口可进行图片识别并返回相应信息",
                                   title = "图像识别与查询相关信息",ok_button = "开始查询")
            time.sleep(3)
            msg = easygui.msgbox(msg="该识别信息将保存于G://the hack/web")
            time.sleep(3)
            try:
                
                name_f,description_f = combine.get_file(f)
            except Exception as e:
                print("哎呦！不好意思，没有搜到该物品信息哦，再拍一次试试")
                main()
            cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2和PIL中颜色的hex码的储存顺序不同
            pilimg = Image.fromarray(cv2img) # PIL图片上打印汉字
            draw = ImageDraw.Draw(pilimg) # 图片上打印
            font = ImageFont.truetype("simhei.ttf",10, encoding="utf-8") # 参数1：字体文件路径，参数2：字体大小
            x = 20
            y = 20
            draw.text((x, y),"物品名称:", (255, 0, 0), font=font)
            h = len(name_f)
            draw.text((x + h * 10 + 30, y), name_f, (255, 0, 0), font=font)
            i = 0
            count = 0
            n = len(description_f)
            while n >= 20:
                count += 1
                draw.text((x,y + 10 * count + 10),description_f[i:i + 20],(255,0,0),font = font)
                i = i + 20
                n -= 20
            draw.text((x,y + 10 * (count + 1) + 10),description_f[i:],(255,0,0),font = font)
    
    
            text1,text2 = combine.look_up(name_f)
            draw.text((x,y + 10 * (count + 2) + 10),"扩展资料查询网址:",(255,0,0),font = font)
            count0 = count + 3
            for i in range(len(text1)):
                draw.text((x, y + (count0 + i) * 10 + 10),text1[i] + ":", (255, 0, 0), font = font)
                # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体 # PIL图片转cv2 图片
                draw.text((x + len(text1[i]) * 10 + 30, y + (count0 + i) * 10 + 10), text2[i], (255, 0, 0), font=font)
            cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
            cv2.namedWindow("information",0)
            cv2.resizeWindow("information",1200,800)
            cv2.imshow('information',cv2charimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
    
main()