## 图像

- **颜色**：我们通常把颜色表示为一个RGB值，如(255, 255, 255)表示white，(0, 0, 0)表示black。

- **像素**：由图像的小方格组成的，这些小方块都有一个明确的位置和被分配的色彩数值，小方格颜色和位置就决定

  ​			该图像所呈现出来的样子，它们是不可分割的单位或者是元素，称之为像素。

##### 用`Pillow` 来操作图像

```python
# demo_1.py
from PIL import Image,ImageGrab，ImageFilter

new = Image.new('RGB', (800, 500), (255, 255, 255))		# 创建图片:mode, size, color
screenGrab = ImageGrab.grab().save('screengrab.jpg', 'jpeg')	# 抓取屏幕
image = Image.open('./meizi.jpg')	# 加载图像
image.show()    # 显示图片
print(image.getbands())     # 获取图片的管道数和名称 这里打印了一个元组('R', 'G', 'B')
print(image.format)  # 获取图片格式,此处为JPEG
print(image.mode)   # 获取图片模式,典型的取值为“1”，“L”，“RGB”或“CMYK”。
print(image.size)   # 获取图片尺寸(width, height)
print(image.info)   # 获取图片信息

```

```python
# 裁剪(crop)图像
rect = 250, 50, 550, 300      # 左上角为(0, 0) 参数：left, upper, right, lower的坐标位置
image.crop(rect).show()

# 生成缩略图(thumbnail)，图像不会被拉伸，且只能缩小
size = 500, 400		# width, height
image.thumbnail(size)

# 缩放(图片可能会被拉伸，可放大可缩小)
w, h = image.size
image = image.resize(w//2, h//2)

# 粘贴图片(paste)
image.past(image, (100, 100))	# 参数：图像，坐标

# 旋转(rotate)
image.rotate(180)	
# 翻转 即左右翻转
image.transpose(Image.FLIP_LEFT_RIGHT)	
#模糊图片并保存
image = image.filter(ImageFilter.BLUR).save('meizi_blur.jpg', 'jpeg')
```

