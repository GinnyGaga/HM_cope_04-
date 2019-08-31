def print_line(char,times):
    """打印单行分隔符号
    :param char: 单行分隔符号样式
    :param times: 单行分隔符重复次数

    """

    print(char * times)

def print_lines(char,times):
    """打印多行分隔符号

    :param char: 分隔符号样式
    :param times: 分隔重复次数
    """
    row = 0
    while row < 5:
        print_line(char,times)
        row += 1

print_lines("2",6)