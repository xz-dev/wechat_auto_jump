"""Starter"""
import cv2
import numpy as np

import time
import json
import random

import adb_utils
import img_proc


def main():
    """Main function"""
    i = 0
    out = True

    avatar_img = cv2.imread('images/player.png')
    avatar_img = cv2.cvtColor(avatar_img, cv2.COLOR_BGR2GRAY)

    try:
        with open('profile/default.json', 'r') as f:
            configuration = json.load(f)
            phone_model = configuration["cellType"]
            debug_mode = configuration["debug"]
    except FileNotFoundError:
        phone_model = input("Please enter your cellphone model now. ")
        debug_mode = input("Whether to open the debug mode? (y/n)")
        if debug_mode in ['y', 'Y']:
            debug_mode = True
        else:
            debug_mode = False
        with open('profile/default.json', 'w') as f:
            configuration = {"cellType": phone_model, "dedug": debug_mode}
            json.dump(configuration, f)
    try :
        with open('profile/{cellPhone}.json'.format(cellPhone = phone_model), 'r') as f:
            configuration = json.load(f)
            resolution = configuration["resolution"]
            coefficient= configuration["coefficient"] 
    except FileNotFoundError:
        print("Please confirm \"default.json\" is right or contact the provider. ")
    with open('profile/{resolution}.json'.format(resolution = resolution), 'r') as f:
        configuration = json.load(f)
        scale = configuration["scale"]
    print("Current configurationuration: " + phone_model)
    print("Debug mode: " + str(debug_mode))
    print("Profile: profile/default.json")
    # Determine the configuration of cellphone model
    # Whether to open the debug mode

    while True and out:
        out, img = adb_utils.adb_sc()  # screenshots
        if out:
            print("Wait...")
            edge_img = img_proc.edge_detection(img = img, debug_mode = debug_mode)

            avatar_position, top_left, bottom_right = img_proc.find_avatar(img, avatar_img, scale)
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
                if debug_mode:
                    cv2.imwrite('images/center_{}.png'.format(i), img)
                    i += 1
                dis = np.sqrt((avatar_position[0] - platform_position[0]) ** 2 + (avatar_position[1] - platform_position[1]) ** 2)
                adb_utils.adb_touch(int(coefficient * dis), h1 = avatar_position[0], x1 = avatar_position[1], h2 = platform_position[0], x2 = platform_position[1])
        time.sleep(random.uniform(1.2, 1.4))


if __name__ == '__main__':
    main()
