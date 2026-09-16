import cv2
import matplotlib.pyplot as plt
image = cv2.imread("python coding /PYgame/how to make documents/image horse.jpg")
plt.title("RGB Image")
plt.show()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(gray_image)
plt.title("RGB_Image")
plt.show
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, camp='gray')
plt.title("Grayscale image")
plt.show
cropped_image=image[100:300, 200:400]
cropped_rgb=cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB )
plt.imshow(cropped_rgb)
plt.title("cropped_region")
plt.show
