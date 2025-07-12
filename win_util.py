import win32gui


def find_window(class_name=None, window_name=None):
    """

    :param class_name:
    :param window_name:
    :return: str hwnd
    """
    return win32gui.FindWindow(class_name, window_name)
