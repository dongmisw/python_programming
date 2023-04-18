#0418
#튜플, 딕셔너리, 집합
lst =[]
#수정, 변경, 일부 원소 삭제 가능

#수정이 불가항목들. -> 튜플
t1 = (1,2,3,4)
print(t1)
t2 = tuple()
print(t2)
t3 = 1,2,3,4,5,3,3,10,3
print(type(t3))

print(t3.index(3))
print(t3.count(3))

t4 = 1,2,3,4,5,3,3,10,3
t5 = 100,200,300
print("t4+t5 : ", t4+t5 )
print("t4 : " , t4)
print("t5 : ", t5) 

print("t4 : " , t4)
print(sorted(t4))  #원본은 안바뀜
print("t4 : " , t4)
#lst.sort() #원본이 바뀜.

#dictionary
#key:value 
#1001:"홍길동", 1002:"김길동"

d1 = {1001:"홍길동", 1002:"김길동", 1003:"박길동", 1004:"고길동"}
print(d1[1001])
#print(d1[key])

#d2={}
#강좌에 대한 dictionary
d2 = dict()
d2['강좌명'] = '파이썬'
d2['개설 요일'] = '화요일'
d2['년도'] = 2003
d2['수강생'] = ['김', '이', '박']
print("d2  : " , d2)
print(d2['수강생'])
print(len(d2))


#dictionary  key:value 1:1월, 2:2월... 12:12월


'''
month = {10:'1월', 20:'2월', 30:'3월', 40:'4월', 50:'5월', 60:'6월', 70:'7월' ,80:'8월',90:'9월',100:'10월',110:'11월',120:'12월'}

#dictionary method
print("month.keys() : ", month.keys())
print("month.values(): ",month.values())
print("month.items(): ",month.items())
'''

# for문을 돌려서 각각의 value값을 찍어라.
#1) key값이 숫자인것을 활용
month = {10:'1월', 20:'2월', 30:'3월', 40:'4월', 50:'5월', 60:'6월', 70:'7월' ,80:'8월',90:'9월',100:'10월',110:'11월',120:'12월'}
for i in range(10,121,10) :   #1,2,3,4,5....12
    print(month[i])

#2) month.keys() 활용
for kim in month.keys():    #[10,20,30,40,...,120]
    #print("kim: ", kim)
    print(month[kim])

#3) month.values() 활용
print("month.values()활용")
for m in month.values() : #['1월', '2월',... , '12월']
    print(m)

#4) month.items() 활용
print(month.items())
print("month.items()")
for item in month.items():
    #item - (10, '1월')
    #print(item)
    print(item[1])

#5) month.items() 활용
print("month.items() 2 ")
for k,v in month.items():
    #item - (10, '1월') (item[0], item[1]) (k, v)
    #print(item)
    #print(item[1])
    print(k)
    print(v)

#month = {10:'1월', 20:'2월', 30:'3월', 40:'4월', 50:'5월', 60:'6월', 70:'7월' ,80:'8월',90:'9월',100:'10월',110:'11월',120:'12월'}
#6) month.keys() month
for i in month:  # month.keys()
    print(i)  # key - 10
    print(month[i]) #value

print("month.pop(10) : ", month.pop(10)) # key값을 주고, 해당 item을 제거.
print(month)
print("month.popitem(): ", month.popitem()) #제일 마지막 item을 제거
print(month)

month.update({30:'March'})
print(month)
month.update({150:'15월'})
print(month)
month.update({30:'300월'})
print(month)

# dictionary-tuple-list 변환
# tuple - 변경불가.수정.x    (아메 , 핫초코, 라떼)
#tuple ->list  유자차 추가 => tuple 변경
# list -> tuple   수강신청 전 수강생 변경, -> tuple
# tuple, list => dictionary  (1,2,3,4) , (홍, 김, 박, 이)

seql = ['a','b','c','d']  
seqt = tuple(seql)
print(seqt)
print(type(seqt))
 
seql2 = list(seqt)
print(seql2)
print(type(seql2))

seqd = dict(enumerate(seql))
print(seqd)
print(type(seqd))


# zip 
# list, tuple 가 여러개. -> 하나의 튜플의 조합으로 된 리스트로.
l1 = ['1조','2조','3조']
YA = ['홍', '김', '이']
YB = ['최', '한', 'James']

z = zip(l1, YA, YB)
print(type(z))
print(z)
print(list(z))

print(tuple(zip(l1, YA, YB)))


#
l10 = ['한식',    '양식' ,  '중식',    '분식']
l11 = ['전주식당', '닥터로빈', '취영루', '토마토']
l12 = ['제육',     '파스타',    '짬뽕', '김밥']
#print(list(zip(l10, l11, l12)))
#for i in range(4):
#    print(l10[i] , l11[i], l12[i])

l100 = list(zip('ABCD',l11, l10, l12))
for i in l100:
    print( i[0], i[1], i[2], i[3])


'''
l100 = list(zip(l11, l10, l12))
for i in l100:
    print( i[0], i[1], i[2])
'''

#zip list1, list2 => list3
#a , b   
#[(a1, b1), (a2, b2)]

l10 = ['한식',    '양식' ,  '중식',    '분식']
l11 = ['전주식당', '닥터로빈', '취영루', '토마토']
l12 = ['제육',     '파스타',    '짬뽕', '김밥']

#dictionary
print(list(zip(l10, l11)))
print(dict(zip(l10, l11)))

#print(dict(zip(l10, l11, l12)))

print(dict(zip(l10, zip(l11, l12))))


#           0          1      2            3
l11 = ['전주식당', '닥터로빈', '취영루', '토마토']

print(list(enumerate(l11)))
print(dict(enumerate(l11)))


#문제 - 강의실 알려주기

# dictionary로 만든다.
# for문 ,while도 됨
# quit이 들어올때까지 계속 받는다.
# input ()  => 강의명 입력
# 강의실을 알려줌.

lecture = ["파이썬", "c++",  "AI", "java", "spring"]# 5개 강의명
space = [101, 102, 103, 104, 105] #강의실
d = dict(zip(lecture, space))
#{'파이썬':101, c++:102...}
while True:
    c = input("강의명을 쓰세요")
    if c == "quit" :
        print("quit을 입력했으니, 종료합니다.")
        break
    else :
        if c in d.keys():
            print(d[c])
        else:
            print("컴퓨터과 과목만 넣으세요.")
            continue
    

