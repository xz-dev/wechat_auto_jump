"""Starter"""
import cv2

import adb_utils
import img_proc


def main():
    """Main function"""
    # out = adb_utils.adb_sc()  # screenshots
    out = True
    if out:
        print("Wait...")
        # platform_position = 0
        img, edge_img = img_proc.edge_detection()

        piece_position = img_proc.find_piece(img, edge_img)
        if piece_position:
            if piece_position[1] < img.shape[1] / 2:
                # if piece on the left, scanning right
                platform_position = img_proc.find_platform(img, edge_img, left=piece_position[1] + img.shape[1] * 0.03125)
            else:
                # if piece on the right, scanning left
                platform_position = img_proc.find_platform(img, edge_img, right=piece_position[1])

            img[piece_position[0], piece_position[1]] = (255, 0, 0)
            img[platform_position[0], platform_position[1]] = (225, 0, 0)
            # mark the position in the image
            cv2.imwrite('center.png', img)


if __name__ == '__main__':
    main()
