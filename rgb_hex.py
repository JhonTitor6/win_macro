def rgb2hex(rgb_tuple):
    """
    将RGB元组转换为十六进制颜色字符串
    :param rgb_tuple: (r, g, b)格式的元组
    :return: 十六进制颜色字符串(不带#)
    """
    return '{:02X}{:02X}{:02X}'.format(*rgb_tuple)


def hex2rgb(hex_str):
    """
    将十六进制颜色字符串转换为RGB元组
    :param hex_str: 十六进制颜色字符串(带或不带#) BBGGRR
    :return: (b, g, r)格式的元组
    """
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))
