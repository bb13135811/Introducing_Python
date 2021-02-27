5.1
#建立名為zoo.py的檔案.在裡面定義一個名為hours()的函式,用來印出字串'Open 9-5 daily'
#使用互動式解譯器匯入zoo模組並呼叫hours()函式
import zoo
zoo.hours()

5.2
#在解譯器中將zoo模組匯入為menagerie並呼叫函式
import zoo as menagerie
menagerie.hours()

5.3
#直接從zoo匯入hours()函式並呼叫
from zoo import hours
hours()

5.4
#將hours匯入為info並呼叫
from zoo import hours as info
info()

5.5
#使用鍵/值對 'a':1, 'b':2, 'c':3 製作一個名為plain的字典並印出
plain = {
    'a':1,
    'b':2,
    'c':3
    }
print(plain)

5.6
#製作名為fancy的OrderDict並印出
from collections import OrderedDict
fancy = OrderedDict(plain)
print(fancy)

5.7
#製作名為 dict_of_lists 的defaultdict並傳入引數列串列
#製作串列dict_of_lists['a']並將'something for a'指派給他,印出dict_of_lists['a]
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
