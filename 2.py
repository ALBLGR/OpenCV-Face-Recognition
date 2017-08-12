import cv2
import sys
import os
import subprocess
import urllib
import urllib2
import json
import time

cascPath="./haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier("/home/chm/face_recognized_sys/haarcascades/haarcascade_frontalface_alt.xml")

video_capture = cv2.VideoCapture(0)

while True
    requrl = "http://alblgr.vicp.net/face.php"
    req = urllib2.Request(url = requrl,data =test_data_urlencode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    rospy.loginfo(res)
    JSON_1=json.loads(res)
    if JSON_1['requestFace'] = 1 :
        hasPerson = False
        while (not hasPerson):
             # Capture frame-by-frame
             ret, frame = video_capture.read()
             # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             faces = faceCascade.detectMultiScale(
                 frame,
                 scaleFactor=1.1,
                 minNeighbors=3,
                 minSize=(50, 50),
                 flags=cv2.cv.CV_HAAR_SCALE_IMAGE
             )

           #subprocess.Popen("/home/chm/techx_ws/src/techx_talker/scripts/talker.py",shell=True)

           # Draw a rectangle around the faces
           for (x, y, w, h) in faces: 
               cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
           # Display the resulting frame
           cv2.imshow('Video', frame)
           if cv2.waitKey(1) & 0xFF == ord('q'):
               break
        # When everything is done, release the capture

        video_capture.release()
        cv2.destroyAllWindows()
    time.sleep(1)
