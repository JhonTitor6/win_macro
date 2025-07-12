from menghuan.common_util import find_window
from pic_and_color_util import *
from menghuan.config import init
import config

'''
挖宝
'''

config.DEBUG = True

def click_use(hwnd):
    return bg_find_pic_and_click(hwnd, "images/use.bmp", similarity=0.5)


def main():
    init()
    hwnd = find_window()
    while True:
        click_use(hwnd)
        time.sleep(1)


if __name__ == '__main__':
    main()
