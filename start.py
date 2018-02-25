"""Starter"""
import cv2
import numpy as np

import time
import random

import adb_utils
import img_proc


def main():
    """Main function"""
    i = 0
    out = True

    try:
        with open('profile/default.txt', 'r') as f:
            str = f.read().split()
            phone_model = str[0]
            debug_mode = str[1]
    except FileNotFoundError:
        phone_model = input("Please enter your cellphone model now. ")
        debug_mode = input("Whether to open the debug mode? (y/n)")
        if debug_mode in ['y', 'Y']:
            debug_mode = 'True'
        else:
            debug_mode = 'False'
        with open('profile/default.txt', 'w') as f:
            f.write(phone_model)
            f.write(' ')
            f.write(debug_mode)

    with open('profile/' + phone_model + '.txt', 'r') as f:
        coefficient = float(f.read())
    print("Current configuration: " + phone_model)
    print("Debug mode: " + debug_mode)
    print("Profile: profile/default.txt")
    # Determine the configuration of cellphone model
    # Whether to open the debug mode

    while True and out:
        out = adb_utils.adb_sc()  # screenshots
        if out:
            print("Wait...")
            # platform_position = 0
            img, avatar_img, edge_img = img_proc.edge_detection()

            avatar_position, top_left, bottom_right = img_proc.find_avatar(img, avatar_img)
            if avatar_position:
                if avatar_position[1] < img.shape[1] / 2:
                    # if avatar on the left, scanning right
                    platform_position = img_proc.find_platform(img, edge_img, left=avatar_position[1] + img.shape[1] * 0.04)
                else:
                    # if avatar on the right, scanning left
                    platform_position = img_proc.find_platform(img, edge_img, right=avatar_position[1] - img.shape[1] * 0.04)

                img[avatar_position[0], avatar_position[1]] = (255, 0, 0)
                img[platform_position[0], platform_position[1]] = (225, 0, 0)
                cv2.rectangle(img, (top_left[1], top_left[0]), (bottom_right[1], bottom_right[0]), (255, 255, 255), 2)
                # mark the position in the image
                if debug_mode == 'True':
                    cv2.imwrite('images/center_{}.png'.format(i), img)
                i += 1
                dis = np.sqrt((avatar_position[0] - platform_position[0]) ** 2 + (avatar_position[1] - platform_position[1]) ** 2)
                adb_utils.adb_touch(int(coefficient * dis))
                time.sleep(random.uniform(1.2, 1.4))


if __name__ == '__main__':
    main()
