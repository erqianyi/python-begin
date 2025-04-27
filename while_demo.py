# 根据用户输入算平均值
print('这是一个求平均值的程序！')

total = 0
count = 0

user_input = input('请输入数字（完成所有数字输入后，请输入 q 终止程序）：')

while user_input != 'q':
    num = float(user_input)
    total += num
    count += 1
    user_input = input('请输入数字（完成所有数字输入后，请输入 q 终止程序）：')

if count == 0:
    result = 0
else:
    result = total / count

print('所得平均值为：' + str(result))
