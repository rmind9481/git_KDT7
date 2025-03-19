import cv2

img_file ='../image/cat.jpg'

img = cv2.imread(img_file, cv2.IMREAD_COLOR)


if img is not None:
	cv2.imshow('IMG',img)
	cv2.waitKey()
	cv2.destroyAllWindosw()
else:
	print('no Image file')



