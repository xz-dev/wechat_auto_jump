"""Starter"""
import msvcrt
import adb

def main():
    """Main function"""
    out = adb.adb_sc() # screenshots
    if out == 0: # error
        print('Press any key to continue . . .')
        msvcrt.getch()
        exit()

if __name__ == '__main__':
    main()
