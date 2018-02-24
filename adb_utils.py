"""The ADB module"""
import subprocess  # use run()
import re  # use split()


def adb_sc():
    """screenshots"""
    out = subprocess.run('adb/adb devices', stdout=subprocess.PIPE)
    out = re.split(r"b'|\\t|\\n|\\r", out.stdout.__str__())
    if 'device' not in out:  # Check the devices status
        print("Please check the devices status.")
        print("We cannot capture the screenshot of your device. Please try again.")
        return False
    else:
        subprocess.run('adb/adb shell screencap /sdcard/screen.png')  # ADB screenshots
        subprocess.run('adb/adb pull /sdcard/screen.png .')  # Copy the screenshot to the project root directory
        return True

def adb_touch(time, h1 = 500, x1 = 500, h2 = 500, x2 = 500):
    adb_swipe = 'adb/adb shell  input swipe ' + str(h1) + ' ' + str(x1) + ' ' + str(h2) + ' ' + str(x2) + ' ' + str(time)
    print(adb_swipe)
    subprocess.run(adb_swipe)
   
