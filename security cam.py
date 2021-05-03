import cv2
import time

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

width=int(cap.get(3))
height=int(cap.get(4))

# Define the codec and create VideoWriter object.
# The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('_video.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))

faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#optional for slow learners
font = cv2.FONT_HERSHEY_SIMPLEX




# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")


oldtime=0
while(True):
  ret, frame = cap.read()

  if ret == True:
    

    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    #optional for slow learners
    timeNow=time.asctime(time.localtime(time.time()))
    cv2.putText(frame,timeNow, (10,450), font, .98, (0, 255, 0), 2, cv2.LINE_AA)

    

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #optional for slow learners
        if time.time()-oldtime>30:
          cv2.imwrite(str(time.time())+"_face.jpg", frame)
          oldtime=time.time()
    
    
    # Write the frame into the video
    out.write(frame)

    # Display the resulting frame    
    cv2.imshow("Video Footage", frame)

    # Press Q on keyboard to stop recording
    if cv2.waitKey(25) == ord('q'):
      break
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows() 
