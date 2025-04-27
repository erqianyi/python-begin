# for in
# 字典的迭代：
# some_dict.keys() 所有键
# some_dict.values() 所有值
# some_dict.items() 所有键值对

# range 整数序列

for num in range(1, 10, 2):
    print(num)

# 计算 1加到100
total = 0
for i in range(1, 101):
    total = total + i
print(total)