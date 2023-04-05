#0405 
#문자열 
'''
str = "파이썬수업 씨수업 자바수업 파이썬수업 파이썬수업 "
str2 = "파이썬수업,씨수업,자바수업,이썬수업,파이썬수업"

#format
#3+4=7
print(3, "+" ,4, "=",7)
f1= "{} + {} = {}".format(3,4,3+4)
f2= "{0} + {1} = {2}, {2}, {2}, {2}".format(3,4,3+4)
f3= "{0:d} + {1:f} = {2:f}, {2}, {2}, {2}".format(3,4.0,3+4.0)
f4= "{0:10d} + {1:10f} = {2:10.3f}".format(3,4.0,3+4.0)
print(f4)

#join
#print("**".join(str))

#split
#print(str.split())
print(str2.split(","))
print(str2.split("업"))

#find, index
print("find : ", str.find("씨") , "index  : ", str.index("씨"))
print(str.find("에이아이")) # 없을때 return -1
print(str.index("에이아이")) # 없을때 error 냄

#replace 
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬"))

#bool 
print(type(True), type(False))
a = "hello"
print(bool("hello"), bool("hi"), bool(3), bool(1.2), bool(-2))
print(bool(""), bool(0))
print(int(True), int(False), str(True))

'''
# 조건문
'''
if 조건1 :
    실행문1
 

if 조건1 :
    실행문1 #참
else :
    실행문2 #거짓

if 조건1 :
    실행문1 #참
elif 조건2:
    실행문2
    ...
elif 조건10:
    실행문10
else :
    실행문3 #거짓


 
#오전/오후/저녁 
h = 20     
if h < 12 :
    print("오전 ", h, " 가 12보다 작다 ") #h가 12q보다 작을때
elif h<18 :  # 12 < h < 18
    print("오후 ", h, " 가 12보다 크고 18보다 작아요 ") #h가 12q보다 작을때
else :    #18<h 
    print("저녁 ", h , "는 18보다 크다.")
 

lunch = input("밥 먹을래?")
if lunch == "yes" :
    print("밥을 먹고싶군요.")
    cafeteria = input("학식?")
    if cafeteria == "yes" :
        print("8호관 1층으로 ")
    else :  
        print("학식을 싫어하는군요.")
        subway = input("subway? ")
        if subway == "yes":
            print("8호관 1층으로 고고")
        else :
            print("subway를 싫어하는군요.")
else:
    print("밥 먹기 싫군요.")

'''


# for, while
# 반복문 
# in range
'''
for i in 10,25,32,4354,635,216 :
    print("i : " , i)
 
#range
for i in range(3,21,3):
    print("i : " , i)


for i in range(20):
    print("i : " , i)
'''

#1부터 10까지 합을 구하시오.
#2가지 방법으로, range도 쓰고, 그냥 명시도 하고

sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    #sum = sum + i
    sum += i
    print( i ," 번째 loop입니다. sum은 ", sum ," 입니다.")
  

print("range를 사용하였음")
sum = 0
for i in range(1,11,1) :
    sum += i
    #sum = sum + i
    print( i ," 번째 loop입니다. sum은 ", sum ," 입니다.")
 
#else할것.















