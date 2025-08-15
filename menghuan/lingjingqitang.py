from common_util import *
from my_mouse import *
from pic_and_color_util import *
import config

"""
灵境奇谭
"""

hwnd = find_window()
config.DEBUG = True

def click_que_ren_chu_shou():
    return bg_find_pic_and_click(hwnd, "images/ljqt_que_ren_chu_shou.png", similarity=0.6)


def main():
    while True:
        click_que_ren_chu_shou()
        time.sleep(2)


if __name__ == '__main__':
    main()
