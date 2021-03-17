# 1. 建立名為mystery的Unicode字串，指派'\U0001f4a9'值，印出mystery
mystery = '\U0001f4a9'
print(mystery)

# 2. 將mystery編碼至bytes變數pop_bytes，使用UTF-8印出pop_bytes
pop_bypes = mystery.encode('utf-8')
print(pop_types)

# 3. 使用UTF-8將pop1解碼成字串變數 pop_string / pop_string = mystery?
pop_string = pop_bypes.decode('utf-8')
print(pop_string)
print(mystery)
pop_string == mystery

# 4. 使用舊方式的格式化來編寫下列的詩,將字串放入
poem = '''My kitty cat likes %s, \
 My kitty cat likes %s, \
 My kitty cat fell on his %s, \
 And now thinks he's a %s.'''
print(poem % ('roast beef', 'ham', 'head', 'claim'))
args = ('roast beef', 'ham', 'head', 'claim')
print(poem % args)

# 5. 使用新格式來編寫信件,將下列字串存成letter
letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your{room}. 
Please note that it should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. 
We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
Thank you for your support.

Sincerely,
{spokesman}
{job_title},
'''

# 6. 製作一個名為response的字典,字典鍵的值為'salutation','name','product','verbed'(past tense verb),,'room','animals','amount'
# 'percent','spokesman', 'job_title' 用response的值印出letter
response = {
   'salutation':'Colonel',
    'name':'Hackenbush',
    'product':'duck blind',
    'verbed':'imploded',
    'room':'conservatory',
    'animals':'emus',
    'amount':'$1.38',
    'percent':'1',
    'spokesman':'Edgar Schmeltz',
    'job_title':'Licensed Podiatrist'
    }
print(letter.format(**response))

# 7.
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go 
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr.Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze

And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

# 8. 匯入re模組使用python的正規表達式,使用re.findall()印出所有c開頭的單字
import re
c = re.findall(r'\bc\w*', mammoth)

# 9. 尋找所有c開頭的四個字母單字
a = re.findall(r'\bc\w{3}\b', mammoth)
a

# 10. 尋找所有最後一個字母是r的單字
b = r'\b\w*r\b'
re.findall(b, mammoth)

# 10-1. 結尾是l的單字
c = r'\b\w*l\b' # \w不會抓取單引號
re.findall(c, mammoth)
c1 = r"\b[\w']*l\b" # 使用引號字元框住模式字串
re.findall(c1, mammoth)

# 11. 尋找具有連續三個母音的單字
d = r'\b\w*[aeiou]{3}[^aeiou]\w*\b' # 會匹配到包含其他字元的字串
re.findall(d, mammoth)
d1 = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b' # 搜尋不到三母音結尾的字串
re.findall(d1, mammoth)
d2 = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b' # 需新增母音後字元數量不限(包含零)
re.findall(d2, mammoth)

# 12. 使用unhexlify將十六進位字串轉換成bytes變數gif
import binascii
gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9' +\
'0401000000002c000000000100010000020144003b')
print(gif)
len(gif)

# 13. gif裡面的byte定義一張一個像素的透明GIF檔案,有效的GIF會從GIF89a開始, gif符合嗎
gif[:6] == b'GIF89a'

# 14. GIF的像素寬度是16位元的little-endian整數,從byte位移植6開始,高度的大小一樣,從位移植8開始
#     取出並印出gif的這些值,都是1嗎
import struct
width, height = struct.unpack('<2H', gif[6:10])
width, height == 1
