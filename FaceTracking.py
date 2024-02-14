
import cv2 as cv
import cv2
import time


#Getting camera on the first capture port and doing sleep to give camera time to warm up
cap = cv2.VideoCapture(0)
time.sleep(5)

#this will change from computer to computer
CascadePath = 'C:\\Users\\rkuhn\Desktop\\CodingProjects\\ImageShit_OpenVc\\haarcascade_frontalface_default.xml'

#loading the file 
Cascade = cv2.CascadeClassifier(CascadePath)

#checking if it successfully got the file.
if Cascade.empty():
    raise IOError("Unable to load Cascade File")
else:
    print("Model Loaded")

while True:
    
    #Pretty much just a boolean saying that if you dont have the frame then will end the while loop
    ret, frame = cap.read()
    if ret == False:
        print("Failed to grab frame")
        break
    
    #Takes the capture frame and converts it to grayscale. If you want to access the Normal frame display frame if not then do GrayScaleFrame
    GrayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = Cascade.detectMultiScale(GrayScaleFrame, scaleFactor=1.1, minNeighbors=5)

    #Shows the frame and the name of the window is in the quote marks
    cv2.imshow('Big ol Turd', GrayScaleFrame)

    #if q is pressed then end function. 0xFF is an encrypter that will make the ASCII keys represent the same ammount of bits no matter what opperating system. 
    #ord comes with python and turns the character (for this case 'q' and turns it into a ASCII value to look out for)
    #if the ASCII value of q (Firgured out by 0xFF) is equal to the ord value then it returns true)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("key pressed")
        cap.release()
        cv2.destroyAllWindows()
        break
