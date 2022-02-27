import cv2 

def readImg(path):
    img=cv2.imread(path)
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    return val

print(readImg('media/QR/xufstcbywgvrbacqfdvg.png'))