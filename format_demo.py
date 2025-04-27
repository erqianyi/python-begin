# format

message_content = """
第一行文本
第二行文本，{param1}参数1
第三行，{param2}参数2
""".format(param1='aaa', param2='bbb')

print(message_content)

# f 字符串
param3 = 'ccc'
param4 = 'ddd'
message_content2 = f"""
第一行文本
第二行文本，参数3{param3}
第三行文本，参数4{param4}
"""
print(message_content2)

# f 用于数字保留位数
gpa_data = {'小明':3.251, '小红':3.869, '小李':2.683}
for name, gpa in gpa_data.items():
    print('{0}你好，你当前的绩点为：{1}'.format(name, gpa))

for name, gpa in gpa_data.items():
    print('{0}你好，你当前的绩点为(保留2位)：{1:.2f}'.format(name, gpa))

