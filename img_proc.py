"""Image Processing"""
import cv2

def edge_detection():
    """Canny edge detection"""
    img = cv2.imread('screen.png')
    cv2.imwrite('screen.png', cv2.Canny(img, 40, 85))

def score_recognition():
    """Score recognition"""
    img = cv2.imread('screen.png')
    height = img.shape[0]
    width = img.shape[1]
    # Get the picture size
    cropped = img[0:height//4, 0:width//2] # Get score screenshot

