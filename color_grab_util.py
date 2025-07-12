import cv2
import numpy as np
from PIL import ImageGrab


def select_screen_region():
    """让用户用鼠标框选一个屏幕区域"""
    print("请拖动鼠标选择一个屏幕区域...")
    screen = ImageGrab.grab()
    screen_np = np.array(screen)
    r = cv2.selectROI("Select Region", screen_np, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Region")
    return r  # x, y, w, h


def get_points_from_image(img, max_points=10):
    """让用户在指定图像上点击选择点位，并支持撤销"""
    points = []

    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < max_points:
            points.append((x, y))
            print(f"已选点：({x}, {y})")
            cv2.circle(img_draw, (x, y), 1, (0, 255, 0), -1)
            cv2.imshow("Click to select points", img_draw)
        elif event == cv2.EVENT_RBUTTONDOWN and len(points) > 0:
            # 右键点击撤销最后一个点
            removed = points.pop()
            print(f"已撤销点：{removed}")
            # 重新绘制图像和剩余点
            img_draw[:] = img.copy()
            for px, py in points:
                cv2.circle(img_draw, (px, py), 1, (0, 255, 0), -1)
            cv2.imshow("Click to select points", img_draw)

    img_draw = img.copy()

    # 创建窗口并设置为NORMAL以防止自动缩放
    cv2.namedWindow("Click to select points", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Click to select points", click_event)

    cv2.imshow("Click to select points", img_draw)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == 13 or key == 27 or len(points) >= max_points:  # Enter 或 Esc 或满点数
            break

    cv2.destroyAllWindows()
    return points


def generate_color_list_from_user_input(max_points=10):
    """
    用户交互式生成 color_list
    :param max_points: 最多允许选择的点数
    :return: color_list 格式为 [(dx, dy, (r, g, b)), ...]
    """
    # 步骤1：用户框选屏幕区域
    # x0, y0, w, h = select_screen_region()
    # x1, y1 = x0 + w, y0 + h

    # 截图选定区域
    img = ImageGrab.grab()
    img_np = np.array(img)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # 步骤2：让用户在截图上点击选择点位
    points = get_points_from_image(img_bgr, max_points)

    # 步骤3：生成 color_list
    color_list = []
    for x, y in points:
        pixel = img_np[y, x]  # RGB格式
        r, g, b = pixel
        dx = x
        dy = y
        color_list.append((dx, dy, (int(r), int(g), int(b))))

    print("\ncolor_list 已生成，可用于 find_multiple_colors 函数：")
    for item in color_list:
        print(item)

    return color_list


# 🚀 启动交互式生成器
if __name__ == "__main__":
    generate_color_list_from_user_input(max_points=20)
