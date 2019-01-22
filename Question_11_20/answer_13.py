import cv2
import numpy as np
# MAX-MIN滤波器是一个滤波器，它输出滤波器中像素的最大值和最小值之间的差值，
# 并且是用于边缘检测的滤波器之一。 边缘检测用于检测图像中的线，并且用于提
# 取这种图像中的信息的操作被称为特征提取。 在边缘检测中，在大多数情况下，
# 对灰度图像执行滤波。
# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray scale
gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
gray = gray.astype(np.uint8)

# Max-Min Filter
K_size = 3

## Zero padding
pad = K_size // 2
out = np.zeros((H + pad*2, W + pad*2), dtype=np.float)
out[pad:pad+H, pad:pad+W] = gray.copy().astype(np.float)
tmp = out.copy()

for y in range(H):
    for x in range(W):
        out[pad+y, pad+x] = np.max(tmp[y:y+K_size, x:x+K_size]) - np.min(tmp[y:y+K_size, x:x+K_size])

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
