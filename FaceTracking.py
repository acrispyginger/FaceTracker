
import cv2
import time


#Getting camera on the first capture port and doing sleep to give camera time to warm up
cap = cv2.VideoCapture(0)
#If not working then uncomment this time.sleep camera may need time to start up.
#time.sleep(5)

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

    #ok this line of code has a ton of shit going on.
    #detectMultiScale pretty much means scale down the frame (we cant see this version) until it gets too small to recognize a face
    #Grayscaleframe means simply that the frame is grayscale and that some things need to change because of that 
    #scalefactor= 1.1 means that it is scaling down the image like the way that google slides scales down an image by compressing them.
    #   it is scaling down the frame by 90% (approximately) because 1/1.1 = about .9
    #   it will do this until it eather reaches a minimum size or in the model it becomes too small for the image to recognize it.
    #minNeighbors means that it will go through sections of the frame called windows and check if the model recognizes a face. and if
    #   there are 5 detected faces next to eachother then it will consider that a face. This removes redundencies and fixes false positives
    #Lastly consider adding a minimum scale because then it wont scale down any smaller than it needs to and this might make it faster
    face = Cascade.detectMultiScale(GrayScaleFrame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in face:
     cv2.rectangle(GrayScaleFrame, (x, y), (x+w, y+h), (255, 0, 0), 2)

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
