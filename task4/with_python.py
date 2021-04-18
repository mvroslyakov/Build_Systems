import cv2


img = cv2.imread('map.png', cv2.IMREAD_COLOR)
watman = cv2.imread('watman.jpg', cv2.IMREAD_COLOR)
h, w, c = watman.shape
for hi in range(h):
  for wi in range(w):
    b,g,r = watman[hi,wi]
    watman[hi,wi] = (img[2,b,2], img[1,g,1], img[0,r,0])
cv2.imwrite('new_watman.png', watman)

