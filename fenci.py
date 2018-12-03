# encoding=utf-8
import jieba

# 定义一个空字符串
final = ""
# 文件夹位置
filename = r"zhwiki_simple.txt"

# 打开文件夹，读取内容，并进行分词
with open(filename, 'r', encoding='utf8') as f:
    for line in f.readlines():
        word = jieba.cut(line)
        for i in word:
            final = final + i + " "

filesave=open("zhwiki_simple2.txt",'w')
filesave.write(final);
filesave.close()

print(final)

