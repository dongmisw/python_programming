#0412
#자료형 - 리스트 , 튜플, 딕셔너리, 집합
# "김밥", "떡볶이", "돈까스" 
'''
리스트 
["김밥", "떡볶이", "돈까스", "칼국수"]  
튜플
("김밥", "떡볶이", "돈까스") 

딕셔너리 - 사전     apple - 동그란 빨간 과일
{k1:v1 , k2:v2}
address = {"홍길동":"구로구", "김길동":"부천", "박길동":"인천" }
 '''

#["김밥", "떡볶이", "돈까스", "칼국수"]  

#1. 빈 리스트를 만들어서, 하나씩 원소를 추가 하는 방식
lst = []
print(type(lst))
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육") 
#print(lst)
'''
print("list에서 3번째에 있는 값입니다.: ", lst[2])

#점심메뉴 출력하기 1
for i in range(len(lst)):
    print(lst[i])

#점심메뉴 출력하기 2
for item in lst :
    print(item)

print(lst)
print('lst.count("탕")', lst.count("탕"), ' lst.index("탕") : ', lst.index("탕") )

#len(lst) => 11
# slicing 
[     0   ,   1   , 2  , 3   ,  4     ,    5   ,   6   ,   7   ,    8   ,   9   ,   10  ]
['써브웨이','학식','김밥','햄','감자튀김','탕수육','파스타','햄버거','탕수육','햄버거','탕수육']
#lst[start :end :step ]
#lst[0,10, 1]  0~(10-1),step 수 만큼 뛰어 넘어라.
print(lst[::]) #전체
print(lst[0:len(lst):1])#전체 [0:11:1]  0~10
print(lst[0:8:2])# 0~7 2칸씩 뛰어넘기. '써브웨이''김밥''감자튀김''파스타'
print(lst[3:7:1]) # 3~6   햄'감자튀김', '탕수육', '파스타'
print(lst[::-1]) #거꾸로
print(lst[0:6:3]) # 0 ~5  3칸씩 0,3 '써브웨이','햄'

lst.append("김밥")
lst.append("라볶이")
lst.append("김밥")
print(lst)

lst.remove("김밥")
print(lst)

lst.remove("김밥")
print(lst)

#lst.remove("커피")
lst.append("커피")
print(lst)

item1="커피"
if item1 in lst :
    lst.remove(item1)
    print("커피존재함", lst)
else:
    print("커피 존재 안함", lst)


#pop
print(lst)
print("lst.pop() : ", lst.pop())
print(lst)


print("lst.pop() : ", lst.pop())
print(lst)

print("lst.pop() : ", lst.pop(0))
 
#l1 <=l1 + l2
print(lst)
dessert = ["케잌","커피","우유", "와플"]
print(dessert)
lst.extend(dessert)
print(lst)
 
#print(lst.extend(dessert))

x = "15"  #string
print(type(x))
# x 를 숫자로 바꿈. +1
print(x+ "1" ) #151   "15" + "1"  =>151
#print(x+ 1 ) #151
print(int(x) + 1 ) #16
print(type(x))  #어떤 타입? 

#sort vs sorted
l1 = ["orange", "apple", "mango","kiwi","banana"]

print(l1)
#l2 = sorted(l1)
#print(l2)
print(sorted(l1))
print(l1)

print("===  l1.sort()실행 ====")
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.clear() # 비어있다.   l1 = []
print(l1)

 '''


#리스트 컴프리핸션
#리스트를 선언할때, 짧게 , 빠르게 간결하게 하고싶다.
#0~10까지 숫자가 있는 리스트를 선언하라.
#1) 그냥 선언
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print("l2 : ", l2)
#2) for 문으로 append
l3 = []
for i in range(11) :  # 0~ 10 , 00,1,2,3,4,5,....,10
    l3.append(i)
print("l3 : ", l3)

#3) 리스트 컴프리핸션
l4 = [ i for i in range(11) ] 
print("l4 : ", l4)

#4)0-10 까지의 숫자의 제곱을 리스트에 넣어라,
#[0,1,4,9,....,81,100]     i**2
#l5 = []
#for i in range(11): # 0~10
#    l5.append(i**2)

l5 = [ i**2 for i in range(11) ]
print(l5)


#5)0-10 까지의 숫자의 3배수 리스트에 넣어라,
#[0,3,6,9,....,27,30]     
l6 = [ i*3 for i in range(11) ]
print(l6)

#6) hello를 10번 넣어라.
#['hello', 'hello'.....,'hello']      
#l7 = []
#for i in range(10) : #0~9
#    l7.append("hello")

l7 = [ "hello" for i in range(10)]
print(l7)

#7) 0-10 까지  짝수들의 제곱을 리스트에 넣으시오.
# [0,4,16,36,64,100]

l8 = []
for i in range(11) :
    if i % 2 == 0  :
        l8.append (i**2)

print(l8)    

l9 = [ i**2 for i in range(11) if i % 2 == 0]
print(l9)

l80 = []
for i in range(11) :
    if i % 2 == 0  :
        if i %3 == 0 :
            l80.append (i**2)

print(l80) 
l91 = [ i**2 for i in range(11)    if i % 2 == 0     if i %3 == 0]
print(l91)



#list 를 복사
#shallow copy
a = [0, 4, 16, 36, 64, 100]
b = a  #메모리 주소를 공유
print("a  :  ", a)
print("b  :  ", b)

a.pop()
print("=== after a.pop()  ")
print("a  :  ", a)
print("b  :  ", b)

print("a is b : " , a is b)

b.append("333")
print("=== after  b.append(333)  ")
print("a  :  ", a)
print("b  :  ", b)

#deep copy
print("deep copy")
#c = a[:]  # a[:]
#c= a.copy()
c = list(a)
print("a is c : " , a is c)
print("a  :  ", a)
print("c  :  ", c)

a.pop()
print("==== after a.pop()")
print("a  :  ", a)
print("b  :  ", b)
print("c  :  ", c)

c.append(555)
print("==== after c.append(555)")
print("a  :  ", a)
print("b  :  ", b)
print("c  :  ", c)