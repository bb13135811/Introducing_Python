<<<<<<< HEAD
# lookup()接收一個不分大小寫的名稱,回傳一個Unicode字元
# name()接收一個Unicode字元,回傳一個大寫名稱

#編寫一個測試函式,接收Unicode字元,查看名稱,用該名稱再次查看字元
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value = "%s", name = "%s", value2 = "%s",' % (value, name, value2))
unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')

#使用字形在顯示文字上的限制,可能顯示一些預留位置字元
unicode_test('\u2603')

place = 'Café'
place
unicode_test('\u00e9')
place = 'caf\u00e9'
place
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
place

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
u_umlaut
drink = 'Grew' + u_umlaut + 'rztraminer'
print('Have a', drink,'in the', place )

#字串函式len會計算Unicode字元的數目,而不是byte數
len('$')
unicode_test('$')
len('\u0024')

# 以UTF-8編碼與解碼

#編碼
#將字串編碼成byte  /  使用encode()函式,第一個引數是編碼名稱
#可將任何東西編碼成UTF-8
snowman = '\u2603' #將Unicode字串'\u2603'指派給名稱snowman
len(snowman) # 因snowman為一個'字串',有一個字元
ds = snowman.encode('utf-8')
ds #ds是一個byte變數
len(ds) #使用三個byte來編碼一個snowman Unicode字元

#可使用UTF-8以外的編碼,但如果不是有效的字元,會顯示錯誤
ds = snowman.encode('ascii')

# encode()函式會接收第二個引數幫助編碼例外, 預設值為'strict'
snowman.encode('ascii', 'ignore') #使用ignore來丟棄無法編碼的東西
snowman.encode('ascii', 'replace') #使用replace將未知字元換成 '?'
snowman.encode('ascii', 'backslashreplace') #使用'backslashreplace'產生Python Unicode字元字串
snowman.encode('ascii', 'xmlcharrefreplace') #產生字元實體字串,可在網頁中使用


#解碼
#將byte字串解碼成Unicode字串

place = 'caf\u00e9'
place
type(place)

#以UTF-8格式 將他編碼成byte變數
place_bytes = place.encode('utf-8')
place_bytes
type(place_bytes)
len(place_bytes)
place2 = place_bytes.decode('utf-8')# 將byte字串解碼回Unicode字串
place2

place3 = place_bytes.decode('ascii')
place3

place4 = place_bytes.decode('latin-1')
place4
place5 = place_bytes.decode('windows-1252')
place5
# 請使用UTF-8編碼

#格式  (將值放到字串裡面)

#以%來使用舊方式  - string % data
# 整數
'%s' % 42 # 字串
'%d' % 42 # 十進位整數
'%x' % 42 # 十六進位整數
'%o' % 42 # 八進位整數

# 浮點數
'%s' % 7.03
'%f' % 7.03 # 十進位浮點數
'%e' % 7.03 # 指數浮點數
'%g' % 7.03 # 十進位或指數浮點數

# 整數與常值 %
'%d%%' % 100

#字串與整數混合
actor = 'Hugh'
cat = 'Peng'
weight = 72
"the actor is %s" % actor
"the actor %s's cat %s's weight is %s" % (actor, cat, weight)

# 可以在 % 與類型指定符之間加入其他的值指定, 最小與最大寬度, 對齊與字串填充
n = 72
f = 7.03
s = 'string'
'%d %f %s' % (n, f, s)

# 將最小欄位寬度設為10個字元,並靠右對齊,用空格來填充左邊
'%10d %10f %10s' % (n,f,s)
# 使用預設寬度 靠左對齊
'%-10d %-10f %-10s' % (n,f,s)
# 相同的欄位寬度,最大字元寬度為4,靠右對齊
'%10.4d %10.4f %10.4s' % (n,f,s) #會截斷字串,並將浮點數限制為小數點後4位
# 靠右對齊
'%.4d %.4f %.4s' % (n,f,s)
# 由引數取得欄位寬度,而不是寫死
'%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s)


