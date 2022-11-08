import cv2

def takesnap():
    v=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=v.read()
        print(ret)
        cv2.imwrite("testPic.jpg",frame)
        result=False
    v.release()
    cv2.destoryAllWindows()

takesnap()
