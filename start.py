"""启动文件"""
import msvcrt
import adb

out = adb.adb_sc() # 调用ADB模块截图
if out == 0:
    print('按任意键结束')
    msvcrt.getch()
    exit()
