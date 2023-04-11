#0411
#리스트, 튜플, 딕셔너리, 집합
# 김, 이, 박, 최, 
#리스트 
#['김', '이', '박', '최']

#튜플 
#('김', '이', '박', '최')

#딕셔너리 ->사전  {key:value, k1:v1, k2:v2,.....}
#address= {'홍길동': '서울', '김길동':'부천', 'james':'미국'}
#print(address['홍길동'])


'''
#list 
#숫자, int, float, string 다 가능함.
lst = [10,20,30,40,50]
str_list=['하', '호']
print(type(lst))
print(lst[0], " ", lst[1], " " , lst[len(lst)-1])

#빈리스트 생성 -> 하나씩 원소를 추가
list1=[]
#list2=list()
print(list1)
list1.append("python")
list1.append("java")
list1.append("c++")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")

print(list1)
print(list1[0])

print("-====for 1=====-") #range(3)  0,1,2
for i in range(len(list1)):
    print(list1[i])

print("-=====for 2====-")
for i in list1:    # for i in {python, java, c++}
    print(i)

print(list1)
print("count : " , list1.count("python"))
print("index : " , list1.index("python"))
#"hahah".index("a")

# list 수정
list1[0]="AI"
list1[2]="IoT"
print(list1)

#['AI', 'java', 'IoT', 'python', 'python', 'python', 'python']
list2 = list1[0:3:1]  #0~2 #AI', 'java', 'IoT'
print(list2)
list2 = list1[1:5:1]  #1~4  'java', 'IoT', 'python', 'python',
print(list2)
list2 = list1[1:len(list1):2]  # 1~6 , 1,3,5, 'java','python', 'python'
print(list2)
list2 = list1[2:6:3]  # 2~5  , 2, 5 'IoT','python'
print(list2)
list2 = list1[::-1]  
#'python', 'python', 'python', 'python, 'IoT', java, AI
print(list2)



#list1 ,  list3 
#list1 의 일부를 list3에 대입

list2 = list1[2:6:3]  # 2~5  , 2, 5 'IoT','python'
['IoT','python']
print(list2)
list3=[1,2,3,4,5,6,7,8]

#list3[1]=list2
#print(list3)

list3[1:2]=list2
print(list3)

#수정 불가 - > append, insert, 값 변경.x
#[1,2,3,4]
#(1,2,3,4)  t1+t2 => t3
#t1 +1 => t1

'''
#list insert 
food =[]
food.append("짜장면")
food.append("샌드위치")
food.insert(0,"파스타")
food.insert(0,"제육")
'''
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"제육")
print(food)

food.remove("제육")
print(food)

print("food.pop : " , food.pop())
print(food)
print("food.pop : " , food.pop())
print(food)

#extend
#print(food)
dessert=["커피","케잌", "와플"] 

food_list =food + dessert
#print(food_list)

food.extend(dessert)  # food + dessert
 

#print(food)
food.reverse()
#print(food)

#sort() 
#sorted()
l1 = ["banana","apple","orange","mango"]
print(l1)
print("sorted(l1): ", sorted(l1))
print("l1        : " , l1)

l1.sort()
print(l1)




 
a= "1"
print(type(a)) #string
print(int(a) + 5) #=> 6 
print(type(a))
#print(a + 5) #=> 6 ㄷerror
'''


#food.clear()
#del food
#print(food)

'''
#리스트 컴프리헨션
#0-10 까지 있는 list를 만들자.
#1) 
l3=[0,1,2,3,4,5,6,7,8,9,10]
print(l3)
#2)
l3=[]
for i in range(11) :
    l3.append(i)
print(l3)

#3) 리스트 컴프리헨션
#리스트 변수명  = [i for i in range() ]
l3 = [ i for i in range(11)]  #[0,1,2,3,...]
print(l3)

#10 
#0~10까지의 숫자의 제곱을 원소로 가지는 리스트를 작성
#i**2 
#[0,1,4,9,16,...,64,81,100]d
l4 = [ ]
for i in range(11) :
    l4.append(i**2)
print(l4)
 
l5= [ i**2 for i in range(11) ] 
print(l5)

#11 
#0~10까지의 숫자의 3배를 원소로 가지는 리스트를 작성
#i*3 
#[0,3,6,9,12,...30]
 
l6= [ i*3 for i in range(11) ] 
print(l6)

#12 
#"hello"를 10개 가지는 리스트 작성
l7=["hello" for i in range(10)]
print(l7)

l8=[]
for i in  range(10) :
    l8.append("hello")
print(l8)
 
#0-10까지의 숫자의 제곱을 리스트로 만들어라.
# 짝수의 제곱만 넣어라.
#[0,1,4,9,....100]
#[0,4,16, ... ,100]
l10=[]
for i in range(11) :
    if i%2 == 0: #짝수
        l10.append(i**2)
print(l10)

l11 = [ i**2 for i in range(11) if i%2 == 0 ]
print(l11)

'''

#shallow copy 
wishlist = food
print("food:     " , food)
print("wishlist: " , wishlist)

food.pop()
print("after food.pop()")
print("food:     " , food)
print("wishlist: " , wishlist)

print(food is wishlist)

#deep copy
food2 = food[:]
food3 = list(food)



print("deep copy ")
print("food:     " , food)
print("food2:    " , food2)
print(food is food2)
food2.append("김밥")
print("food:     " , food)
print("food2:    " , food2)

food.append("라뽁이")
print("food:     " , food)
print("wishlist: " , wishlist)
print("food2:    " , food2)









