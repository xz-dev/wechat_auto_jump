"""Starter"""
import cv2

import adb_utils
import img_proc


def main():
    """Main function"""
    out = adb_utils.adb_sc()  # screenshots
    if out:
        print("Wait...")
        platform_position = 0
        img_proc.edge_detection()
        piece_position =  img_proc.find_piece()
        img = cv2.imread('screen.png')
        cropped_piece = img[:,piece_position[1]:piece_position[1] + piece_position[2]]
        img[piece_position[0]] = (0, 0, 0)
        cv2.imwrite('piece.png', cropped_piece)
        if piece_position[1] < cv2.imread('screen.png').shape[1] / 2:
           platform_position =  img_proc.find_platform(left = piece_position[1] + piece_position[2])
        else:
            platform_position = img_proc.find_platform(right = piece_position[1])
        cropped_platform = img[:,:]
        img[platform_position[0]] = (0, 0, 0)
        cv2.imwrite('platform.png', cropped_platform)


if __name__ == '__main__':
    main()
