# 0502
# 함수
#input을 주면 output이 나오는것.

'''
input - 숫자 - num1
output = 숫자 - ouput_num
이런 기능을 하는 function - multi
'''

#print(multi(10)) # return 30

#3을 곱하는 함수
#함수 정의
def multi(num1) :
    output_num = num1 * 3
    print("여기는 multi 함수 안입니다.")
    return output_num

#정의한 함수를 호출한다.
print(multi(10)) # return 30


#
# function - hello
# parameter - input - 사람이름 두개입력, 
# ouput - 안녕 1번사람, 안녕 2번사람
# 함수내에서 출력하시오

#function 선언
def hello(n1="홍", n2="김"):
    print("안녕 ,", n1)
    print("안녕 , ",n2)
print("기본값")    
hello()

print("사용자값")
hello("하하하", "호호호")

# 두개의 숫자를 입력받아, 
# 두개의 합을 함수내에서 출력하시오.

def mysum(num1, num2) :
    print("두 숫자의 합은 : " , num1 + num2)

mysum(100,1000)

def mysum2(num1, num2) :
    return num1+num2

result = mysum2(100,2000) # return 2100 
print(result)
print(mysum2(100,2000))


# 지역 변수, 전역 변수
'''
num = 100 #전역 변수 global variable
print("*** num: ", num)  # 100

def addone() :
    num = 10
    print(" addone()" , num + 1)  # num + 1 \=> 11
    print(" addone() num : " , num) # num =10
    num = num *8 + 20
    return num 

result1 = addone()
print("*** num : ", num)   # 100
print("*** num : ", result1)   # 100
'''
'''
# 2) 변수를 수정하지 않으면, 내부 function에서도 전역변수 사용 가능
num = 100   #전역 변수 global variable
print("*** num: ", num)  # 100

def addone() :
    # 내부 function 에서 num를 수정하지 않을때.  
    print(" addone()" , num + 1)  # num + 1  
    print(" addone() num : " , num) # num = 
     
addone()
print("*** num : ", num)   # 100 
'''

'''
#3) 내부 function에서 전역변수를 사용하면 좋겠고
# 수정도 하고 싶고, function이 끝나도 그 값이 반영되었으면 좋겠음

num = 100   #전역 변수 global variable
print("*** num: ", num)  # 100

def addone() :
    global num  # 전역 변수를 쓰겠다. 변수에 새로운 값 대입가능
    num = num + 1      
     
addone()
print("*** num : ", num)    # 101
'''


#인자의 갯수가 여러개인 경우
print()
print(1,2,3,4,5,6,7,9)
print()

def hello2(*names) :    #안녕 찍기
    for i in names:
        print("hello ", i)  # hello 홍길동

hello2("홍길동", "김", "이","박")

#합을 구하는 function
def mysum2(*numbers) :
    result = 0 
    for num in numbers:
        result = result + num
    return result

print("합: " , mysum2(1,2,1,2,1,2,3,4,67,9))
lst1 = [1,2,1,2,1,2,3,4,67,9]
print(mysum2(*lst1))

# dictionary = {key1:value1, key2:value2}
# 
coffee ={"아메":2000, "라떼":3000, "티":2500}

def printmenu(**keyvalue):
    for key in keyvalue :
        print(key , keyvalue[key])
        
printmenu(**coffee)
printmenu(아메=2000, 라떼=3000, 티=2000, 핫초코=4000, 핫도그=3000)


def func1(*num, **menu):
    result = 0 
    for n in num:
        result = result + n
    print(result)

    for key in menu :
        print(key , menu[key])

coffee ={"아메":2000, "라떼":3000, "티":2500}
lst1 = [1,2,1,2,1,2,3,4,67,9]

func1(1,2,3,1,3,2,2,3,4,2,4,3,아메=3000, 핫초코=2000, 핫도그=3000)
func1(*lst1, **coffee)
func1(1,2,3,1,3,2,2,3,4,2,4,3,**coffee)


#lambda function
# function을 만드는데, 이름짓기가 귀찮다. 실행문이 하나밖에 없다. 

def addone(x):
    return x+1
print(addone(100))

#lambda parameter_name : parameter로 실행하는 문
print((lambda x : x+1)(100))



def mysum2(num1, num2) :
    return num1+num2

print(mysum2(100,1000))

print((lambda num1, num2 : num1+num2)(100,1000))
'''
# map, filter
list가 존재할떄, 
lst1= [1,2,3,4,5,6,7]
addone()
lst2 = [2,3,4,xxxx,]

map(함수, input 리스트)

map(lambda함수, input 리스트)
map(addone, lst1)  
(lambda x : x+1)(100)
'''
lst1= [1,2,3,4,5,6,7]
print(list(map(lambda x : x+1, lst1)))

# 
#@lambda num1, num2 : num1+num2
lst1= [1,2,3,4,5,6,7]
lst2= [1,2,3,4,5,6,7]
# result = [2,4,6, 8, 10...., 14 ]
# map(함수, input 리스트,inputlist2)
print(list(map(lambda num1, num2 : num1+num2, lst1 ,lst2 )))

#map(lambda num1, num2 : num1+num2, [1,2,3,4,5,6,7] ,[1,2,3,4,5,6,7] )