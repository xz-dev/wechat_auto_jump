"""Transfer the ADB module"""
import subprocess # use run()
import re #use split()

def adb_sc():
    """screenshots"""
    out = subprocess.run(r'adb\adb devices', stdout=subprocess.PIPE)
    out = re.split(r"b'|\\t|\\n|\\r", out.stdout.__str__())
    if 'device' not in out: # Check the devices status
        print('Please check the devices status. \n')
        return 0
    else:
        subprocess.run(r'adb\adb shell screencap /sdcard/screen.png') # ADB screenshots
        subprocess.run(r'adb\adb pull /sdcard/screen.png .') # Copy the screenshot to the project root directory
        if (input('The initial screenshot is completed. \nContinue? (y/n) ') in ['Y', 'y']): # Whether to start
            return 1
        else:
            return 0
