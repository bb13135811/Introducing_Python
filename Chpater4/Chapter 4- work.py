4.1
#將7這個值指派給變數guess_me,並編寫條件測試式
#當guess_me < 7時印出字串'too low', < 7時印出字串'too high', = 7時印出'just right'
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

4.2
#將7指派給變數guess_me,將1指派給變數start. 寫一個while迴圈來比較start與guess_me.
#在迴圈的結尾遞增start
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start += 1

4.3
#使用for迴圈印出串列[3,2,1,0]
words = []
for word in range(3,-1,-1):
    print(word)

4.4
#使用一個串列生成式製作range(10)內的偶數的串列
list(range(0,11,2))
list = [int for int in range(10) if int % 2 ==0]
list

4.5
#使用字典生成式製作字典squares,使用range(10)回傳鍵,並以鍵的平方作為值
number = range(10)
square = {number: number * number for number in range(10)}
square

4.6
#使用一個集合生成式,以range(10)內的奇數製作odd集合
list = {number for number in range(10) if number % 2 ==1}
list

4.7
#使用產生器生成式回傳字串'Got'與range(10)內的一個數字,使用for迴圈來迭代
for number in range(10):
    print('Got', number)
for thing in ('Gor %s' %number for number in range(10)):
    print(thing)

4.8
def good():
    return ['Harry', 'Ron', 'Hermione']
good()

4.9
def get_odds():
    for number in range(1,10,2):
        yield number
for count, value in enumerate(get_odds(), 0):
    if count == 2:
        print('The Third Number Is:',value )
        break
        count += 1

4.10
def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_function

@test
def greeting():
    print('Greetings, Earthing')
greeting()

4.11
class OopsException(Exception):
    pass

raise OopsException()

try:
    raise OopsException
except OopsException:
    print('Caught an oops')

4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movie)

movies = {title:plot for title,plot in zip(titles, plots)}
movies

for title, plot in zip(titles, plots):
    print(title,':', plot)

list(zip(titles, plots))
