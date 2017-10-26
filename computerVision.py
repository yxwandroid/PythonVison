from  PIL import Image
import os

# 9灰度变换
# im = array(Image.open('wilson.jpg').convert('L'))
# im2 = 255 - im
# # 对图像进行反相处理
# im3 = (100.0 / 255) * im + 100  # 将图像像素值变换到 100...200 区间
# im4 = 255.0 * (im / 255.0) ** 2  # 对图像像素值求平方后得到的图像
# print (int(im.min()), int(im.max()))
#
# pil_im = Image.fromarray(uint8(im4))
# pil_im.show()

# 8    获取图片数组信息
# im = array(Image.open('wilson.jpg'))
# print(im.shape,im.dtype)
# im = array(Image.open('wilson.jpg').convert('L'), 'f')
#
# print(im.shape,im.dtype)
#


# 7 接受控制台输入数据
# filelist = "/Users/yangxuewu/Downloads/wilson.jpg"
# im = array(Image.open(filelist))
# imshow(im)
# print
# 'Please click 3 points'
# x = ginput(3)
# print
# 'you clicked:', x
# print(x)
# show()


# 6  轮廓图和直方图
# from PIL import Image
# from pylab import *  # 读取图像到数组中
#
# filelist = "/Users/yangxuewu/Downloads/wilson.jpg"
# im = array(Image.open(filelist).convert('L'))
# # 新建一个图像
# figure()
# # 不使用颜色信息
# gray()
# # 在原点的左上角显示轮廓图像
# contour(im, origin='image')
# axis('equal')
# axis('off')
#
# figure()
# hist(im.flatten(), 128)
# show()

#5  绘制点和线
# from PIL import Image
# from pylab import *  # 读取图像到数组中
#
# filelist = "/Users/yangxuewu/Downloads/wilson.jpg"
# im = array(Image.open(filelist))
# # 绘制图像
# imshow(im)
# # 一些点
# x = [100, 100, 400, 400,500]
# y = [200, 500, 200, 500,300]
# # 使用红色星状标记绘制点
# plot(x, y, 'r*')
# # 绘制连接前两个点的线
# plot(x[1:5], y[1:5])  # 添加标题，显示绘制的图像
# title('Plotting: "empire.jpg"')
# show()





# 4 图像基本操作
filelist = "/Users/yangxuewu/Downloads/wilson.jpg"
filelistyxw = "/Users/yangxuewu/Downloads/yxw.jpg"
newImage = Image.open(filelist)
box = (100, 100, 400, 400)
region = newImage.crop(box)
region.show()

newImage.thumbnail((128, 128))
newImage.save(filelistyxw)
newImage.show()

out = newImage.resize((228, 228))
out.show()

out = out.rotate(45)
out.show();

# 3 获取目录的jpg图片
def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


# 2 图片格式转换
infile = "/Users/yangxuewu/Downloads/wilson.jpg"
outfile = "/Users/yangxuewu/Downloads/wilson.jpeg"
Image.open(infile).save(outfile)
print("---------2--------")

# 1. 灰度处理
path = "/Users/yangxuewu/Downloads/wilson.jpg"
pilImage = Image.open(path).convert('L')
print("---------1--------")
pilImage.show();
