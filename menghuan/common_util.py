import win32con
import win32gui
from loguru import logger


def find_window(title_part="梦幻西游：时空"):
    """查找游戏窗口"""
    global hwnd
    hwnd = win32gui.FindWindow(None, title_part)
    if not hwnd:
        logger.error("未找到游戏窗口")
        raise Exception("未找到游戏窗口")

    # 设置窗口大小
    win32gui.SetWindowPos(hwnd, None, 0, 0, 1520, 855, win32con.SWP_NOMOVE)

    # 获取客户区大小
    _, _, width, height = win32gui.GetClientRect(hwnd)
    global client_rect
    client_rect = (0, 0, width, height)

    logger.info(f"窗口句柄: {hwnd}, 客户区大小: {width}x{height}")
    return hwnd
