import cv2
import dropbox
import time
import random

start_time=time.time()
print(start_time)

def takePic():
    num = random.randint(0,100)
    v=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=v.read()
        img_name = "img"+str(num)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False

    return img_name
    print("snapshot taken")
    v.release()
    cv2.destoryAllWindows()

def upload(img_name):
    access_token = "sl.BLBYweiRm9wpXOjVd96L6dubwBxoEBCZa1S3tf32Ik0faxQ-x9hZ381fOKmSL7EcDRrKEBXcDar2UNGVaML2a63weqshENmcaUWuwSG8mqa314T58as399mS1kNV-Br74_uRjqsNnYYL"
    file=img_name
    file_from = file
    file_to = "/Python/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takePic()
            upload(name)

main()