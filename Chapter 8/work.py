# 1. 將字串'This is a test of the emergency text system'指派給變數test1，並將test1寫到test.text檔
test1 = 'This is a test of the emergency text system'
len(test1)
with open('test.txt', 'wt') as file:
    file.write(test1)
file.close()

# 2. 開啟檔案test.text，並將內容讀至字串text2，test1會與test2一樣嗎？
with open('test.txt', 'rt') as file:
    text2 = file.read()
    print(text2)
test1 == text2

# 3. 將這幾行文字存到test.csv檔，如果欄位是以逗號分隔，當裡面有逗號時，必須用引號框住該欄位
text = '''author, book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''
with open('test.csv', 'wt') as file:
    file.write(text)
len(text)

# 4. 使用csv模組與DictReader()將test.csv讀到變數books，印出books的值
import csv
with open('test.csv', 'rt') as file:
    books = csv.DictReader(file)
    book = [book for book in books]
    print(book)

# 5. 使用這幾行建立一個名為books.csv的CSV檔
word = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mi.ville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''
with open('books.csv', 'wt') as file:
    file.write(word)

# 6. 使用sqlite3模組建立名為books.db的SQLite資料庫，與一個名為books的資料表，
#    欄位： title、author、year
import csv
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
        (title TEXT,
         author TEXT,
         year INT)''')
conn.commit()
curs.close()

# 7. 讀取books.csv，將資料插入book資料表
import csv
import sqlite3
ins_str = '''INSERT INTO books VALUES(?, ?, ?)'''
with open('books.csv', 'rt') as file:
    books = csv.DictReader(file)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))
conn.commit()

# 8. 照字母順序選取並印出books資料表的title欄位
sql = '''SELECT title FROM books ORDER BY title ASC'''
for row in curs.execute(sql):
    print(row)
# 假如只想印出值，不印出括號和逗號
for row in curs.execute(sql):
    print(row[0])
# 忽略標題開頭的'The'
sql = '''SELECT title FROM books ORDER BY 
case when (title like "The %") then substr(title, 5) else title end'''
for row in curs.execute(sql):
    print(row[0])

# 9. 照出版物順序來選取並印出books資料表所有欄位
sql = '''SELECT * FROM books ORDER BY year '''
for row in curs.execute(sql):
    print(row)
# 要印出每列所有欄位，需用逗號和空格來分隔
for row in curs.execute(sql):
    print(*row, sep=', ')

# 10. 使用sqlalchemy模組連結8.6的資料庫books.db，如8.8，照字母順序選取並印出資料表的title欄位
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = '''SELECT title FROM books ORDER BY title ASC'''
rows = conn.execute(sql)
for row in rows:
    print(row)

# 11. 安裝Redis伺服器與Python redis程式庫，建立名為test的Redis雜湊
#     裡面有欄位count(1)與name('Fester Bestertester')，印出test的所有欄位
import redis
conn = redis.Redis()
conn.hmset('test', {'count':1, 'name':'Fester Bestertester'})
conn.hmget('test', 'count', 'name')
conn.hgetall('test')

# 12. 遞增test的count欄位，並將它印出
conn.hincrby('test', 'count', 3)
conn.hget('test', 'count')