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
        if piece_position:
            img = cv2.imread('screen.png')
            if piece_position[1] < img.shape[1] / 2:
                # if piece on the left, scanning right
               platform_position =  img_proc.find_platform(left = piece_position[1] + img.shape[1] * 0.03125)
            else:
                # if piece on the right, scanning left
                platform_position = img_proc.find_platform(right = piece_position[1])

            img[piece_position[0], piece_position[1]] = (255, 0, 0)
            img[platform_position[0], platform_position[1]] = (225, 0, 0)
            cv2.imwrite('center.png', img)
            # mark the position in the image


if __name__ == '__main__':
    main()
