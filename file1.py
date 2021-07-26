import matplotlib.pyplot as plt
import numpy as np
import cv2


image = cv2.imread("./picture_flo.jpg")

img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.rectangle(imgGrey, (1000, 5000), (2000, 4000), (240, 240, 240), 20)
plt.imshow(imgGrey, "gray")
plt.show()
