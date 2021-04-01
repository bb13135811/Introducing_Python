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

fout = open('relativity', 'xt') # 使用x 避免覆寫
# 同時使用例外處理程式
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exist')

# 用read()、readline()、readlines()來讀取文字檔

# fin.read()，一次讀入全部，或是指定讀入字節數，注意記憶體占用情況
fin = open('relativity', 'rt') # 使用read()不使用引數則讀取整個檔案
poem = fin.read()
fin.close()
len(poem)

# 可提供最大字元數量，限制read()每次回傳的數量，每次讀取100字元，將每個段落附加到poem字串
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
    print("目前",len(poem),"字")
fin.close()
len(poem)

# fin.readline()，一次讀入一行
poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
    print('這行',len(line),'字')  # 含換行字元
fin.close()
len(poem)

# 使用迭代器，一次回傳一行
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)

# fin.readlines()，疊代器用法，寫法更好看
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines:
    print(line,end='!')


# 用write()寫入二進位檔案
bdata = bytes(range(0,256))
len(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()

# 用read()讀取二進位檔案
fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
fin.close()

# 用with自動關閉檔案
# 格式 -> expression as variable
with open('relativity', 'wt') as fout:
    fout.write(poem) # 這行程式完成後會自動關閉檔案

# 用seek()來更改位置
# file.tell()可以查詢讀取位置 seek(offset,origin)
fin = open('bfile', 'rb')
fin.tell()

# 使用seek()跳到檔案結尾的一個byte之前
fin.seek(255)


bdata = bytes(range(0, 256))
fin = open('bfile', 'wb')
fin.write(bdata)
fin.close()

fin = open('bfile', 'rb')
data = fin.read()
len(data)
fin.close()

fin = open('bfile', 'rb')
fin.tell()
fin.close()

fin.seek(255) # 跳到結尾前一個byte

bdata = fin.read() # 讀到檔案結尾
len(bdata) # 一個byte
bdata[0] # 這是256個byte裡的255位移植

# seek()也會回傳目前的位移 -> seek(offset, origin)
# origin = 0(預設)，從頭算起第offset個byte
# origin = 1，從目前位置算起第offset個byte
# origin = 2，從最後往前為算第offset個byte

import os # os模組定義這些值
os.SEEK_SET
os.SEEK_CUR
os.SEEK_END

# 以不同方式讀取最後的byte
fin = open('bfile', 'rb')
fin.seek(-1, 2) # 從最後讀取-1位移植
fin.tell()

bdata = fin.read()
len(bdata)
bdata[0]
fin.close()

fin = open('bfile', 'rb')
fin.seek(254, 0)
fin.tell()

fin.seek(1,1)
fin.tell()

bdata = fin.read()
len(bdata)
bdata[0]
# 以上函式適合用於二進位檔案 / 文字檔除非是ASCII，否則因字元bytes不同，計算位移植困難

# 文字檔結構

# CSV
# 常見分隔符號， 1.,  2. |  3. \t
# 轉義序列： 假如欄位內容有分隔字元，必須以引號匡選整欄 or 在前面加上轉義字元
# 檔案使用行尾字元
# 第一行可能是欄位名稱

# 如何讀取、寫入一連串的“列”，每一列有一連串的欄位
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofield'],
    ]
with open('villains', 'wt') as fout: # 寫入
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains', 'rt') as fin: # 讀取
    cin = csv.reader(fin)
    villains = [row for row in cin]
print(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last']) # 欄位名'first' 'last'
    villains = [row for row in cin]
print(villains)

# 使用新的DictWriter()重寫CSV檔
import csv
villains = [
    {'first':'Doctor','last':'No'},
    {'first':'Rosa', 'last':'Klebb'},
    {'first':'Mister','last':'Big'},
    {'first':'Auric', 'last':'Goldfinger'},
    {'first':'Ernst', 'last':'Blofield'},
    ]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last']) # 會建立有標頭行的檔案
    cout.writeheader() # 檔頭
    cout.writerows(villains)
print(villains)

# 將檔案讀回
import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin) # 忽略fieldname引數，使用檔案第一行的值作為欄位標籤
    villains = [row for row in cin]
villains


# XML
# 使用“標籤”劃分資料

# 1.標籤以<字元開頭
# 2.忽略空白字元
# 3.通常<menu>等開始標籤會匹配結束標籤</menu>
# 4.標籤可被嵌套在其他標籤裡
# 5.開始標籤裡可能會有選用的屬性
# 6.標籤裡可以放“值”
# 7.假如標籤內沒有值或子標籤，可用一個標籤敘述，在最後的括號前加上斜號，以取代開始與結束標籤
# 8.可以隨意選擇放置資料的位置

# 使用ElementTree解析XML
import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag

# 每個元素包含如下屬性
# tag：string物件，表示資料代表的種類。
# attrib：dictionary物件，表示附有的屬性。
# text：string物件，表示element的內容。
# tail：string物件，表示element閉合之後的尾跡。
# 若干子元素（child elements）

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attrubutes:', child.attrib)
len(root) # number of menu sections
len(root[0]) # number of breakfast items


# JSON
menu = \
{
"breakfast": {
        "hours": "7-11",
        "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
                }
        },
"lunch" : {
        "hours": "11-3",
        "items": {
                "hamburger": "$5.00"
                }
        },
"dinner": {
        "hours": "3-10",
        "items": {
                "spaghetti": "$8.00"
                }
        }
}

import json
menu_json = json.dumps(menu) # json.dumps()將python轉化為json
menu_json

menu2 = json.loads(menu_json) # json.loads() 將json轉化為python物件
menu2

import datetime
now = datetime.datetime.utcnow()
now
import json
json.dumps(now)

# 將datetime轉換成某些JSON了解的東西，例如字串 or epoch值
now_str = str(now)
json.dumps(now_str)

from time import mktime
now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)

#可以使用“繼承”修改JSON的編碼方式
import json
class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime): #isinstance()會檢查obj物件是否為datetime.datetime類別
            return int(mktime(obj.timetuple()))
         # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
json.dumps(now, cls=DTEncoder)
# 可使用isinstance()與適合類型的方式查看結構並檢視值
# 例如：項目為字典，可用keys()、values()、items()擷取內容
