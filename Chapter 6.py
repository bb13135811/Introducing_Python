#用Class來定義類別
class Person():
    pass
Person()

someone = Person()
someone

class Person():
    def __init__(self):
        pass

class Person():
    def __init__(self, name):
        self.name = name
#傳遞一個字串給name參數,用Person類別建立一個物件
hunter = Person('Floyd')
print("the greatest hunter's name is:", hunter.name) #建立實際物件後要用hunter.name來參考
#查看Person類別定義
#在記憶體建立新物件
#呼叫該物件的__init__方法,傳遞新物件給self,傳遞另一個引數('Floyd')給name
#在物件儲存name的值
#回傳新物件
#將hunter名稱指派給物件

#繼承
class Car():
    pass
class Yugo(Car):
    pass
a_car = Car()
a_yugo = Yugo()

class Car():
    def exclaim(self):
        print("I'm a car")
class Yugo(Car):
    pass
a_car = Car()
a_yugo = Yugo()
a_car.exclaim()
a_yugo.exclaim()

#覆寫方法
#如何替換或覆寫父類別
#更改Yugo的exclaim()方法的行為
class Car():
    def exclaim(self):
        print("I'm a Car")
class Yugo(Car):
    def exclaim(self):
        print("I'm not a car")
car = Car()
yugo = Yugo()
car.exclaim()
yugo.exclaim()

#可以覆寫任何方法,包含__init__()
#使用Person類別製作代表醫生與律師的子類別
class Person():
    def __init__(self, name):
        self.name = name
class MDPerson():
    def __init__(self, name):
        self.name = "Doctor " + name
class JDPerson():
    def __init__(self, name):
        self.name = "Lawyer " + name
person = Person("Hugh")
doctor = MDPerson("Hugh")
lawyer = JDPerson("Hugh")
print(person.name)
print(doctor.name)
print(lawyer.name)

#添加方法
#可以在子類別加入父類別沒有的方法
class Car():
    def exclaim(self):
        print("I'm a car")
class Yugo(Car):
    def exclaim(self):
        print("I'm not a car")
    def need_a_push(self):
        print("Any help?")
a_car = Car()
a_yugo = Yugo()
a_yugo.need_a_push()
#a_car.need_a_push() #通用的Car物件無法使用

#使用super讓父類別幫忙
#假如想要呼叫父類別的方法?
class Person():
    def __init__(self, name):
        self.name = name
#定義名為EmailPerosn的新類別,代表email與person
class EmailPerson(Person):
    def __init__(self, name, email):#為類別定義__init__()時,會取代父類別的__init__()方法,因此不會呼叫後者
        super().__init__(name) #取得父類別Person的定義
        self.email = email
bob = EmailPerson('Bob', "bb@gmail.com")
print(bob.name)
print(bob.email)

#self防衛
#Python會使用self引數來尋找正確物件的屬性與方法
car = Car()
car.exclaim()
Car.exclaim(car)

#使用特性來取得屬性值與設定
class Duck(): #定義一個Duck類別
    def __init__(self, input_name):
        self.hidden_name = input_name #只有hidden_name一個屬性
    def get_name(self): #定義第一個方法
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name): #定義第二個方法
        print("inside the setter")
        self.hidden_name = input_name
    name = property(get_name, set_name) #將兩種方法定義為name屬性的特性

fowl = Duck('Hugh') #參考Duck物件的name時,會呼叫get_name()方法
fowl.name
fowl.get_name() #可以直接呼叫get_name()

fowl.name = 'Hugh2'
fowl.name
fowl.set_name('Hugh2')
fowl.name
#使用裝飾器定義特性
class Duck(): #定義一個Duck類別
    def __init__(self, input_name):
        self.hidden_name = input_name #只有hidden_name一個屬性
    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
fowl = Duck('Hugh')
fowl.name

fowl.name = 'Hugh2'
fowl.name

#特性可以參考算出來的值
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
c.radius
c.diameter
#可隨時更改屬性值
c.radius = 7
c.diameter
#假如沒有指定setter特性給屬性,則無法在外面設定
c.diameter = 20
#使用特性好處: 更改屬性定義時,只需修改類別定義裡的程式

