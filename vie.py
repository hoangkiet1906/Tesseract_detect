import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("3.PNG")
cv2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

data = pytesseract.image_to_string(img, lang="vie")
print(data)
with open("dich.txt", "a", encoding="utf-8",) as f:
    f.writelines(data)
