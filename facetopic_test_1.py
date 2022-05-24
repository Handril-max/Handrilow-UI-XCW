import cv2
import time
import os,shutil
import numpy as np
from PIL import Image
#from HandrilowOSLauncherCode  import cpupack as cpk
#shutil.rmtree('dataSet')
#os.mkdir('dataSet')
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
sampleNum = 0
#输入人脸图像数据类别
Id = time.strftime("%S")
print(Id)
print('开始采集')
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sampleNum = sampleNum + 1
        #命名规则为User.[ID].[SampleNumber].jpg
        #如果是2号人的第十张照片，我们可以将它命名为User.2.10.jpg
        cv2.imwrite("dataSet/User." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])  #
        cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif sampleNum > 20:
        break
cap.release()
cv2.destroyAllWindows()
print('采集完成！')

#初始化识别器和人脸检测器
'''
如果face.LBPHFaceRecognizer_create或createLBPHFaceRecognizer显示不存在
则需要下载opencv-contrib-python  pip install opencv-contrib-python
'''
# recognizer = cv2.createLBPHFaceRecognizer()
#detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
'''
遍历图片路径，导入图片和id，添加到list
'''
def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    for image_path in image_paths:
        #灰度图片
        image = Image.open(image_path).convert('L')
        #将图片转换成了Numpy数组
        image_np = np.array(image, 'uint8')
        #为了获取到id，我们将图片的路径分裂一下并获取相关信息
        if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
            continue
        image_id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(image_np)
        #将图片和id都添加在list中
        for (x, y, w, h) in faces:
            face_samples.append(image_np[y:y + h, x:x + w])
            ids.append(image_id)
    return face_samples, ids
#让LBPH识别器去训练
print('模型开始建立')
faces, Ids = get_images_and_labels('dataSet')
recognizer.train(faces, np.array(Ids))
recognizer.save('trainner' + Id + '.xml')
print('模型数据完成！')
