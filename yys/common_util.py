import random
import time

import win32gui
from loguru import logger

from my_mouse import bg_left_click_with_range
from pic_and_color_util import bg_find_pic


def find_window(title_part="阴阳师-网易游戏"):
    """查找游戏窗口"""
    global hwnd
    hwnd = win32gui.FindWindow(None, title_part)
    if not hwnd:
        logger.error("未找到游戏窗口")
        raise Exception("未找到游戏窗口")

    # 设置窗口大小
    # win32gui.SetWindowPos(hwnd, None, 0, 0, 1136, 671, win32con.SWP_NOMOVE)

    # 获取客户区大小
    _, _, width, height = win32gui.GetClientRect(hwnd)
    global client_rect
    client_rect = (0, 0, width, height)

    logger.info(f"窗口句柄: {hwnd}, 客户区大小: {width}x{height}")
    return hwnd


def random_sleep(min, max):
    sleep_seconds = random.uniform(min, max)
    # logger.debug(f"等待{sleep_seconds}秒")
    time.sleep(sleep_seconds)


def click_battle_end(hwnd):
    point = bg_find_pic(hwnd, "images/battle_end.bmp")
    first_click = bg_left_click_with_range(hwnd, point, x_range=400, y_range=100)
    random_sleep(0.3, 0.6)
    second_click = bg_left_click_with_range(hwnd, point, x_range=400, y_range=100)
    random_sleep(1.2, 1.7)
    return first_click or second_click


def click_battle_end_1(hwnd):
    point = bg_find_pic(hwnd, "images/battle_end_1.bmp")
    first_click = bg_left_click_with_range(hwnd, point, x_range=400, y_range=70)
    random_sleep(0.1, 0.3)
    second_click = bg_left_click_with_range(hwnd, point, x_range=400, y_range=70)
    return first_click or second_click


def close_jia_cheng(hwnd):
    point = bg_find_pic(hwnd, "images/jia_cheng.bmp")
    if not bg_left_click_with_range(hwnd, point, x_range=10, y_range=10):
        return False
    random_sleep(0.5, 0.8)
    success_close_count = 0
    loop_count = 0
    while loop_count < 30 or success_close_count >= 2:
        loop_count += 1
        point = bg_find_pic(hwnd, "images/jia_cheng_ji_huo_zhong.bmp", 630, 100, 830, 480, similarity=0.9)
        if bg_left_click_with_range(hwnd, point, x_range=6, y_range=8):
            success_close_count += 1
        random_sleep(0.1, 0.3)
    return True
