import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
cam.set(3, 640) # set video FrameWidth
cam.set(4, 480) # set video FrameHeight


detector = cv2.CascadeClassifier('engine\\auth\\haarcascade_frontalface_default.xml')
#Haar Cascade classifier is an effective object detection approach

face_id = input("Enter a Numeric user ID  here:  ")
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

print("Taking samples, look at camera ....... ")
count = 0 # Initializing sampling face count

# Initialize the main loop for capturing face samples
while True:

    # Read a frame from the webcam
    ret, img = cam.read()
    # Convert the frame to grayscale for face detection
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale frame
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        # Save the detected face region as an image file
        cv2.imwrite("engine\\auth\\samples\\face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h, x:x+w])

    # Display the frame with rectangles in a window
    cv2.imshow('image', img)
    # Move the window to position (100, 100) on the screen
    cv2.moveWindow('image', 100, 100)
    # Set the window to always stay on top
    cv2.setWindowProperty('image', cv2.WND_PROP_TOPMOST, 1)
    # Wait for 100ms for a key press
    k = cv2.waitKey(100) & 0xff
    if k == 27:  # If 'ESC' key is pressed, exit the loop
        break
    elif count >= 100:  # If 100 samples are collected, exit the loop
        break

print("Samples taken now closing the program....")
cam.release()
cv2.destroyAllWindows()