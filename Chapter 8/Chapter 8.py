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
# 檔案會使用不同的行尾字元
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





# YAML
# 與JSON很像，有鍵與值，但可處理更多資料類型

import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.safe_load(text) # lead()將YAML字串轉換成python資料
data['details']             # 如果要匯入不信任的YAML，使用safe_load()來代替load()
len(data['poems'])

# 假如資料超過一層，可使用字典/串列/字典來參考，取得第二首詩的標題
data['poems'][1]['title']


# configparser解析器
import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
cfg
cfg['french']
cfg['french']['greeting']
cfg['files']['bin']


# 用pickle來序列化(serializing)
# pickle模組可儲存及還原特殊二進位格式物件
import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
now1
now2

# 可在自己的類別及物件使用pickle
import pickle
class Tiny():
    def __str__(self):
        return "tiny"
obj1 = Tiny()
obj1
str(obj1)
pickled = pickle.dumps(obj1) # dumps() 序列化(將資料結構或物件狀態轉換成可取用格式)
pickled
obj2 = pickle.loads(pickled) # loads() 反序列化
obj2


# SQL
# 陳述式分兩大種
# DDL (資料定義語言)
# DML (資料處理語言)

# DB-API
# connect() - 連結到資料庫，可傳入帳號、密碼、伺服器地址等引數
# cursor() - 建立cursor物件來處理查詢指令
# execute() & executemany() - 對資料庫執行一或多個SQL指令
# fetchone()、fetchmany()、fetchall() - 取得execute的結果


# SQLite
import sqlite3
conn = sqlite3.connect('enterprise.db') # 製作稱為'enterprise.db的資料庫
curs = conn.cursor() # cursor() - 建立cursor物件來處理查詢指令
curs.execute('''CREATE TABLE zoo 
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)''') # execute() & executemany() - 對資料庫執行一或多個SQL指令
# critter - 變數長度字串，為主鍵
# count - 該動物目前整數數量
# damages - 動物造成損失金額
# 加入動物
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
# 使用“佔位符” - 較安全的資料插入方式
ins = 'INSERT INTO zoo(critter, count, damages) VALUES(?,?,?)'
curs.execute(ins, ('weasel', 1, 2000.0))

curs.execute('SELECT * FROM zoo') # 將所有動物取出
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * FROM ZOO ORDER BY count')
curs.fetchall()

curs.execute('SELECT * FROM ZOO ORDER BY count DESC') # 以降冪排序
curs.fetchall()

curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')
curs.fetchall()
# 必須在完成工作時關閉開發連結與cursor
curs.close()
conn.close()


