import matplotlib.pyplot as plt
import numpy as np
import cv2


img = cv2.cvtColor(cv2.imread("./picture_flo.jpg"), cv2.COLOR_BGR2RGB)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.rectangle(imgGrey, (1000, 5000), (2000, 4000), (240, 240, 240), 20)
#plt.imshow(imgGrey, "gray")
# plt.show()

classifier = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
faces = classifier.detectMultiScale(imgGrey, minNeighbors=10)


for face in faces:
    x, y, w, h = face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 10)
    print(faces)


plt.imshow(img)
plt.show()
