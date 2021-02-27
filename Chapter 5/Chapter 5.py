#用其他名稱匯入模組
#如有其他相同名稱模組,可使用別名
import report as wr
description = wr.get_description()
print("Today's weather is:", description)

#只匯入模組內想要的東西
#可以只匯入模組中一或多個部分,可保留原本名稱或是使用別名
from report import get_description
description = get_description()
print("Today's weather:", description)
#用do_it來匯入
from report import get_description as do_it
description = do_it()
print("Today's weather is:", description)

#模組搜尋路徑
import sys
for place in sys.path:
    print(place)

#用setdefault()與defaultdict()處理遺漏的鍵
#假如鍵有遺漏,setdefault()會指派給字典
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

Carbon = periodic_table.setdefault('Carbon', 12)
Carbon
periodic_table #鍵沒有在字典裡,會使用新值
#假如指派不同值給已存在的鍵,會回傳原始值
helium = periodic_table.setdefault('Helium', 999)
helium
periodic_table

#defaultdict()會在字典被建立時,為任何新鍵指定預設值
from collections import defaultdict
periodic_table = defaultdict(int) #defaultdict的引數是函式
periodic_table['Hydrogen'] = 1
periodic_table['Lead'] #遺漏的鍵都會是整數,值為0
periodic_table

#傳入defaultdict的函式會回傳指派給遺漏的鍵的值
from collections import defaultdict
def no_idea():
    return '???'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'AboS'
bestiary['B'] = 'Bas'
bestiary['A']
bestiary['C']
#可使用int(), list(), dict()回傳這些類型的預設空白值
#假如省略引數,新鍵的初始值會被設為None

#可使用lambda在呼叫式中定義預設的函式
bestiary = defaultdict(lambda: '??')
bestiary['AAA']

#int可製作計數器
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
#假如使用一般的字典,會發出例外,因此需額外輸入條件
dict_counter = {}
for food in ['spam', 'spam', 'egg', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1
for food, count in dict_counter.items():
    print(food, count)

#用counter()來計算項目數量
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter
#most_common()以降冪回傳元素,或是指定數量時,回傳最前面count個元素
breakfast_counter.most_common()
breakfast_counter.most_common(1)

breakfast_counter
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter

breakfast_counter + lunch_counter
breakfast_counter - lunch_counter
lunch_counter - breakfast_counter
breakfast_counter & lunch_counter
breakfast_counter | lunch_counter

#使用鍵與OrderedDict()來排序
quotes = {
    'Moe': 'A wise guy',
    'Larry': 'Ow',
    'Curly': 'Nyuk',
    }
for stooge in quotes:
    print(stooge)
#OrderedDict()會記得加入鍵的順序,並按照順序回傳
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe','A wise guy'),
    ('Larry','Ow'),
    ('Curly','Nyuk')
    ])
for a in quotes:
    print(a)

#堆疊+序列 == deque
#想要從序列任何一端加入或刪除項目時
#popleft()會將deque最左邊的項目移除並回傳
#pop()會移除最右邊的並回傳
#同時從兩端開始往中間移動,只要兩端字元相符就會繼續pop,直到最中間為止
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
palindrome('a')
palindrome('abbbcc')
palindrome('racecar')

def a_palindrome(word):
    return word == word[::-1]
a_palindrome('word')
a_palindrome('radar')

#使用itertools來迭代程式結構
list = [('aa', 'bb'),('cc', 'dd')]
for a in list:
    print(a)

#chain()會逐一經過引數
import itertools
for item in itertools.chain([1,2], [3,4]):
    print(item)
#cycle是無限迭代器,循環經過引數
# import itertools
# for item in itertools.cycle([1,2,3,4]):
#  print(item)

#accumulate()會計算累計的值,預設為計算總和
import itertools
for item in itertools.accumulate([1,2,3,4]):
    print(item)

#可以在accumulate()的第二個引數提供函式,須提供兩個引數,會取代加法
import itertools
def multiply(a,b):
    return a * b
for item in itertools.accumulate([1,2,3,4], multiply):
    print(item)

#用pprint()印出好看結果
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy'),
    ('Larry', 'Ow'),
    ('Curly', 'Nyuk'),
    ])
pprint(quotes)
