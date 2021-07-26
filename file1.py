import matplotlib.pyplot as plt
import numpy as np
import cv2


image = cv2.imread("./picture_flo.jpg")

img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(imgGrey, "gray")
plt.show()
