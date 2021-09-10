import cv2
image=cv2.imread("IMG_20200925_202900_882.jpg")
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted_img=255-gray_img
blurred=cv2.GaussianBlur(inverted_img,(21,21),0)
inverted_blurred=255-blurred
pencil=cv2.divide(gray_img,inverted_blurred,scale=256.0)
cv2.imshow("Original Image".image)
cv2.imshow("Pencil Sketch",pencil)
cv2.waitkey(0)