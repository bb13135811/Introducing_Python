# 檔案輸入/輸出
# fileobj = open(filename, mode)
#(open()回傳的檔案物件)       (指示檔案類型)

# 使用write()來編寫文字檔案
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
len(poem)
fout = open('relativity', 'wt')
fout.write(poem)  # write()會回傳被寫入的byte數量
fout.close()


fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

# 使用print寫入時可以使用sep與end參數指定分隔符號與結束符號
# sep，預設為空格' '
# end，預設為換行'\n'

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='') # 除非傳入其他東西，否則使用預設值
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()



