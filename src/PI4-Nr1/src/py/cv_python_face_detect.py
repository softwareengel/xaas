# 2020-09-04 - NOT WORKING 



# 1. Let’s create a file called face_detection.py and start by importing the necessary module:
import cv2
print ("cv2 Version:", cv2.__version__)


# 2. After this, we declare a method, detect(), which will perform face detection.
def detect():
    face_cascade =  cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    # print (eye_cascade)
    # camera = cv2.VideoCapture(0)

    cap = cv2.VideoCapture(0)
    '''3. The first thing we need to do inside the detect() method is to load the Haar cascade
    files so that OpenCV can operate face detection. As we copied the cascade files in the
    local cascades/ folder, we can use a relative path. Then, we open a VideoCapture
    object (the camera feed). The VideoCapture constructor takes a parameter, which
    indicates the camera to be used; zero indicates the first camera available.'''
    while (True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        '''4. Next up, we capture a frame. The read() method returns two values: a Boolean
        indicating the success of the frame read operation, and the frame itself. We capture
        the frame, and then we convert it to grayscale. This is a necessary operation, because
        face detection in OpenCV happens in the grayscale color space:'''
 #       cv2.imshow('frame', gray)
#         continue 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        '''5. Much like the single still image example, we call detectMultiScale on the grayscale
        version of the frame.'''
        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0,(40,40))
            ''' There are a few additional parameters in the eye detection. Why? The method
            signature for detectMultiScale takes a number of optional parameters: in the case
            of detecting a face, the default options were good enough to detect faces. However,
            eyes are a smaller feature of the face, and self-casting shadows in my beard or my
            nose and random shadows in the frame were triggering false positives.
            By limiting the search for eyes to a minimum size of 40x40 pixels, I was able to
            discard all false positives. Go ahead and test these parameters until you reach a point
            at which your application performs as you expected it to (for example, you can try
            and specify a maximum size for the feature too, or increase the scale factor and
            number of neighbors). '''
            '''6. Here we have a further step compared to the still image example: we create a region
            of interest corresponding to the face rectangle, and within this rectangle, we operate
            “eye detection”. This makes sense as you wouldn’t want to go looking for eyes
            outside a face (well, for human beings at least!).'''
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                ''' 7. Again, we loop through the resulting eye tuples and draw green rectangles around
                them. '''
        cv2.imshow("camera", frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()


'''8. Finally, we show the resulting frame in the window. All being well, if any face is
within the field of view of the camera, you will have a blue rectangle around their
face and a green rectangle around each eye, as shown in this screenshot:'''

if __name__ == "__main__":
    detect()