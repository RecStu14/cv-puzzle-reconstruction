
#Importing Necessary Libraries
import numpy as np
import cv2
import os

#Importing Necessary Files
import PATHS as PATHS

red = [(0,0,200),(20,20,255)]
blue = [(200,0,0), (255,20,20)]

dot_colours = {"BLUE": blue, "RED": red}

colour_names = list(dot_colours.keys())
colour_limits = list(dot_colours.values())
    
contents = os.listdir(PATHS.SIMPLE_DIR)
info_dict = dict()

for i in range(len(contents)):
    image_path = os.path.join(PATHS.SIMPLE_DIR, contents[i])
    
    img = cv2.imread(image_path) 

    count = -1
    pos_values = []

    print(f"Image: {contents[i]}")

    for lower, upper in colour_limits:
        count += 1
        output = img.copy()
        # apply threshhold color to white (255,255, 255) and the rest to black(0,0,0)
        mask = cv2.inRange(img,lower,upper) 
        

        circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,20,param1=20,param2=8,
                                minRadius=0,maxRadius=60)    
        index = 0
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")

            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                index = index + 1
        
            pos_values.append(index)
            info_dict[contents[i]] = pos_values
            
    print(f'No. of BLUE circles detected = {pos_values[0]}')
    print(f'No. of RED circles detected = {pos_values[-1]}\n')

for k,v in info_dict.items():
    print(k, '--', v)

#helper function to get the number of rows and columns needed in the picture            
def get_details(dictionary):
    values = list(dictionary.values())
    rows = set()
    cols = set()

    print(values)

    for i,j in values:
        rows.add(i)
        cols.add(j)

    return max(rows), max(cols)

num_rows, num_cols = get_details(info_dict)

print("n:", num_rows, num_cols)

#sorting the images by their rows and cols
info_dict_values = list(info_dict.values())
info_dict_keys = list(info_dict.keys())

ordered_values = sorted(info_dict_values)
print('ordered vals:', ordered_values)

"""
EG.. cjj..
r1.. 3k..
"""

temp = []
count = 0

ordered_imgs = [info_dict_keys[n:n+num_cols][::-1] for n in range(0, len(ordered_values), num_cols)]
