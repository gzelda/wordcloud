

import wordcloud
from PIL import Image
import numpy as np

font = r'./Alibaba-PuHuiTi-Medium.ttf'
f = open('a.txt')
a = f.readlines()
result = ""

for i in a:
    print(type(i),i)
    for j in range(len(i)):
        if (i[j] == "\n"):
            print("skip")
            result+=','
        else:
            result+=i[j]
print(result)


mask = np.array(Image.open("mask1.jpg"))
print(mask)
w = wordcloud.WordCloud(mask = mask,font_path=font,width=5000,height=5000,background_color='white')
w.generate(result)
w.to_file('output.png')
f.close()
# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
#w = wordcloud.WordCloud(width=1000,height=700,background_color='white')

# 调用词云对象的generate方法，将文本传入
#w.generate('DS abd.,adfva,211,dvafd,a ,sd, asd')

# 将生成的词云保存为output2-poem.png图片文件，保存到当前文件夹中
#w.to_file('output2-poem.png')