import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)''')
ins = 'INSERT INTO zoo(critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)
rows = conn.execute('SELECT * FROM zoo')
print(rows) # rows在SQLAlchemy不是串列，而是ResultProxy，無法被印出來
for row in rows:
    print(row)


# SQL Expression Language
import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
# 為定義zoo資料表，使用Expression Language取代SQL
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
    sa.Column('critter', sa.String, primary_key=True),
    sa.Column('count', sa.Integer),
    sa.Column('damages', sa.Float)
    )
meta.create_all(conn)
# 使用Expression Language函式來插入資料
conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
conn.execute(zoo.insert(('duck', 10, 0)))
result = conn.execute(zoo.select()) # 選擇資料表內zoo物件的所有東西
rows = result.fetchall()
print(rows)

# 物件-關係對應器
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)
Base.metadata.create_all(conn) #建立資料表與資料庫
#建立Python物件插入資料
first = Zoo('duck', 5, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
first
# 建立session與資料庫互動
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn) # 將conn綁定
session = Session()
# 將之前三個物件寫入資料庫
session.add(first) # add() - 加入一個物件
session.add_all([second, third]) # add_all() - 加入一個串列
session.commit()
rows = conn.execute('''SELECT * FROM zoo''')
for row in rows:
    print(row)


# NOSQL 資料存放區

# dbm (鍵-值存放空間)
# 'r'代表讀取，'w'代表寫入，'c'代表兩者，假如不存在會建立檔案
import dbm
db = dbm.open('definition', 'c')
# 建立鍵-值對，將值指派給鍵
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'
len(db)
db['mustard']
db.close()
db = dbm.open('definition', 'r')
db['mustard']


# Redis (ㄧ種資料結構伺服器)

# 字串
#連結到某個Redis伺服器的主機(預設為localhost)、連接埠(預設為6379)
import redis
conn = redis.Redis()
redis.Redis('localhost')
redis.Redis('localhost', 6379) # 兩者會產生相同的結果
#列出所有鍵
conn.keys('*')
conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', '101.5')
# 以鍵取回值
conn.get('secret')
conn.get('carats')
conn.get('fever')
# 當鍵不存在時，setnx()才會設定新值
conn.setnx('secret', 'the new one') #已存在，則出現False
conn.get('secret') #還是會回傳舊值
conn.getset('secret', 'the new one') #先回傳舊值，接著設為新值
conn.get('secret') # 新值設定成功
# 使用getrange()取得子字串
conn.getrange('secret', -3, -1) # 0=開始，-1=結束
# 使用setrange()替換一個子字串
conn.setrange('secret', 0, 'THE') # 使用以零開始的位移
conn.get('secret')

#使用mset()一次設定多個鍵
conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
# 使用mget一次取得多個值
conn.mget(['fever', 'carats'])
conn.mget(['pie', 'cordial'])

#使用delete()刪除鍵
conn.delete('fever')
conn.get('fever')

#使用incr()或incrbyfloat()來遞增，decr()遞減
conn.incr('carats')
conn.incr('carats', 100)
conn.decr('carats', 50)
conn.set('fever', '101.5')
conn.incrbyfloat('fever')
conn.incrbyfloat('fever', 0.05)
conn.incrbyfloat('fever', -2.5) # 沒有decrbyfloat()，因此用負數遞增

# 串列
# Redis串列只能存放字串，首次插入便會建立串列
# 使用lpush()在開頭插入
conn.lpush('zoo', 'bear')
conn.lpush('zoo', 'alligator', 'duck')

# 使用linsert()在一個值之前/之後插入
conn.linsert('zoo', 'before', 'bear', 'beaver')
conn.linsert('zoo', 'after', 'bear', 'cassowary')
# 使用lset()在某位移植執行插入(串列必須已存在)
conn.lset('zoo', 2, 'marmoset')
# 使用rpush()在結尾插入
conn.rpush('zoo', 'yak')
# 使用lindex()取得某位移的值
conn.lindex('zoo', 3)
# 使用lrange()取得某位移範圍內的值 (0~-1可取出全部值)
conn.lrange('zoo', 0, 2)
# 使用ltrim()修剪串列，只留下位移範圍內的值
conn.ltrim('zoo', 1, 4)
# 使用lrange()取得某位移範圍內的值 (0~-1可取出全部值)
conn.lrange('zoo', 0, -1)


# 雜湊
# 與Python字典很像，但只能容納字串，因此只能往下一層，無法製作深層嵌套結構

# 使用 hmset() 設定雜湊song的do與re
conn.hmset('song', {'do': 'a dear', 're': 'about a dear'})
# 使用 hset() 設定雜湊的單一欄位值
conn.hset('song', 'mi', 'a note to follow re')
# 使用 hget() 取得一個欄位的值
conn.hget('song', 'mi')
# 使用 hmget() 取得多個欄位的值
conn.hmget('song', 're', 'do')
# 使用 hkeys() 取得雜湊所有欄位的鍵
conn.hkeys('song')
# 使用 hvals() 取得所有欄位的值
conn.hvals('song')
# 使用 hlen()取得欄位數量
conn.hlen('song')
# 使用 hgetall()取得所有欄位鍵與值
conn.hgetall('song')
# 當欄位的鍵不存在，使用 hsetnx()設定欄位
conn.hsetnx('song', 'fa', 'a new note')
conn.hgetall('song')


# 集合

conn.sadd('zoo', 'duck', 'goat', 'turkey')# 將一或多個值加至集合
conn.scard('zoo') # 取得集合值的數量
conn.smembers('zoo') # 取得集合所有值
conn.srem('zoo', 'turkey') # 移除集合的值
conn.sadd('better_zoo', 'tiger', 'wolf', 'duck') # 製作第二組集合
conn.sinter('zoo', 'better_zoo') # 查看交集
conn.sinterstore('wolf_zoo','zoo', 'better_zoo') # 將交集結果存入另一組集合
conn.smembers('wolf_zoo')
conn.sunion('zoo', 'better_zoo') # 取得聯集
conn.sunionstore('f_zoo', 'zoo', 'better_zoo') # 將聯集結果存入另一組集合
conn.smembers('f_zoo')
conn.sdiff('zoo', 'better_zoo') # 取得差集
conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo') # 將差集結果存入
conn.smembers('zoo_sale')


# 有序集合 ( sorted set )
# zset是Redis最多功能的類型之一，每個值都有相關的浮點分數(score)
# 可以用值或分數存取每一個項目
#用途：
    #排行榜
    #輔助索引
    #時間序列，使用時戳來作為分數
import time
now = time.time()
now

conn.zadd("logins", {'smeagol': now})
conn.zadd("logins", {'sauron': now + (5*60)})
conn.zadd("logins", {'bilbo': now + (2*60*60)})
conn.zadd("logins", {'treebeard': now + (24 * 60 * 60)})

conn.zrank('logins', 'bilbo')
conn.zscore("logins", 'bilbo')
conn.zrange('logins', 0, -1)
conn.zrange('logins', 0, -1, withscores=True)


# 位元
# 先建立每天的位元集
days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212
# 假設在第一天，有兩位使用者來訪
conn.setbit(days[0], big_spender, 1)
conn.setbit(days[0], tire_kicker, 1)
# 隔天其中一位回訪
conn.setbit(days[1], big_spender, 1)
# 再隔一天，其中一位回訪第二次，並加入一位新使用者
conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)
# 取得這幾天的訪客數量
for day in days:
    print(conn.bitcount(day))
# 是否有特定的使用者在特定日期造訪
conn.getbit(days[1], tire_kicker)
# 每天有多少使用者造訪
conn.bitop('and', 'everyday', *days)
    # bitop() -> BITOP(operation, destkey, key [key ...])
    # 將一或多個key進行位元操作，並將結果保存到destkey上
conn.bitcount('everyday')
conn.getbit('everyday', big_spender)
conn.bitop('or', 'alldays', *days)
conn.bitcount('alldays') # 這三天裡，有幾位使用者曾造訪


# 快取與逾期
# 所有Redis鍵都有存活時間，可使用expire()函式指示要將鍵保存多久
import time
key = 'now see it'
conn.set(key, 'not for long')
conn.expire(key, 30)
conn.ttl(key)
conn.get(key)
time.sleep(10)
conn.get(key)
# expireat()指令會在給定的epoch時間讓一個鍵逾期
# 讓鍵逾期可讓快取維持在最新狀態、限制登入session