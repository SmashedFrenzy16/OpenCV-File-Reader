import cv2
import matplotlib.pyplot as plt

image = cv2.imread("house.jpg")

processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(processed_image)

plt.waitforbuttonpress()

plt.close('all')