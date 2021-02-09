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
