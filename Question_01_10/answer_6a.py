import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Decrease color 减色处理
out = img.copy()
print(out)
print("***********************")
print(len(out[0][0]))
#print(out[2][127])
print("***********************")
for i in range(4):
    ind = np.where(((64*i-1) <= out) & (out < (64*(i+1)-1))) #选出满足色域的点?
    print(i,ind,out[ind])
    out[ind] = 32 * (2*i+1) # 对选出点重新赋值
    print(type(ind),len(ind[0]),"************************")
    print(ind[0])



#img_gray = cv2.imread('imori.jpg', cv2.IMREAD_GRAYSCALE)
#H,W,C = img_gray.shape
#print(H,W,C)
#print(img.shape)