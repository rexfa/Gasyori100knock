import cv2
import numpy as np
# python不熟，测试用
# Read image
img = cv2.imread("imori.jpg").astype(np.float)
#高度，宽度，深度（the pixels value is made up of three primary colors像素值由三原色组成）
H, W, C = img.shape

a= [1,23,4]
b = [123,4,2]
c = [232,4,43]
d= np.array([a,b,c])
print (d)
print (d[...,0])
print (d[...,1])
print (d[...,2])
print (d[...,0]+d[...,1]+d[...,2])
v = range(0, 2, 1)
print (v)
print ("***************")
for num, i in enumerate(range(0, 2, 1)):
    print(num,i)
