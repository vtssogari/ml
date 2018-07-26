# Spark MLLib Machine Learning

## Spark MLLib Classic ML Routine

### Find usecase with clear classification problem 
  1. Y/N
  2. Problem code
  2. final decision
### Select columns for features which shouldn't include any form of predicting output

### Convert columns values to vectors 

### Use StringIndexer to convert string value to vector

### Use vectorindexer to optimize the prediction

### Use Assembler to combine all the vectors into single feature column

### Use Pipeline to automate the training 

### Setup algorithm with params

### build model

### show importance variables 

### Apply the model to testing set

### Compare the accuracy
 
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)d
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
