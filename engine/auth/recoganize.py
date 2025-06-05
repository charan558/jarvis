import time
import cv2


def AuthenticateFace():
    flag = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('engine\\auth\\trainer\\trainer.yml')
    cascadePath = "engine\\auth\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    user_ids = [1,2]  # Your user ID
    names = ['', 'Charan','kamal hasan']
    

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            break
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            pred_id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

            if (accuracy < 60) and (pred_id in user_ids):  # Only accept your face
                name = names[pred_id]
                flag = 1
            else:
                name = "unknown"
                flag = 0

            cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, "  {0}%".format(round(100 - accuracy)), (x + 5, y + h - 5),
                        font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)
        #cv2.moveWindow('image', 100, 100)
       # cv2.setWindowProperty('image', cv2.WND_PROP_TOPMOST, 1)
        k = cv2.waitKey(10) & 0xff
        if k == 27 or flag == 1:
            break

    cam.release()
    cv2.destroyAllWindows()
    return flag