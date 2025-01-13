import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (640, 480))
capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()

    if ret:
        out.write(frame)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        #cv2.imshow('frame', gray)
        #cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
out.release()
cv2.destroyAllWindows()