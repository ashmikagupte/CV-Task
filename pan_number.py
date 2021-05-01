import cv2
import pytesseract

img = cv2.imread("Resources\img3.jpg")

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.resize(img, (600, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)
canny = cv2.Canny(gray, 30, 200)

text = pytesseract.image_to_string(gray, config="--psm 11")
li = list(text.split("\n"))

for i in li:
    if len(i)==10:
        if(i[2]=='/' and i[5]=='/'):
            dob=i
        str1=i[:5]+i[9]
        str2=i[5:9]
        if (str1.isalpha() and str2.isnumeric()):
            pan=i
print("PAN number : ",pan)
print("DOB        : ",dob)
cv2.imshow("Card Image", img)
cv2.waitKey(0)
