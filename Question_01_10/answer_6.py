import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Decrease color 减色处理
out = img.copy() #完整拷贝

for i in range(4):
    ind = np.where(((64*i-1) <= out) & (out < (64*(i+1)-1))) #选出满足色域的点?
    out[ind] = 32 * (2*i+1) # 对选出点重新赋值

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
