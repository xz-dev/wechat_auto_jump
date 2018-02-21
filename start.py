"""Starter"""
import adb_utils


def main():
    """Main function"""
    out = adb_utils.adb_sc()  # screenshots
    if not out:
        print("We cannot capture the screenshot of your device. Please try again.")


if __name__ == '__main__':
    main()
