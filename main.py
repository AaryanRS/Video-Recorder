import cv2
from AudioRecorder import Audio
import threading

cap = cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("input.avi", fourcc, 20.0 , (640 ,480))
aud =Audio()

def AudioRec():
    return aud.record()

def VideoRec():
    while True :
        success, frame = cap.read()

        out.write(frame)

        cv2.imshow("Capture" , frame)

        if cv2.waitKey(10) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    t1 = threading.Thread(target=AudioRec)
    t2 = threading.Thread(target=VideoRec)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
