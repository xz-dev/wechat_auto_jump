"""Starter"""
import cv2

import adb_utils
import img_proc


def main():
    """Main function"""
    out = adb_utils.adb_sc()  # screenshots
    if out:
        img_proc.edge_detection()
        piece_position =  img_proc.find_piece()
        img = cv2.imread('screen.png')
        cropped_piece = img[:,piece_position[1]:piece_position[1] + piece_position[2]]
        cv2.imwrite('piece.png', cropped_piece)
        if piece_position[1] < cv2.imread('screen.png').shape[1] / 2:
            img_proc.img_cropped(left = piece_position[1] + piece_position[2])
        else:
            img_proc.img_cropped(right = piece_position[1])


if __name__ == '__main__':
    main()
