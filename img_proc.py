"""Image Processing"""
import cv2
import numpy as np


def edge_detection(read_img = "screen.png", save_name = 'edge.png'):
    #"""BackgroundSubtractorMOG2"""
    #fgbg = cv2.createBackgroundSubtractorMOG2( detectShadows=True)
    #fgmask = fgbg.apply(img)
    #cv2.imwrite('BackgroundSubtractorMOG2.png', fgmask)
    """Canny edge detection"""
    img = cv2.imread(read_img) # read image
    cv2.imwrite(save_name, cv2.Canny(img, 75, 100))

def find_edge(read_img = "edge.png", top = 0.80, bottom = 0.30):
    """
    Get all positions of white pixel
    to reduce the amount of computation
    """
    img = cv2.imread(read_img) # read image
    height = img.shape[0]
    width = img.shape[1]
    cv2.imwrite('piece.png', img[ int(height * bottom) : int(height * top), : ])
    edge_positions = []
    img_array=np.array(img)  # Open the image and convert it to a numeric matrix
    for h in range( int(height * bottom), int(height * top)): # search range
        for x in range(0, width):
            pixel = img_array[h][x]
            if pixel[0] != 0:
                edge_positions.append((h, x))
    print(len(edge_positions))
    return  edge_positions


def find_piece(read_img = "screen.png"):
    """find position of the piece""" 
    img = cv2.imread(read_img) # read image
    img_array=np.array(img)  # Open the image and convert it to a numeric matrix
    for temp in range(0, 13):
        print(img_array[0][temp])
    height = img.shape[0]
    width = img.shape[1]
    n_array = []
    broadband_array = []
    edge_right = 0
    tmp_h = -1
    broadband_mix = 0
    edge_positions = find_edge()
    if edge_positions:
        for z in range(0, len(edge_positions)):
            h = edge_positions[z][0]
            x = edge_positions[z][1]
            pixel = img_array[h][x]
            for rbg in range(0,2):
                if pixel[0] in list(range(80, 84)) + list(range(70, 75)) \
                    and pixel[1] in list(range(53, 59)) + list(range(40, 45)) \
                    and pixel[2] in list(range(55, 60)) + list(range(40, 45)):
                    if h > tmp_h:
                        tmp_h = h
                        if edge_right:
                            broadband_array.append((edge_right[0], edge_left[1],
                                             edge_right[1] - edge_left [1]))
                        edge_left = (h, x)
                    else:
                        edge_right = (h, x)
    for broadband_tmp in broadband_array:
        if not broadband_mix:
            broadband_mix = broadband_tmp
        if broadband_mix[2] < broadband_tmp[2]:
            broadband_mix = broadband_tmp
    print(broadband_mix)
    return broadband_mix

def img_cropped(left = 0, right = 0):
    print(left)
    print(right)
    if not right:
        right = cv2.imread('screen.png').shape[1]
    print(cv2.imread('screen.png').shape[1])
    """cropped image into 2 parts (score and platform part)"""
    img = cv2.imread('screen.png')
    height = img.shape[0]
    width = img.shape[1]
    # Get the picture size
    cropped_score = img[height // 11 : height // 6, 0 : width // 2] # Get score screenshot
    cropped_pltform = img[height // 6 : height  * 12 // 13,  left : right]
    cv2.imwrite('score.png', cropped_score)
    cv2.imwrite('pltform.png', cropped_pltform)

def division(img):
    """Watershed algorithmr"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray.png', gray)
    #kernel = np.ones((3, 3), np.uint8)
    #opening = cv2.morphologyEx(gray)


def score_recognition():
    """Score recognition"""
