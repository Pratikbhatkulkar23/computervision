import cv2

# creating a cascadeclassifier object

face_cascade = cv2.CascadeClassifier("C:\\Users\\Admin\\PycharmProjects\\computer vision\\image\\face.jpg")

#reading the image as it is

img = cv2.imread("C:\\Users\\Admin\\PycharmProjects\\computer vision\\face.jpg")

#reading the image as grey scale image
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#searching the co-ordintea of the image
face = face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=5)

print(type(face))
print(face)
for x,y,h in face :
    img = cv2.rectangle(img, (x,y),(x+w,Y+h),(0,255,0),3)


cv2.imshow("Grey",img)


cv2.waitKey(0)
cv2.destroyAllWindows()