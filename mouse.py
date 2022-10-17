# This project is made to use your computer's camera to control the movement
# of the users eye to act like a computer mouse

#Import the libraries needed for the project
import cv2
import mediapipe
import pyautogui

#Camera to capture the video using cv2
camera = cv2.VideoCapture(0)

#Detect the face from the camera using mediapipe
face = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)

screen_width, screen_height = pyautogui.size()

# The frames for the video captured
while 1:
    _, frame = camera.read() #Read whats coming from the camera
    frame = cv2.flip(frame, 1) #flip the frame
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Reads the color from the frame to RGB
    out = face.process(rgb) # Output the process of the rgb that is made from the variable above
    # The two lines of code under this comment
    #shows the green dots that are displayed in the camera, and prints them
    marks =  out.multi_face_landmarks
    frame_height, frame_weight, _ = frame.shape
    if marks:
        all_marks = marks[0].landmark #get the first face [0] from the marks
        for id, landmark in enumerate(all_marks[474:487]): #Gets 4 different lenmarks
            x = int(landmark.x * frame_weight)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x,y), 3, (0,255,0)) #Where, center, radius of circle, color (RGB)
            if id == 1:
                # Code inside this block allows the user to move
                # their mouse within any radius in the screen
                screen_x = int(landmark.x * screen_width)
                screen_y = int(landmark.y * screen_height)
                pyautogui.moveTo(screen_x, screen_y)
        hand = [all_marks[145], all_marks[159]] # get the index of top and bottom eye lid
        for landmark in hand:
            x = int(landmark.x * frame_weight)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

    cv2.imshow("The Mouse Spy", frame) #Show what the camera is seeing
    cv2.waitKey(1) #Wait time for 1 second


