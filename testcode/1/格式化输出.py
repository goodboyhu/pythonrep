name = "大明"
print("我的名字叫 %s，请多多关照！"%name)
student_no = 1
print("我的学号是 %06d" % student_no)  # 输出整数位数为6，不足补零。
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.4f 元。" % (price,weight,money))  # %.2f保留2位小数，默认是6位小数。
scale = 0.25
print("数据比例是%.2f%%。" % scale * 10)
print("数据比例是%.2f%%。" % (scale * 100))