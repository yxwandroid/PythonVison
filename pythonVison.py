from PIL import Image
from pylab import *
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"/Users/yangxuewu/CodingDemo/python/SimSun.ttc", size=14)
figure()

pil_im = Image.open('./wilson.jpg')
gray()
subplot(121) #绘制多图 
title(u'原图',fontproperties=font)
axis('on')  #显示坐标
imshow(pil_im)
pil_im = Image.open('./wilson.jpg').convert('L')
subplot(122)
title(u'灰度图',fontproperties=font)
axis('on')
imshow(pil_im)
show()