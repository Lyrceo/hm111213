import cv2

image_path = 'cat.jpg'
cat_face_cascade = cv2.CascadeClassifier('nn.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
cv2.imshow('Cat', image)
cv2.waitKey()
