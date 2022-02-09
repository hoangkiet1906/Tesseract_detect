import  cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("2.PNG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
data = pytesseract.image_to_data(img)

for x,d in enumerate(data.splitlines()):
    if x!=0:
        d = d.split()
        if len(d) == 12:
            x,y,w,h = int(d[6]),int(d[7]),int(d[8]),int(d[9])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,d[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
cv2.imshow("haha",img)
cv2.waitKey()
cv2.destroyAllWindows()


