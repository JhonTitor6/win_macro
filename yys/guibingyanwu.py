from yys.common_util import *
import config as config
from loguru import logger

config.DEBUG = True
hwnd = find_window()


def click_tiaozhan():
    point = bg_find_pic(hwnd, "images/guibingyanwu_tiaozhan.png")
    return bg_left_click_with_range(hwnd, point, x_range=20, y_range=20)


def get_max_battle_count():
    """获取用户输入的捉鬼轮数"""
    while True:
        try:
            default_max_battle_count = 100
            count = int(input(f"请输入要完成的次数(默认{default_max_battle_count}次): ") or default_max_battle_count)
            if count > 0:
                return count
            print("请输入一个正整数！")
        except ValueError:
            print("请输入有效的数字！")


def main():
    max_battle_count = get_max_battle_count()
    total_battle_count = 0
    next_sleep_counter = 0
    next_sleep_threshold = random.randint(40, 60)
    while total_battle_count < max_battle_count:
        click_tiaozhan()
        click_battle_end(hwnd)
        if click_battle_end_1(hwnd):
            total_battle_count += 1
            next_sleep_counter += 1
            logger.success(f"通关次数：{total_battle_count}")
        random_sleep(1, 2.5)

        # 防封逻辑，打一定场数后，随机休息一段时间
        if next_sleep_counter >= next_sleep_threshold:
            next_sleep_counter = 0
            sleep_duration = random.uniform(30, 60)
            logger.info(f"已完成 {total_battle_count} 场战斗，随机休息 {sleep_duration:.1f} 秒")
            time.sleep(sleep_duration)
            next_sleep_threshold = random.randint(40, 60)
    close_jia_cheng(hwnd)
    logger.info("已完成所有战斗，程序结束")


if __name__ == '__main__':
    # main()
    close_jia_cheng(hwnd)
