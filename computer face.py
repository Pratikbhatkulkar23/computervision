import cv2

img = cv2.imread ("C:\\Users\\Admin\\PycharmProjects\\computer vision\\face.jpg")
#print(img)
#print(type(img))
#print(img.shape)

cv2.imshow("Legend",img) ### this code for opening image
cv2.waitKey(2000)

cv2.destroyAllWindows()