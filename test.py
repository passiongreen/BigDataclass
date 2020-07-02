a = 0
if a>0:
    print("긍정")
elif a<0:
    print("부정")
else:
    print("zero")
odd = [1, 3, 5, 7, 9]
a = 123
a = -178
a = 0
a = 3
b = 4
a+b
a / b
a - b
a ** b
7 % 3
3 % 7
7 / 4
7 // 4
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too shotrt, You need python'''
food = "Python's favorite food is perl"
food = 'Python's favorite food is perl'
say = '"Python is very easy." he says.'
food = 'Python\s favorite food is perl'
say = "\"Python is very easy.\" he says."
multiline = "Life is too short\nYou need python"
multiline
print(multiline)
multiline = '''
Life is too short
You need python
'''
multiline = """
Life is too short
You need python
"""
print(multiline)

multiline = "Life is too short\nYou need python"
multiline
print(multiline)

head = "Python"
tail = " is fun!"
head + tail

a = "python"
a * 2

a = "Python"
a * 2

print("=" * 50)
print("My program")
print("=" * 50)

a = "Life is too short"
len(a)

a = "Life is too short, You need Python"

a[3]

a[0]

a[12]

a[4]

a[-1]

a[-0]

a = "Life si too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b

a = "Life is too short, You need Python"
a[0:4]
a[0:5]

a[5:7]

a = "Life is too short, You need Python"
len(a)

a[19:]

a[:19]

a[:]

a[19:-8]

a = "20010331Rainy"
date = a[:8]
weather = a[8: ]
date
weather

year = a[:4]
day = a[4:8]
weather = a[8:]

year
day
weather


a = "Piathon"
a[1]
a[1] = 'y'

a[:1]
a[2:]
a[:1] + 'y' + a[2:]

"I eat %d apples." %3

"I eat %s apples." %"five"

number = 3
"I eat %d apples." % number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

"I have %s apples" % 3
"rate is %s" % 3.234

"%10s" % "hi"
"%-10sjane." % 'hi'

"%0.4f" % 3.42134234

"%10.4f" % 3.42134234

"I eat {0} apples".format(3)

"I eat {0} apples".format("five")

number = 3
"I eat {0} apples".fotmat(number)

number = 3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

"I ate {0} apples. so I was sick for {day} days.".format(10,day=3)

"{0:>10}.format("hi)

"{0:^10}".format("hi")

"{0:>10}".format("hi")

"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)

"{{ and }}".format()

name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

age = 30
f'나는 내년이면 {age+1}살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'
y = 3.42134234
f'{y:0.4f}'
f'{y:10.4f}'

a = "hobby"
a.count('b')

a = "Python is the best choice"
a.find('b')
a.find('k')

a = "Life is too short"
a.index('t')
a.index('K')

",".join('abcd')

",".join(['a', 'b', 'c', 'd'])

a = "hi"
a.lower()

a = "hi"
a.lstrip()

a = "Life is too short"
a.replace("Life", "Your leg")

a = "Life is too short"
a.split()

 b = "a:b:c:d"
 b.split(":")
 
odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]


a = [1, 2, 3]
a
a[0]
a[0] + a[2]
a[-1]

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
a[-1]
a[3]
a[-1][0]
a[-1][1]
a[-1][2]

a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2]
a[2][2][1]

a = [1, 2, 3, 4, 5]
a[0:2]

a = "12345"
a[0:2]

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]

a = [1, 2, 3]
b = [4, 5, 6]
a + b

a = [1, 2, 3]
a * 3

a = [1, 2, 3]
len(a)

a = [1, 2, 3]
a[2] + "hi"

str(a[2]) + "hi"

a = [1, 2, 3]
a[2] = 4
a

a = [1, 2, 3]
del a[1]
a

a = [1, 2, 3, 4, 5]
del a[2:]
a

a = [1, 2, 3]
a.append(4)
a
a.append([5,6])
a

a = [1, 4, 3, 2]
a.sort()
a

a = ['a', 'c', 'b']
a.sort()
a

a = ['a', 'b', 'c']
a.reverse()
a

a = [1, 2, 3]
a.index(3)
a.index(1)
a.index(0)

a = [1, 2, 3]
a.insert(0,4)
a
a.insert(3,5)
a

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a
a.remove(3)
a

a = [1,2,3]
a.pop()
a

a = [1, 2, 3]
a.pop(1)
a

a = [1, 2, 3, 1]
a.count(1)

a = [1, 2, 3]
a.extend([4,5])
a
b = [6, 7]
a.extend(b)
a

food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

Life is too short
You need python

multiline = "Life is too short\nYou need python"

multiline = '''
Life is too short
You need python
'''
multiline="""
Life is too short
You need python
"""

print(multiline)
Life is too short
You need python

head = "Python"
tail = " is fun!"
head + tail

a = "Python"
a * 2

a = "Life is too short"
len(a)

a = "Life is too short, You need Python"
a[3]
a[7]
a[-8]

a = "Life is too short, You need Python"
b = a[-1] + a[-2] + a[-3] + a[-4] + a[-5] + a[-6]
b
a[0:4]
a[5:7]
a[12:17]
a[19:]
a[:17]
a[:]
a[19:-7]

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather
year = a[:4]
day = a[4:8]
weather = a[8:]
year
day
weather

a = [1, 2, 3]
a.append(4)
a

a = [1, 2, 3]
a.append([5,6])
a

a = [1, 4, 3, 2]
a

a.sort()
a

a = ['a', 'c', 'b']
a

a.reverse()
a

a = [1, 2, 3]
a.index(3)

a.insert(0,4)
a

a = [1, 2, 3, 1, 2, 3]
a

a.remove(3)
a
a.remove(3)
a

a = [1, 2, 3]
a.pop()
a

a = [1, 2, 3, 1]
a.count(1)

a = [1, 2, 3]
a.extend([4,5])
a
b = [6,7]
a.extend(b)
a

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
del t1[0]

t1 = (1, 2, 'a', 'b')
t1[0] = 'c'

t1 = (1, 2, 'a', 'b')
t1[0]
t1[3]

t1 = (1, 2, 'a', 'b')
t1[1:]

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2

t2 = (3,4)
t2 * 3

t1 = (1, 2, 'a', 'b')
len(t1)


{key1:Value1, key2:Value2, key3:Value3, ...}

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic

a = {1: 'a'}
a[2] = 'b'
a

a['name'] = 'pey'
a

del a[1]
a

grade = {'pey': 10, 'juliet': 99}
grade['pey']
grade['juliet']

a = {1:'a', 2:'b'}
a[1]
a[2]

a = {'a': 1, 'b': 2}
a['a']
a['b']

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic['name']
dic['phone']
dic['birth']

a = {1:'a', 1:'b'}
a

a = {[1,2] : 'hi'}

a = {'name': 'pey', 'phone': '0119993323', 'birht': '1118'}
a.keys()


list(a.keys())

a.values()

a.items()

a.clear()
a

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.get('name')
a.get('phone')
print(a.get('nokey'))
print(a['nokey'])
a.get('foo', 'bar')
'name' in a
'email' in a

s1 = set([1,2,3])
l1 = list(s1)
l1
l1[0]
t1 = tuple(s1)
t1
t1[0]

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1 & s2
s1.intersection(s2)
s1 | s2
s1.union(s2)
s1 - s2
s2 - s1
s1.difference(s2)
s2.difference(s1)

s1 = set([1, 2, 3])
s1.add(4)
s1

s1 = set([1, 2, 3])
s1.update([4,5,6])
s1

s1 = set([1, 2, 3])
s1.remove(2)
s1


a = True
b = False
type(a)
type(b)
1 == 1
2 > 1
2 < 1


bool('python')
bool('')

bool([1,2,3])
bool([])
bool(0)
bool(3)

a = 1
b = "python"
c = [1,2,3]

a = [1, 2, 3]
id(a)

a = [1,2,3]
b = a
id(a)
id(b)

a is b
a[1] = 4
a
b

13 % 2

a = "881120-1068234"
len(a)
a[:6]
a[7:]

pin = "991120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)

pin = "881120-1068235"
print(pin[7])

a = "a:b:c:d"
b = a.replace(":","#")
print(b)

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
b = a[0] + a[1] + a[2] + a[3]
print(b)
result = " ".join(a)
print(result)

t1 = (1,2,3)
t2 = ("4")
t1 + t2

a = (1,2,3)
a = a + (4,)
print(a)

a = dict()
a

a = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

a = [1,2,3,4]
a

a = 3
if a == 3:
    print("3이다")
if a > 5:
    print("5보다 크다")        
if a < 5:
    print("5보다 작다")


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = True
if money:
    print("택시를")
    print("타고")
    print("가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

'a' in ('a', 'b', 'c')

'j' not in 'python'

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print('걸어가라')


pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
        print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")


if score >= 60:
    message = "succes"
else:
    message = "failure"

message = "succes" if score >= 60 else "failure"

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number !=4:
    print(prompt)
    number = int(input())

    1. Add
    2. Del
    3. List
    4. Quit

Enter number:

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break



a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

while True:
    print("crtl+c를 눌러야 while문을 빠져나갈 수 있습니다.")

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)



a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)



marks = [90, 25, 67,  45, 80]

number = 0 
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)



marks = [90, 25, 67,  45, 80]

number = 0 
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)



a = range(10)
a
range(0,10)

a = range(1,11)
a
a(1,11)


add = 0
for i in range(1,11):
    add = add + i

print(add)


for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')


for i in range(2,10):
    for j in range(1,10):
        print(i, "*" , j, "=", i*j, " ", end=" ")
    print('')


a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)


a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


for i in range(1,101):
    print(i, end=" ")



a = 1
while a < 1000:
    a += 1
    if a % 3 == 0: 
        print(a)


result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

i = 0
while * < 5:
    i += 1
    if i > 5: break
print('*' *i)

A = [70,60,55,75,95,90,80,85,100]
total = 0

for score in A:
    total += score

average = total / len(A)
print(average)
























