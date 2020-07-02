###############################################################################
# 03-1 if
###############################################################################

money = True
    if money:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")





money = 2000
    if money >= 3000:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")



money = 2000
card = True
    if money >= 3000 or card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")





pocket = ['paper', 'cellphone', 'money']
    if 'money' in pocket:
        print("택시를 타고 가라")
    else:
        print("걸어가라")





pocket = ['paper', 'cellphone', 'money']
    if 'money' in pocket:
        pass
    else:
        print("걸어가라")





pocket = ['paper', 'handphone']
card = True
    if 'money' in pocket:
        print("택시를 타고가라")
    else:
        if card:
            print("택시를 타고가라")
        else:
            print("걸어가라")



pocket = ['paper', 'cellphone']
card = True
    if 'money' in pocket:
        print("택시를 타고가라")
    elif card:
        print("택시를 타고가라")
    else:
        print("걸어가라")







if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")





pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")



score = 50

if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)


score = 50
message = "success" if score >= 60 else "failure"
print(message)

###################
# 03-1  if  Quiz  #
###################

# Q1. age와 height 변수가 주어졌을 때 8세 이상이고, 키 100 이상인 경우만
#     '놀이기구 탈 수 있음' 이라는 조건문을 작성하세요.













# Q2. 서울(seoul) 우유는 1리터(1000)에 2500원이고
# 매일(maeil) 우유는 1.8리터(1800)에 4200원일 경우
# 용량대비 어떤 우유가 더 싼지 계산 및 판단하여 결과를 출력하세요
# 서울우유가 더 싸면 '서울우유 win' 매일우유가 더 써면 '매일우유 win'











###############################################################################
# 03-2 while
###############################################################################

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
while number != 4:
    print(prompt)
    number = int(input())






coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break




# coffee.py

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break






a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)





while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")



###################
# 03-2 while Quiz #
###################

# Q1. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보세요.












# Q2. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보세요.
*
**
***
****
*****












###############################################################################
# 03-3 for
###############################################################################

test_list = ['one', 'two', 'three']
for i in test_list:
        print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)






# marks1.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)








# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)







a = range(10)
a

a = range(1, 11)
a





sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)







#marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))






for i in range(2,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print(i*j, end=" ")
    print('')





a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)





a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)




result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)


###################
# 03-3 for  Quiz  #
###################

# Q1. for문을 사용해 1부터 50까지의 숫자를 출력해 보세요










# Q2. for문을 사용해 1에서 10까지 출력하되 3의 배수는 건너뛰는 프로그램을 작성해 보세요.











###################
#     심화학습     #
###################












