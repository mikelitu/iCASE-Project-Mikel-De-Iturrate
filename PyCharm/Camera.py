import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import imageio


print("Imported OpenCV ", cv2.__version__)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


#Check whether user selected camera is opened successfully.
if cap.isOpened():
    # Capture frame-by-frame
    is_capturing, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.asarray(frame)
    pre_frame = frame
    pre_frame[pre_frame==0] = 1 #Avoid divisions by zero

num_frames = 20

for i in range(0, num_frames):
#while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    start = time.time()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.asarray(frame)
    flow = np.divide(frame, pre_frame)
    #flow = flow * 255 // np.max(flow) #Use to transform the relative difference into a uint8 format for saving purposes
    # Display the resulting frame
    end = time.time()
    print("The division between matrices and image saving took: %0.3f ms"  % ((end-start)*1000))
    plt.imshow(flow, cmap="hot", vmin=0.5, vmax=5.0)
    #plt.hist(flow, bins='auto')
    plt.pause(0.03)
    #pre_frame = frame


# When everything done, release the capture
cap.release()
plt.show()

plt.hist(flow)
plt.show()