#使用{}與format的新格式化方式
#簡易方法
n = 72
f = 7.03
s = 'string'
'{} {} {}'.format(n,f,s)
'{0} {1} {2}'.format(f,s,n) #可以指定順序
'{1} {1} {2}'.format(n,f,s)
# 可以在引數使用字典或具名引數,在指定符加入名稱
'{n} {f} {s}'.format(n=72, f=7.03, s='string')

d = {'n': 42, 'f' : 7.03, 's' : 'string'}
'{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')
'{0[f]} {0[s]} {1} {0[s]}'.format(d, 'other')
#轉換類型: 舊方式 %+指定符 / 新方式: : + 指定符
'{0:d} {1:f} {2:s}'.format(n,f,s)
#使用具名引數
'{s:s} {f:f} {n:d}'.format(n = 72, f = 7.04, s = 'str')
#最小欄寬、最大字元寬、對齊方式

'{0:10d} {1:10f} {2:10s}'.format(n,f,s) #最小欄寬10,靠右對齊
'{0:>10d} {1:>10f} {2:>s}'.format(n,f,s) #用>字元讓靠右對齊更明顯
'{0:<10d} {1:<10f} {2:<10s}'.format(n,f,s) # 靠左對齊
'{0:^10d} {1:^10f} {2:^10s}'.format(n,f,s) # 置中對齊

# 與舊方法不同,無法在整數中使用"精度值"(小數點後位數)
'{0:>10.4d} {1:>10.4f} {2:>10.4s}'.format(n,f,s)
#填充字元 (使用空格以外的字元填充輸出欄位)
'{0:!^20s}'.format('SALES') #將字元放在:後面 (總共20字元)

# 以正規表達式匹配
# 定義想要匹配的字串模式 + 要匹配的對象字串
result = re.match('You', 'ABCDE')
                # 模式    # 來源
# 可以先編譯模式以提升匹配速度
youpattern = re.compile('You')
result = youpattern.match('ABCDE')
# function	功能
# re.match( pattern, source )	查看字串是否以規定的規則開頭
# re.search( pattern, source )	會返回第一次成功的匹配值 (如果有成功)
# re.findall( pattern, source)	會返回所有成功且不重複的匹配值 (如果有成功)
# re.split( pattern, source )	會根據 規則 將 字串 切分成若干段，返回由這些片段組成的list
# re.sub( pattern, replacement, source )	還需一個額外的參數 replacement，它會把 字串 中所有匹配規則的字串 替換成 replacement
# 使用match()取出匹配項目
import re
source = 'Young boy'
m = re.match('You', source) # match()會從來源開頭進行
if m:
    print(m.group())
m = re.match('^Y', source)
if m:
    print(m.group())
m = re.match('boy', source)
if m:
    print(m.group())  # match()只會在'模式'位於'來源'開頭才生效
m = re.search('boy', source) # search()則都會生效
if m:
    print(m.group())
m = re.search('.*boy', source) # '.'代表任何單一字元
if m:                          # '*'代表任何在他前面的東西,不論數量
    print(m.group())           # '.*' 任何數量的字元(包含零個)

# 使用findall()匹配全部
source = 'mmmmmmmmnnnnnnnnnnddd'
m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('d.', source) # 'd'的後面有什麼字元?
m # 最後一個d不會被匹配
m = re.findall('d.?', source) # 使用'?'表示'd'後面的字元不是必要的
m

# 使用spilt()來分割
m = re.split('n', source)
m

#使用 sub()來替換匹配項目
m = re.sub('n', '?', source)
m

# 模式:特殊字元

# 特殊字元	功能
# .	        代表任意除 \n 外的字元
# *	        表示任意多個字元(包括 0 個)
# ?	        表示可選字元( 0 個或 1 個)
# \d	    一個數字字元。等價於[0-9]
# \D	    一個非數字字元。等價於[^0-9]
# \w	    一個 字母 或 數字 包括底線字元。等價於[A-Za-z0-9_]
# \W	    一個 非字母 非數字 非底線字元。等價於[^A-Za-z0-9_]
# \s	    空白字元。等價於[ \f\n\r\t\v]
# \S	    非空白字元。等價於[^ \f\n\r\t\v]
# \b	    單詞邊界（一個 \w 與 \W 之間的範圍，順序可逆）
# \B	    非單詞邊界

