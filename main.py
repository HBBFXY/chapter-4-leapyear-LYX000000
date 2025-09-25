def is_leap_year(year):
    """
    判断给定的年份是否为闰年
    闰年规则：能被4整除但不能被100整除，或者能被400整除
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    print("=== 闰年判断程序 ===")
    print("请输入一个年份，程序将判断是否为闰年")
    print("输入 'quit' 退出程序\n")
    
    while True:

