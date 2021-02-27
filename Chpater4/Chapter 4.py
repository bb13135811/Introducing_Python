#使用\延續多行
alphabet = ''
alphabet += 'abc'
alphabet += 'def'
alphabet += 'ghi'
print(alphabet)
#運算式無法跨越多行
alphabet = 'abc' + \
    'def' +\
    'ghi'
print(alphabet)

alphabet = 'abc' + 'def' + 'ghi'
print(alphabet)

#使用if,elif,else
dis = True
if dis:
    print("Run")
else:
    print("Don't Worry")

furry = True
small = True
if furry:
    if small:
        print("It's a Cat")
    else:
        print("Not a cat")
else:
    if small:
        print("It's a skink")
    else:
        print("A Human")

#三個以上測試值,使用if,elif,else
color = "puce"
if color == "red":
    print("Tomato")
elif color == "green":
    print("Green pepper")
elif color == "purple":
    print("Can't Eat")
else:
    print("No color")
#兩個等號用來測試“相等與否”,一個等號用來指派變數

list = []
if list:
    print("There's sth")
else:
    print("Empty")

#while迴圈
count = 1
while count <= 5:
    print(count)
    count += 1

#用breakf取消
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

#用continue來跳過
while True:
    value = input("Enter an integer, please: ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 1:
        print(number, "squared is", number * number)
    else:
        continue

#使用else來檢查中斷
numbers = [2, 3, 4, 6]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Even number", number)
    position += 1
else:
    print("No even number")

#用for來迭代
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

for rabbit in rabbits:
    print(rabbit)
#迭代字典 會回傳鍵
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation:
    print(card)

#如要回傳值必須用value()
for value in accusation.values():
    print(value)

#如要用tuple回傳鍵與值,用item()
for item in accusation.items():
    print(item)

#對tuple賦值，鍵指派給cards,值指派給contents
for cards, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

#break會跳出迴圈,continue則會跳到下次迭代

#使用else來檢查中斷
cheeses = []
for cheese in cheeses:
    print('There are some', cheese)
    break
else:
    print('no cheese')

cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('There are some', 'cheese')
    break
if not found_one:
    print("No cheese")

#用zip來迭代多個序列 （並行）
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'black tea', 'green tea']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ":drink " , drink, "- eat", fruit, "- enjoy" , dessert)

#使用zip查看多個序列,並作成tuple
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dic(zip(english, french)))

#用range產生數字序列
for x in range(0,3):
    print(x)
for x in range(2, -1, -1):
    print(x)
list(range(2,-1,-1))
list(range(0, 11, 2))

#生成式
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for i in range(1,6):
    number_list.append(i)
print(number_list)

number_list = list(range(1,6))
print(number_list)
#串列生成式
#[運算式 for 項目 in 可迭代項目]
number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)
#串列生成式可容納條件運算式
#[運算式 for 項目 in 可迭代項目 if 條件式]
#1~5的奇數
o_list = [odd for odd in range(1,6) if odd % 2 == 1]
print(o_list)

o_list = []
for number in range(1,6):
    if number % 2 == 1:
        o_list.append(number)
print(o_list)

#使用兩組以上的for... 舊式嵌套迴圈
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)
#使用生成式,指派給變數cells
rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

#字典生成式
#{鍵運算式：值運算式 for 運算式 in 可迭代項目}
#同樣可以使用if與多個for
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

from collections import Counter, defaultdict
letter_count = Counter(word)
print(letter_count)
#集合生成式
#{運算式 for 運算式 in 可迭代項目}
a_set = {number for number in range(1,6) if number % 2 ==1}
print(a_set)

#產生器生成式
number_thing = (number for number in range(1,6))
type(number_thing)
for number in number_thing:
    print(number)
number_thing = (number for number in range(1,6))
num_list = list(number_thing)
print(num_list)
#產生器只能執行一次
number_list = list(number_thing)
print(number_list)

#函式
#定義 + 呼叫
def a():
    print("A")
a()

def echo(anyhing):
    return anyhing + ' ' + anyhing
print(echo('AAA'))

def commentary(color):
    if color == 'red':
        return "It's red."
    elif color == 'blue':
        return "It's blue."
    elif color == 'green':
        return "It's green."
    else:
        return "There's no color" +  ' ' + color + "."
comment = commentary('Black')
print(comment)

#位置引數
def menu(wine, entree, dessert):
    return{'wine':wine, 'entree':entree, 'dessert':dessert}
menu('chardonnay', 'chicken', 'cake')
#必須記得位置
menu('beef','bagel', 'bordeaux')

#關鍵字引數
#使用引數的對應參數名稱來指定引數
menu(entree ='beef', dessert ='bagel', wine ='bordeaux')
menu('frontenac', dessert= 'flan', entree= 'fish')

#指定預設參數值
def menu(wine, entree, dessert='pudding'):
    return {'wine' : wine,'entree' : entree, 'dessert': dessert }
menu('chardonnay', 'chicken')
#假如提供引數將使用它,而不是預設值
menu('dunkelfelder', 'duck', 'doughnut' )

#函式呼叫保有前一項目
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b') #應該只有b
#修正
def work(arg):
    result =[]
    result.append(arg)
    return result
work('a')
work('b')
#說明函式是否第一次被呼叫
def nobuggy(arg, result = None):
    if result is None:
        result =[]
    result.append(arg)
    print(result)
nobuggy('a')
nobuggy('b')

#用*來收集位置引數
#星號會將可變數量的潛在引數群組化,變成一個參數值的tuple
def print_args(*args):
    print('Positional argument tuple:', args)
print_args()
print_args(3,2,1, 'wait!', '....')
#可把＊放在位置引述最後面,抓取剩下的引數
def print_more(required_1, required_2, *args):
    print('Need the first one:', required_1)
    print('The second one:', required_2)
    print('All the rest are:', *args)
print_more('workout', 'swimming', 'surfing', 'climbing', 'running')
#在使用*時,不一定要呼叫tuple參數args
#用**來收集關鍵字引數
#將關鍵字引數群組化,變成字典,引數名稱為鍵,值為對應字典值
def print_kwargs(**kwargs):
    print('keyword argument:', kwargs)
print_kwargs(wine = 'god father', entree = 'shot', dessert = 'french fries')

def __kwargs(**kwargs):
    print('the profile:', kwargs)
__kwargs( name = 'Hugh', age = 24 , sex = 'Male')
#如共同使用 **kwargs & *args 順序：args > kwargs
def prac(first_one, *args, **kwargs):
    print('try this one:', first_one)
    print('try the second one:', args)
    print('the rest are:', kwargs)
prac('A', 'C', 'D', 'E', B = 3, the_last_one = 2)

#文件字串
#將文件指派給函式的定義式
#在函式內文的開頭加入一個字串
def echo(anything):
    'echo return its input argument'
    return anything
