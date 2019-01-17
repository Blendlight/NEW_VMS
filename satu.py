import cv2
import imutils
import sys
import pytesseract

cam = cv2.VideoCapture(2)

cam.set(3, 640 )
cam.set(4, 480 )
cam.set(10, 150 )
cam.set(11, 50 )
cam.set(12, 70 )
cam.set(13, 13 )
cam.set(14, 50 )
cam.set(15, -3   )
cam.set(17, 5000 )
cam.set(28, 100    )

# imPath = 'test.jpg'

a = 0
while True:
    a = a + 1
    check, frame = cam.read()
    frame = imutils.resize(frame, width=640, height=480)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite('test1.jpg', frame)
        break
        cam.release()
print (a)


imPath = 'test1.jpg'
config = ('-l eng --oem 1 --psm 3')

# Read image from disk
im = cv2.imread(imPath, cv2.IMREAD_COLOR)

# Run tesseract OCR on image
text = pytesseract.image_to_string(im, config=config)

# Print recognized text
print(text)

f = open("hali2.txt","w")

f.write(text)

f.close()

# with open('hali2.txt', 'r') as myfile:
#     data = myfile.read().replace('\n', '')
#
# print ("ini Print Data =>", data)


with open("hali2.txt", encoding="utf-8")as file:
    bukan = [l.strip() for l in file]

print (bukan)

i = 0
while i < len(bukan):
    if (bukan[i][:4] =='Nama'):
        nama = bukan[i]
        print (nama)
    i += 1




cv2.destroyAllWindows
