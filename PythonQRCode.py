import qrcode
import matplotlib.pyplot as plt # plt 用于显示图片


# 生成二维码相关代码
qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
qr.add_data("wilson")
qr.make(fit=True)
img = qr.make_image()
img.save("11.png")


plt.imshow(img) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()