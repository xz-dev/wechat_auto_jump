"""The ADB module"""
import cv2
import subprocess  # use run()
import re  # use split()
import tempfile
import os
import random


def adb_sc():
    """screenshots"""
    out = subprocess.run('adb/adb devices', stdout=subprocess.PIPE)
    out = re.split(r"b'|\\t|\\n|\\r", out.stdout.__str__())
    if 'device' not in out:  # Check the devices status
        print("Please check the devices status.")
        print("We cannot capture the screenshot of your device. Please try again.")
        return False, None
    else:
        subprocess.run('adb/adb shell screencap /sdcard/screen.png')  # ADB screenshots
        if not os.path.isdir('images'):
            os.mkdir('images')
        with tempfile.TemporaryDirectory() as tempDir:
            subprocess.run('adb/adb pull /sdcard/screen.png {TEMP}/screen.png'.format(TEMP = tempDir))  # Copy the screenshot to the project root directory
            sc_img = cv2.imread('{TEMP}/screen.png'.format(TEMP = tempDir))
        return True, sc_img


def adb_touch(time, h1=500, x1=500, h2=500, x2=500):
    h1 += random.randint(0, 50)
    x1 += random.randint(0, 50)
    h2 += random.randint(0, 50)
    x2 += random.randint(0, 50)
    adb_swipe = 'adb/adb shell input swipe {x1} {h1} {x2} {h2} {time}'.format(h1=h1,x1=x1,h2=h2,x2=x2,time=time) 
    print(adb_swipe)
    subprocess.run(adb_swipe)
