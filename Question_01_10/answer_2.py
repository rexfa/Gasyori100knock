import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray scale 灰度化
# 1)最大值法：使转化后的R，G，B得值等于转化前3个值中最大的一个，即：R=G=B=max（R，G，B）。这种方法转换的灰度图亮度很高。 
# 2)平均值法：是转化后R，G，B的值为转化前R,G,B的平均值。即：R=G=B=(R+G+B)/3。这种方法产生的灰度图像比较柔和。 
# 3)加权平均值法：按照一定权值，对R，G，B的值加权平均，即：这里写图片描述分别为R，G，B的权值，取不同的值形成不同的灰度图像。
#   由于人眼对绿色最为敏感，红色次之，对蓝色的敏感性最低，因此使将得到较易识别的灰度图像。一般时，得到的灰度图像效果最好。 
# 0.2126  + 0.7152 + 0.0722 = 1 ,正好在每个像素落到0-255 之间灰度
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
