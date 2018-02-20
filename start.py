"""starter"""
import msvcrt
import adb

out = adb.adb_sc() # screenshots
if out == 0: # exit the program
    print('Press any key to continue . . .')
    msvcrt.getch()
    exit()
