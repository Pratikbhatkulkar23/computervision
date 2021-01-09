import cv2

img = cv2.imread ("C:\\Users\\Admin\\PycharmProjects\\computer vision\\face.jpg")

resize = cv2.resize(int(img.shape[1]*2),int(img.shape[0]*2))
cv2.imshow("Legend",resize)

cv2.waitKey(2000)
cv2.destroyAllWindows()