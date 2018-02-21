"""The ADB module"""
import subprocess  # use run()
import re  # use split()


def adb_sc():
    """screenshots"""
    out = subprocess.run('adb/adb devices', stdout=subprocess.PIPE)
    out = re.split(r"b'|\\t|\\n|\\r", out.stdout.__str__())
    if 'device' not in out:  # Check the devices status
        print("Please check the devices status.")
        return False
    else:
        subprocess.run('adb/adb shell screencap /sdcard/screen.png')  # ADB screenshots
        subprocess.run('adb/adb pull /sdcard/screen.png .')  # Copy the screenshot to the project root directory
        if input("The initial screenshot is completed. \nContinue? (y/n) ") in ['Y', 'y']:  # Whether to start
            return True
        else:
            return False
