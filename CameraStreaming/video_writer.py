import numpy as np
import cv2
import pickle
import socket

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # Пример отображения текста на видео
        cv2.putText(frame, "Hello world!", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

        # Отображение видео (необходимо убрать при запуске по ssh):
        #cv2.imshow('frame', frame)
        out.write(frame)
        s = socket.socket()
        s.connect(('',1085))#s.connect(('172.24.1.141', 1085))
        s.send(pickle.dumps(frame))
        s.close()


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()

cv2.destroyAllWindows()


