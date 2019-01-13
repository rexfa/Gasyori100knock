import cv2
#cv2默认为 BGR顺序
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2默认为bgr顺序
# Read image
img = cv2.imread("imori.jpg")
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB > BGR  R和B换位置
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

# Save result
cv2.imwrite("out.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
