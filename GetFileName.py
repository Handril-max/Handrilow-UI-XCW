import os
import sys
print('Handrilsoft\n文件名称获取并列出模块\n欢迎使用')
input('————————\n按回车以获取\n————————')
word = os.listdir(sys.path[0])
word2 = str("\n".join(word))
print(word2)

input('————————\n复制后按回车结束程序')
