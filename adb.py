"""调用ADB"""
import os

def adb_sc():
    """ADB截图"""
    os.chdir('adb')
    out = os.popen('adb devices').read() # 检查设备状态
    print(out)
    if 'device' not in str.split(out):
        print('请检查设备状态\n')
        return(0)
    else:
        os.popen('adb shell screencap /sdcard/screen.png') # ADB工具截图
        os.popen('adb pull /sdcard/screen.png ..') # 拉取截图至项目根目录
        print('初始截图完成')
        return(1)
