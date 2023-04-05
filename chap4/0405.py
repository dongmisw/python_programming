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
else:
    print("else안의 문구: for문이 잘 종료됨.")

print(" 완전 바깥. else밖의 문구 : for 문 종료됨")
   
 
 
# print(i , end=' ' )
# while
while 조건 :
    수행문1
else:
    수행문2   

#sum , 0-10까지 숫자를 찍음
# sum을 구할것임.
sum = 0
n=0
while n<11 :   
    sum += n
    print(n, "  번째 sum  : ", sum  )
    n= n+1

print("while 밖에서 sum의 값  : ", sum)

while False:
    print("실행이 되지 않음")

while 0:
    print("실행이 되지 않음")

print("while 0 다음 줄입니다. ")

#while True :
#    print("무한루프")

#while False:
#    print("실행이 되지 않음")
    
'''

'''
#break continue 
# 단어 입력을 무한 루프로 받는다.
# 그 글자를 3번 써줌
#"exit" -> 루프를 끝내고 종료
#"apple" -> 3번 안쓰고 그냥 다시 단어 입력을 받음.

while True :
    word = input("단어를 입력하세요.")
    if word =="exit":
        print("넌 exit 을 입력했다. break를 만난다.")
        break
        print("break 뒤의 문장 ")
    elif word =="apple" :
        print("넌 apple을 입력했다. continue를 만난다.")
        continue
        print("continue뒤의 문장")
    else:
        for i in range(3):
            print(word, end=' ')
        print("해당 단어 끝")

    print("apple을 넣으면 이걸 절대 볼수 없음")


'''
'''
while True :
    단어 입력을 받는다. 
    if exit인경우:
        break
    elif apple인 경우:   
        continue
    else :
        for :   
            3번 찍는다.
'''


#놀이동산 놀이기구 탑승 문제
#총 정원 4명 
#정원이 차면, 놀이기구 시작
#조건 키 150 이상만 탈수 있음.
#사람들한테 키를 물어보고, 탑승시키시오. 
#150이상 4명이 되면 놀이기구를 시작
#수도코드를 작성해볼것. 
#진짜코드도 작성할것






