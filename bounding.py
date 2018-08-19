import cv2
from pathlib import Path
import json
import math
import sys

def convert(file_path, output_directory, file_name):
    image = cv2.imread(file_path)
    print("image size: ", image.shape)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 3) # dilate
    _, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
    i = 1
    
    rects = []
    for contour in contours:
        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)

        # discard areas that are too large
        #if h>500 and w>500:
        #    continue

        # discard areas that are too small
        #if h<40 or w<40:
        #    continue

        # draw rectangle around contour on original image
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)    
        rects.append( {"rect": 
            {
             "x1": (x), 
             "y1": (y), 
             "x2": (x+w), 
             "y2": (y+h)
            }
        } )
        
        # write original image with added contours to disk  
        
    
    output = output_directory + "\\" + file_name
    data = {"fileName": output, "bounds": rects}
    j = json.dumps(data)
    f = open(output + ".json", "w")
    f.write(j)
    print(j)
    print("Writing " + output + "...")
    cv2.imwrite(output, image)



image_directory = sys.argv[1] 
output_directory = sys.argv[2]

print("image_directory : ", image_directory )
print("output_directory: ", output_directory)

pathlist = Path(image_directory).glob('**/*.png')
for path in pathlist:
    path_in_str = str(path)
    print(path_in_str)
    convert(path_in_str, output_directory, path.name)
      
print("output folder : " + output_directory)
    