echo('aaa')

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    the operation is:
        1.Check whether the *second *argument is true.
        2.If it is, print the *first *argument.
    '''
    if check:
        print(thing)
print_if_true('a', '')
#如要印出文件字串,可使用help()

help(echo)
echo(anything)

def answer():
    print(42)
def run_something(func):
    func()
run_something(answer)

def add_args(arg1, arg2):
    print(arg1 + arg2)
type(add_args)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args, 5, 9)
#與*args及**kwargs結合
def sum_args(*args):
    return sum(args)
def run_with_positonal_args(func, *args):
    return func(*args)
run_with_positonal_args(sum_args, 1, 2, 3, 4, 5)

#內部函式
#在函式裡定義函式
def outer(a,b):
    def inner(c,d):
        return c + d
    return a + b
outer(1, 3)
def outer(*args):
    def inner(**kwargs):
        return sum(kwargs)
    return sum(args)
outer(5, 8, 5)
#可在函式內執行多次複雜的工作
def knights(saying):
    def inner(quote):
        return "We are knights who say: '%s' " %quote
    return inner(saying)
knights('Ni!')

#Closure
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s' " % saying
    return inner2
a = knights2('AAAAA')
b = knights2('BBBBB')
type(a)
type(b)
a
b
a()
b()

#匿名函式：lambda()函式
#lambda為以一行陳述式來表示的匿名函式
def edit_story(words, func):
    for word in words:
        print(func(word))
text = ['aaaa', 'bbbb', 'ccccc', 'ddddd']
def Cap(word):
    return word.capitalize() + '!'
edit_story(text, Cap)

edit_story(text, lambda word: word.capitalize() + '!')
#lambda最常使用情況---> 需定義許多小型函式且要記得如何稱呼時

#產生器(Generator)
#保存的僅是算法,不會佔用空間
def my_range(first=0, last=10, step=2):
    number = first
    while number < last:
        yield number
        number += step
ranger = my_range(1,10)
#迭代產生器物件
for i in ranger:
    print(list(ranger))

#裝飾器
#不修改原始碼,加入除錯的陳述式
def document_it(func):
    def new_function(*args, **kwargs):  #定義裝飾器
        print('Running Function:', func.__name__)  #印出函式的名稱及引數的值
        print('Positional Function:', args)
        print('Keyword Argument:', kwargs)
        result = func(*args, **kwargs)  #用引數來執行函式
        print('Result:', result)  #印出結果
        return result
    return new_function #回傳修改後的函式
#手動應用裝飾器:
def add_ints(a, b):
    return a + b
new_add_ints = document_it(add_ints) #手動應用裝飾器
new_add_ints(5, 8)
#在函式前添加＠decorator_name取代手動指派
@document_it
def add_ints(a, b):
    return a + b
add_ints(3, 8)
#同一個函式可以有兩個以上裝飾器
#先編寫另一個裝飾器
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function
@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(5, 6)

@square_it
@document_it
def add_ints(a, b):
    return a + b
add_ints(5, 6)

#命名空間與範圍
#在命名空間內的變數都是“全域變數” (Global variable) - (function外指定的變數)
#                            (local variable) - (function內指定的變數)
#可在函式裡取得全域變數的值但無法修改
animal = 'doggy'
def print_golbal():
    print('inside print_global:', animal)
print('at the top level:', animal)
print_golbal()
#如要在函式中取得值並修改,會出現錯誤
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'cat' #不能對全域變數修改
    print('after change:', animal)
change_and_print_global()
#假如修改了,也會修改另一個也叫animal的變數,但是在函式裡面
def change_local():
    animal = 'bat' #變數位置在函式區域命名空間內
    print('inside change_local:', animal, id(animal))
change_local()
animal
id(animal)
#如要存取全域變數,須明確使用global關鍵字
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
animal
change_and_print_global()
animal
#如不使用global,會使用函式內的區域變數(在函式結束時會消失)
#locals() - 回傳區域字典內容
#globals() - 回傳全域字典內容
animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())
animal
change_local()
print('globals:', globals()['animal'])

#在名稱中使用 ＿ 與 ＿
def amazing():
    ("This is the document of function'amazing'")
    print('The name of this function is:', amazing.__name__)
    print('The words in this function include:', amazing.__doc__)
amazing()

#使用try與except來處理錯誤
short_list = [1, 2, 3]
position = 5
short_list[position]
#以try來包住程式,以except處理錯誤
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and',len(short_list)-1, 'but got',
          position)
#如想得知該類型以外的例外細節,可使用以下格式
# except exceptiontype as name （在變數name中取得完整的例外物件)
short_list = [1, 2, 3]
while True:
    value = input('Position[q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as error:
        print('Bad Index:', position)
    except Exception as other:
        print('Something else broke:', other)

#自行製作例外
#製作一個稱為UppercaseException的例外
class UppercaseException(Exception):
    pass
words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)