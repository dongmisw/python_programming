'''
#1.py - __name__=1     
#2.py - __name__=해당파일이름 , 2
#3.py -  __name__= 3
#4.py   run __main   run  
#1.py 
#__name__



#dictionary


#lambda 

#filter와 lambda를 사용하여 
#리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

def positive1(x):  #input -=숫자. output, 0보다 클때 참, 0보다 작으면 거짓
    return x>0
#lambda 입력값:리턴 결과
lambda x : x>0

#filter(함수, 리스트)
print(list(filter(positive1,[1, -2, 3, -5, 8, -3] )))
print(list(filter( lambda x : x>0 ,[1, -2, 3, -5, 8, -3] )))

#숫자 리스트 두개를 받음.
#각각 같은 순서끼리 더하는 함수를 만들어라.
#lambda와 map을 써서 작성해라.
#lambda를 쓰지 말고도 해보세요.
list3=[10,20,30,40,50]
list4=[100,200,300,400,500]

#결과로 이것이 나오게 하시오. [110,220,330,440,550]
 
def mysum(n1, n2):
    return n1+n2
 
lambda n1, n2: n1+n2

print(list(map(mysum, list3, list4)))
print(list(map(mysum, [10,20,30,40,50], [100,200,300,400,500])))

print(list(map(lambda n1,n2:n1+n2, list3, list4)))




map, filter
map(함수, input list ) => 리스트
map(addone, [0,1,2])
=>[addone(0), addone(1), addone(2)]
 filter 
filter(lambda x: x>0, [-10,20,30]) 
=>[20, 30]
 


mem ={'홍':1, '박':2, '정':3}
print(mem)
mem['최'] =5
print(mem)
mem.update({'강':6})
print(mem)
mem['김']=7
print(mem)
mem.update({'최':8})
print(mem)
 
#key- value
#carDict= {key1:value1, key2:value2, key3:value3}
#자동차 등록번호: (생산년도, 배기량)
#1111: (2020,1600)
list1= [10,20,30,40,50,6]



carDict={ 'h101':('2020', '1600') ,
          'h102' :('2021', '2000'), 
          'b101':('2020', '3600') ,
          'b102' :('2021', '5200')}  


[2017, 2022, 2020, 2020, 2022] 
yearList=[]
# list append()
# values(), 0번째 값을 가져올수 있는가.
# int로 바꿀수 있는가

for value in carDict.values():
    yearList.append(int(value[0]))
print(yearList)

year = int(input("생산년도를 입력하시오")) #2020
print(year, "년도에 생산된 자동차는 ",yearList.count(2020)," 대입니다.")

year2 = int(input("생산년도를 입력하시오")) #2020
count = 0
for prod_year in yearList:
    if prod_year == year2:
        count +=1
print(count)








 
for item in carDict.items():
    print(item[0], item[1])

print("===========")

for key in carDict.keys():
    print(key, carDict[key])


#print(carDict.items())


print(carDict.keys())
print(carDict.values())
print(carDict.items())

H101 ('2017', '3000') 
K301 ('2022', '2700')
H401 ('2020', '3200') 
D221 ('2020', '1500') 
H111 ('2022', '3000') 
'''

'''
#7.3 zip
# list, tuple, 문자열. 여러개를 순서대로 묶어주는것.
L1 =[ 1,  2,   3,   4,  5]
L2 =['a', 'b','c','d','e']
print(list(zip(L1, L2)))

#스포츠 구기종목
sport=['축구', '야구', '농구','배구']
num = [11,9,5,6]

dictionary =  dict(zip(sport, num))
while 1 :
    s= input("구기종목을 입력하시오")
    if s =="quit" :
        print("quit을 입력하였다.끝")
        break 

    if s in dictionary.keys() :
        print("인원은 ", dictionary[s], "입니다.")
    else :
        print("몰라요")
        continue
    
    print("결론 - 입력한 구기종목은 ",s, "이고, 인원은 ", dictionary[s], "입니다.")
 



zip묶고,
input을 받아서,, 종목이름 입력받기.
선수 수를 출력하는것.
for문을 돌려서 할것. 
quit을 만나면 종료할것.
다른 종목 들어오면 "몰라요" 다시 입력 받을것.
continue, break를 활용할것. 
'''