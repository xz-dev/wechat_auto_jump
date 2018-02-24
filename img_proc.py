"""Image Processing"""
import cv2
import numpy as np


def edge_detection(read_img = 'screen.png', save_name = 'edge.png'):
    """Canny edge detection"""
    img = cv2.imread(read_img) # read image
    cv2.imwrite(save_name, cv2.Canny(img, 75, 100))

def find_edge(left, right, top = 0.20, bottom = 0.70 , read_img = "edge.png"):
    """
    Get all positions of white pixel
    to reduce the amount of computation
    """
    img = cv2.imread(read_img) # read image
    height = img.shape[0]
    width = img.shape[1]
    edge_positions = []
    img_array=np.array(img)  # Open the image and convert it to a numeric matrix
    for h in range( int(height * top), int(height * bottom)): # search range
        for x in range(int(width * left), int(width * right)):
            pixel = img_array[h][x]
            if pixel[0] != 0:
                edge_positions.append((h, x))
    return  edge_positions

def find_piece(read_img = "screen.png"):
    """find position of the piece""" 
    img = cv2.imread(read_img) # read image
    img_array=np.array(img)  # Open the image and convert it to a numeric matrix
    height = img.shape[0]
    width = img.shape[1]
    h_top = x_left = x_right = 0
    broadband_mix = 0
    edge_positions = find_edge(left = 0.25, right = 0.75)
    if edge_positions:
        for z in range(0, len(edge_positions)):
            h = edge_positions[z][0]
            x = edge_positions[z][1]
            if h > h_top:
                pixel = img_array[h][x]
                if pixel[0] in list(range(80, 84)) + list(range(70, 75)) \
                    and pixel[1] in list(range(53, 59)) + list(range(40, 45)) \
                    and pixel[2] in list(range(55, 60)) + list(range(40, 45)):
                    if not h_top:
                        h_top = h_bottom = h
                    if h > h_bottom:
                        h_bottom = h
    h_center = int((0.92857 *h_bottom + 0.071423 * h_top))
    # git the hight of piece
    if h_center == 0:
        print("Please confirm whether the screen is the game interface. ")
        return False
    for x in range(0, width):
        pixel = img_array[h_top, x]
        if pixel[0] in list(range(55, 84)) \
            and pixel[1] in list(range(50, 65)) \
            and pixel[2] in list(range(50, 80)):
            if not x_left:
                x_left = x_right = x
            else:
                x_right = x
        if x_right - x_left > width * 0.03125:
            break
    x_center = int((x_left + x_right) * 0.5)
    # git the symmetry axis
    piece_position = (h_center, x_center)
    return piece_position

def find_platform(read_img =  'screen.png', left = 0, right = 0):
    """find position of the platform"""
    img = cv2.imread(read_img) # read image
    img_array=np.array(img)  # Open the image and convert it to a numeric matrix
    if not right:
        right = cv2.imread('screen.png').shape[1]
    height = img.shape[0]
    width = img.shape[1]
    # Get the range size
    n_array = []
    broadband_array = []
    edge_right = 0
    platform_bgr = (-1, -1, -1)
    tmp_h = -1
    broadband_mix = 0
    # set some necessary value
    edge_positions = find_edge(left = left / width, right = right / width, bottom = 0.50)
    if edge_positions:
        for z in range(0, len(edge_positions)):
            h = edge_positions[z][0]
            x = edge_positions[z][1]
            if platform_bgr[0] == -1 \
                and (img_array[h][x] == img_array[h + 1][x]).all() \
                and (img_array[h][x] == img_array[h + 2][x]).all() \
                and (img_array[h][x] == img_array[h + 3][x]).all():
                # find the color of the platform
                    platform_bgr = img_array[h][x]
                    break
        for z in range(0, len(edge_positions)):
            h = edge_positions[z][0]
            x = edge_positions[z][1]
            if (platform_bgr == img_array[h][x]).all():
                if h > tmp_h:
                    tmp_h = h
                    edge_left = (h, x)
                    if edge_right and edge_right[1] - edge_left [1] > 0:
                        broadband_array.append((edge_right[0], edge_left[1],
                                                edge_right[1] - edge_left [1]))
                else:
                    edge_right = (h, x)
        for broadband_tmp in broadband_array:
            if not broadband_mix:
                broadband_mix = list(broadband_tmp)
            if broadband_mix[2] <= broadband_tmp[2]:
                broadband_mix = list(broadband_tmp)
    # find the center of  platform
    broadband_mix[2] += 1
    platform_position = (broadband_mix[0], broadband_mix[1] + broadband_mix[2] // 2)
    return platform_position

def img_cropped(left = 0, right = 0):
    """cropped image into 2 parts (score and platform part)"""
    if not right:
        right = cv2.imread('screen.png').shape[1]
    img = cv2.imread('screen.png')
    height = img.shape[0]
    width = img.shape[1]
    # Get the picture size
    cropped_score = img[height // 11 : height // 6, 0 : width // 2] # Get score screenshot
    cropped_pltform = img[height // 6 : height  * 2 // 3,  left : right]
    cv2.imwrite('score.png', cropped_score)
    cv2.imwrite('pltform.png', cropped_pltform)

def score_recognition():
    """Score recognition"""
