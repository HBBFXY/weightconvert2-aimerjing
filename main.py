# 在这个文件里编写代码
# 获取当前体重
# 增加一个空行
current_weight = float(input("请输入当前体重(kg): "))

# 打印表头
print("年份\t地球体重(kg)\t月球体重(kg)")

# 计算并输出未来10年体重
for year in range(1, 11):
    earth_weight = current_weight + 0.5 * year
    moon_weight = earth_weight * 0.165
    
    # 格式化输出：年份（整数）、地球体重（保留1位小数）、月球体重（保留3位小数）
    print(f"{year}\t{earth_weight:.1f}\t\t{moon_weight:.3f}")
