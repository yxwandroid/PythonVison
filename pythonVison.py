from PIL import Image
from numpy import *
from imtool import ImageUtils

im = array(Image.open('wilson.jpg').convert('L'))
im2, cdf = ImageUtils.compute_average(Image.open('wilson.jpg'))

print(cdf)
print('-----------------------')
print(im2)