#搞砸私用名稱
#如果變數不希望直接被取用
#則可以給兩條底線 例如 self.__name
class Duck(): #定義一個Duck類別
    def __init__(self, input_name):
        self.__name = input_name #只有hidden_name一個屬性
    @property
    def name(self):
        print("inside the getter")
        return self.__name
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.__name = input_name
fowl = Duck('Hugh')
fowl.name

fowl.name = 'Hugh'
fowl.name
#無法存取__name屬性
# fowl.__name
fowl._Duck__name #這種命名變成的樣子

#方法類型
#裝飾器說明接下來的函式是一個類別方法
#參數指向類別本身
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm A")
    @classmethod
    def kids(cls): #cls參數指向類別(A)
        print("A has", cls.count, "objects")
                  #也可以使用 A.count
easy_a = A()
b_a = A()
c_a = A()
A.kids()

#靜態方法
#沒有原本的self和class參數
class Coyoteweapon():
    @staticmethod
    def commercial():
        print("the Ad")
Coyoteweapon.commercial()

# Duck Typing
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + "."

class QuestionQuote(Quote):
    def says(self):
        return self.words + "?"
class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!"

hunter = Quote("Hugh", "I'm hunting")
print(hunter.who(), "says:", hunter.says())

hunted1 = QuestionQuote('Hugh1', "I'm hunting again")
print(hunted1.who(), "says:", hunted1.says())

hunted2 = ExclamationQuote("Hugh2", "Hunting Again")
print(hunted2.who(), "says:", hunted2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
brook = BabblingBrook()
def who_says(obj):
    print(obj.who(), 'says:', obj.says())
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)
who_says(BabblingBrook())

#特殊方法
#建立Word類別, 使用equals()方法才比較兩個單字,忽略大小寫
class Word():
    def __init__(self, text):
        self.text = text # self.text是Word物件裡的文字字串
    def equals(self, text2):
        return self.text.lower() == text2.text.lower() #將text與text2的文字字串比較
#使用三個不同的文字字串製作三個Word物件
first = Word('Ha')
second = Word('hA')
third = Word('He')
first.equals(second)
first.equals(third)

#將equals()方法更改為特殊名稱 __eq__()
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, text2):
        return self.text.upper() == text2.text.upper()
first = Word('Ha')
second = Word('hA')
third = Word('He')
first == second
first == third

first = Word('ha')
first
print(first)
#將__str__()與__repr__()加入到Word類別
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, text2):
        return self.text.lower() == text2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self): #representation
        return 'Word("' + self.text + '")'
first = Word('ha')
first #uses __repr__
print(first)

class Test():
    def __init__(self):
        pass
    def __str__(self): #如果調用了print function，其輸出是__str__返回的字串
        return "the str"
    def __repr__(self): #若是直接輸入變數，輸出則為__repr__返回的字串
        return "repr"
a = Test()
a
print(a)

#組合
#製作bill與tail物件,並提供新的duck物件
class Bill():
    def __init__(self, description):
        self.description = description
class Tail():
    def __init__(self, length):
        self.length = length
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("The duck has a", self.bill.description, 'bill and a', self.tail.length, 'length')
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()

#具名Tuple
#Tuple的一種子類別 可以用名稱(.name)及位置([offset])來存取值
#將Duck類別轉換成具名Tuple,使用bill和tail作為字串屬性
#呼叫namedtuple會使用兩個引數 1.名稱 2.欄位名稱字串,以空格分開
from collections import namedtuple #必須先載入模組
Duck = namedtuple('Dcuk', 'bill tail')
duck = Duck('wide orange', 'long')
duck
duck.bill
duck.tail

#使用字典來製作具名tuple
parts = {'bill':'wide orange', 'tail':'long'}
duck2 = Duck(**parts) #關鍵字引數,取出部分的鍵與值並當成引數傳給Duck()
duck2
duck2 = Duck(bill = 'wide orange', tail = 'long')
#具名tuple不可變,但可以更換屬性並回傳
duck3 = duck2._replace(tail = 'big', bill = 'small')
duck3
#將duck定義成字典
duck_dict = {'bill' : 'wide orange', 'tail' : 'long'}
duck_dict
#將欄位加入字典
duck_dict['color'] = 'green'
duck_dict
#不是加到具名tuple
#duck.color

#具名tuple的優點
# 外觀與行為都像不可變物件
# 節省空間與時間
# 可以用句點標記法取代字典的方括號來存取屬性
# 可當成字典鍵使用