import string
printable = string.printable
len(printable)
printable[:50]
printable[50:]

re.findall('\d', printable) # 找出printable裡的數字
re.findall('\w', printable) # 找出英文數字還有底線
re.findall('\s', printable) # 找出空白字元

# 正規表達式不僅限於ASCII, \d 會匹配任何Unicode稱為數字的東西
X = 'abc' + '+-*' + '\uA78C' + '\u080D'
re.findall('\W', X)

# 模式:使用指定符
source = '''I wish I may, I wish I might
...have a dish of fish tonight.'''

re.findall('wish', source)
re.findall('wish|fish', source)
re.findall('^wish', source)
re.findall('^I wish', source)
re.findall('wish$', source)
re.findall('fish tonight.$', source)

# ^與$字元稱為 '錨點'(anchor)
# ^ -> 將搜尋動作錨定在搜尋字串的開頭
# $ ->　　　　　 ＂＂　　　　　　結尾
# .$ -> 匹配任何在行尾的字元(包括句號)
re.findall('fish tonight\.$', source) # 使用跳脫符號，表示\.為一個點而不是萬用字元
re.findall('[wf]ish', source) # 用ish來找w or f
re.findall('[wsh]+', source) # 找w、s、h組合出來的字串　(越多越好)
re.findall('ght\W', source) # 找ght開頭，後面接著非字母 非數字 非底線字元
re.findall('I (?=wish)', source) # 找I開頭，後面是wish，但只返回前面
re.findall('(?<=I) wish', source) # 找前面開頭是I的wish，只返回後面
re.findall('\bfish', source) # 避免使用Python的原始字串而用到轉義字元 (\b被當作是跳脫字元返回符號)
re.findall(r'\bfish', source) # 採用r來宣告這是一個原始的字串,停用轉義字元

# 模式:指定匹配輸出
m = re.search(r'(. dish\b).*(\bfish)',source) # 將模式放到括號內，匹配項會被存到自己的群組內
m.group()
m.groups() # 用 m.groups() 來取得他們的tuple

# (?P<name> expr) -> 匹配expr，將匹配項存在name群組內
m = re.search(r'(?P<Dish>. dish\b).*(?P<Fish>\bfish)', source) # 可以透過<name>設定名稱
m.group()
m.groups()
m.group('Dish')
m.group('Fish')

# 二進位資料
# byte -> 不可變 / bytearray -> 可變
blist = [1,2,3,255]
the_bytes = bytes(blist)
the_bytes
the_bytes_array = bytearray(blist)
the_bytes_array

the_bytes[1] = 127 # 無法更改byte變數
the_bytes_array[1] = 127 # bytesarray可以更改變數
the_bytes_array

the_bytes = bytes(range(0,256))
the_bytes
the_bytes_array = bytearray(range(0,256))  # 都會建立256個元素，值從0~255
the_bytes_array

# 用struct來轉換二進位資料
# 編寫程式，以擷取圖像的寬與高
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n' #有效的png檔的開頭
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'  # PNG檔前30個byte (width: 16-20個byte/height 21-24個byte)
if data[:8] == valid_png_header:  #>LL為格式化字串，指示unpack()解譯byte輸入序列
    width, height = struct.unpack('>LL', data[16:24])  # 每個L代表一個4-byte的長整數(以big-endian格式儲存)
    print('Valid PNG, width', width, 'height', height )
else:
    print('Not a valid PNG')
data[16:20]
data[20:24]

# Big-endian會將最重要的byte放在最左邊. 由於寬長皆小於255,因此會放到序列的最後一個byte
0x9a
0x8d

# 反過來將資料轉換成byte - struct pack()
import struct
struct.pack('>L', 154)
struct.pack('>L', 141)

# 格式指定符在endian字元後面, 可在指定符前面加上數字以表示數量
struct.unpack('>2L', data[16:24])
struct.unpack('>16x2L6x', data) # 可以使用x指定符來跳過
# 1.使用big-endian整數格式 (>)
# 2.跳過16個bytes (16x)
# 3.讀取8個bytes-兩個不帶符號的長整數 (2L)
# 4.跳過最後的6個bytes (6x)