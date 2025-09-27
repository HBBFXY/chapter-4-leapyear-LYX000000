def main():
    try:
        # 获取用户输入
        year_input = input().strip()
        
        # 处理空输入
        if not year_input:
            print("输入错误")
            return
            
        # 检查输入是否为整数
        try:
            year = int(year_input)
        except ValueError:
            # 尝试处理浮点数输入
            if '.' in year_input:
                print("输入错误")
                return
            else:
                print("输入错误")
                return
        
        # 处理负年份
        if year < 0:
            print("不是闰年")
            return
            
        # 判断闰年
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("是闰年")
        else:
            print("不是闰年")
            
    except Exception:
        print("输入错误")

if __name__ == "__main__":
    main()
