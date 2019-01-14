import cv2
import numpy as np
# 自适应阈值二值化,使用大律（OTSU）算法得到的全局自适应阈值
# Read image
img = cv2.imread("imori.jpg").astype(np.float)
#高度，宽度，深度（the pixels value is made up of three primary colors像素值由三原色组成）
H, W, C = img.shape

# Grayscale
out = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
out = out.astype(np.uint8)

# Determine threshold of Otsu's binarization
max_sigma = 0
max_t = 0

for _t in range(1, 255):
    v0 = out[np.where(out < _t)[0]]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= _t)[0]]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    # 获取最大方差
    sigma = w0 * w1 * ((m0 - m1) ** 2)
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

# Binarization
# 二值化 显示阈值
print("threshold >>", max_t)
th = max_t
out[out < th] = 0
out[out >= th] = 255

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
