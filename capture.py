# python3 -c 'import cv2; print(cv2.getBuildInformation())'| grep Video -A10
import cv2

print(cv2.getBuildInformation())
# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(-1)

while(True):
    ret, frame = capture.read()
    if not ret:
        print("Error: cannot read image from {}".format(capture))
        break
    # resize the window
    windowsize = (800, 600)
    frame = cv2.resize(frame, windowsize)

    cv2.imshow('camera_capture', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
