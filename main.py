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
        try:
            # 获取用户输入
            user_input = input("请输入年份: ").strip()
            
            # 检查是否退出
            if user_input.lower() == 'quit':
                print("程序已退出，再见！")
                break
            
            # 尝试转换为整数
            year = int(user_input)
            
            # 检查年份是否合理（假设我们只考虑公元后的年份）
            if year <= 0:
                print("错误：请输入一个有效的正数年份\n")
                continue
            
            # 判断是否为闰年并输出结果
            if is_leap_year(year):
                print(f"{year}年是闰年 ✓")
            else:
                print(f"{year}年不是闰年 ✗")
            
            print()  # 空行分隔
            
        except ValueError:
            print("错误：请输入有效的数字年份\n")
        except Exception as e:
            print(f"发生未知错误：{e}\n")

if __name__ == "__main__":
    main()

