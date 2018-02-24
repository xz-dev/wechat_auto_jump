"""Image Processing"""
import cv2
import numpy as np


def edge_detection(read_img='screen.png', save_name='edge.png'):
    """Canny edge detection"""
    img = cv2.imread(read_img)  # read image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edge_img = cv2.Canny(img, 75, 100)
    # edge_img = cv2.Canny(img_gray, 75, 100)
    cv2.imwrite(save_name, edge_img)
    return img, edge_img


def find_edge(edge_img, left, right, top=0.20, bottom=0.70):
    """
    Get all positions of white pixel
    to reduce the amount of computation
    """
    height = edge_img.shape[0]
    width = edge_img.shape[1]
    edge_positions = np.nonzero(edge_img[int(height * top):int(height * bottom), int(width * left):int(width * right)])
    return edge_positions[0] + int(height * top), edge_positions[1] + int(width * left)


def find_piece(img, edge_img):
    """find position of the piece"""
    height = img.shape[0]
    width = img.shape[1]
    h_top = x_left = x_right = 0
    edge_positions = find_edge(edge_img, left=0.25, right=0.75)
    if edge_positions:
        for h, x in zip(*edge_positions):
            if h > h_top:
                pixel = img[h][x]
                if pixel[0] in list(range(80, 84)) + list(range(70, 75)) \
                        and pixel[1] in list(range(53, 59)) + list(range(40, 45)) \
                        and pixel[2] in list(range(55, 60)) + list(range(40, 45)):
                    if not h_top:
                        h_top = h_bottom = h
                    if h > h_bottom:
                        h_bottom = h
    h_center = int(0.92857 * h_bottom + 0.071423 * h_top)
    # get the hight of piece
    if h_center == 0:
        print("Please confirm whether the screen is the game interface. ")
        return False
    for x in range(0, width):
        pixel = img[h_top, x]
        if pixel[0] in list(range(55, 84)) \
                and pixel[1] in list(range(50, 65)) \
                and pixel[2] in list(range(50, 80)):
            if not x_left:
                x_left = x_right = x
            else:
                x_right = x
        if x - x_left > width * 0.035:
            break
    x_center = int((x_left + x_right) * 0.5)
    # get the symmetry axis
    piece_position = (h_center, x_center)
    return piece_position


def find_platform(img, edge_img, left=0, right=0):
    """find position of the platform"""
    if not right:
        right = img.shape[1]
    height = img.shape[0]
    width = img.shape[1]
    # Get the range size
    edge_right = 0
    broadband_max = (0, 0, 0)
    platform_bgr = (-1, -1, -1)
    tmp_h = -1
    edge_positions = find_edge(edge_img, left=left / width, right=right / width, bottom=0.50)
    if edge_positions:
        for h, x in zip(*edge_positions):
            if platform_bgr[0] == -1 \
                    and (img[h][x] == img[h + 1][x]).all() \
                    and (img[h][x] == img[h + 2][x]).all() \
                    and (img[h][x] == img[h + 3][x]).all():
                # find the color of the platform
                platform_bgr = img[h][x]
                break
        for h, x in zip(*edge_positions):
            if (platform_bgr == img[h][x]).all():
                if h > tmp_h:
                    tmp_h = h
                    edge_left = (h, x)
                    if edge_right and edge_right[1] - edge_left[1] > broadband_max[2]:
                        broadband_max = (edge_right[0], edge_left[1], edge_right[1] - edge_left[1])
                else:
                    edge_right = (h, x)
    # find the center of platform
    platform_position = (broadband_max[0], broadband_max[1] + (broadband_max[2] + 1) // 2)
    return platform_position


def img_cropped(left=0, right=0):
    """cropped image into 2 parts (score and platform part)"""
    if not right:
        right = cv2.imread('screen.png').shape[1]
    img = cv2.imread('screen.png')
    height = img.shape[0]
    width = img.shape[1]
    # Get the picture size
    cropped_score = img[height // 11: height // 6, 0: width // 2]  # Get score screenshot
    cropped_pltform = img[height // 6: height * 2 // 3, left: right]
    cv2.imwrite('score.png', cropped_score)
    cv2.imwrite('pltform.png', cropped_pltform)


def score_recognition():
    """Score recognition"""
