import time
import cv2

def detect(img, detecter):
    rects = detecter.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    video_src = 0
    path = "E://vs//opencv//sources//data//lbpcascades//lbpcascade_frontalface_improved.xml"
    detecter = cv2.CascadeClassifier(path)

    cam = cv2.VideoCapture(video_src)

    index = 0
    time_sum = 0.0
    old_sum = 0.0
    while True:
        index += 1
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = time.time()
        rects = detect(gray, detecter)
        dt = time.time() - t
        time_sum += dt

        vis = img.copy()
        if len( rects ) > 0:
            draw_rects( vis, rects, (0, 255, 0) )#BGR
        else:
            print("no face found")

        if index%100 == 0:
            old_sum = time_sum
            time_sum = 0.0

        if old_sum > 0.0001:
            cv2.putText( vis, '100 pics, average time: {} s'.format( round( old_sum/100.0, 4 ) ),
                             (20, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2 )
        cv2.imshow( 'facedetect', vis )

        key_ret = cv2.waitKey( 1 )
        if (key_ret == 0):  # if delete key is pressed
            break
    cam.release()
    cv2.destroyAllWindows()

