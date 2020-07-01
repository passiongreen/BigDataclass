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














