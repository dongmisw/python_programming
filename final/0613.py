'''
mem={'홍':'1', '박':'2','정':'3'}
mem['최'] ='5'
print(mem)
mem.update({'강':'6'})
print(mem)
mem['김']='7'
print(mem)
mem.update({'최':'8'})
mem['최'] ='5'
print(mem)
mem.pop('홍')
print(mem)
'''
'''
#carDict
carDict = {'H101': ('2017', '3000'), 
           'K301': ('2022', '2000'), 
           'H401': ('2020', '3200'),
           'D221': ('2020', '1500'), 
           'H111': ('2022', '3000'), 
           'K301': ('2022', '2700')} 

print(carDict.items())

yearList=[]
for value in carDict.values():
    yearList.append(int(value[0]))
print(yearList)

year = input("생산년도를 입력하세요.") #'2020'
print(year, "의 등록차는 " , yearList.count(int(year)), "대입니다.")

#for 문 돌려서 해볼것.
count = 0
year = input("생산년도를 입력하세요.") # '2020'
for value in carDict.values():
    if value[0] == year :
        count = count +1

print(year, "의 등록차는 " ,  count, "대입니다.")
'''







'''
for key in carDict.keys():
    print(key, carDict[key])

for key,value in carDict.items():
    print(key,value)



print(carDict.items())
for item in carDict.items():
    print(item)

carDict.keys()
carDict.values()
carDict.items()
'''
'''
sport=['축구', '야구', '농구','배구']
num = [11,9,5,6]
dictionary = dict(zip(sport, num))
print(dictionary)
while 1:
    i = input("스포츠 경기를 입력하세요. 인원수를 알려줍니다.")
    if i == 'quit':
        print("너는 quit을 입력했다. 종료한다.")
        break
    if i in dictionary.keys():        #인원수 출력
        print("인원수: ", dictionary[i])
    else:
        print("다른 종목을 입력하셨습니다. 모릅니다.")
        continue    
    print("홍길동 님은 지금 ", i,"에 대한 정보를 서치하셨습니다.")

print("종료")
'''


# lambda 함수 작성하기
# map, filter

#입력 숫자 하나 받고,
#출력으로 숫자 +1  를 하는 함수

def addone(num) :
    return num + 1
print(addone(10))
#lambda 입력값: return값
print((lambda num : num + 1)(10))

#1. 숫자 두개 입력받아서, 합을 return 하는 함수
print((lambda n1, n2: n1+n2)(10,30))
def sum1(n1, n2):
    return n1 + n2

#2. 숫자 두개를 입력받아서 a,b  입력, a%b 를 출력하라.
print((lambda n1, n2 : n1%n2 )(100,3))
def cal(n1, n2):
    return n1%n2
'''
#map(), filter()랑 함께쓰이는 lambda
print((lambda num : num + 1)(10))
[20,22,23,24,25,26]
=> [21,23, 24,25, 26, 27]
map(function, 입력값 리스트)
'''
print(list(map(lambda num : num + 1, [20,22,23,24,25,26])))
list1 =[100,200,300,400]
list2 = [5,2,4,10]

#map(function, list1, list2)
#1. 숫자 두개 입력받아서, 합을 return 하는 함수
print(list(map(lambda n1, n2: n1+n2, list1, list2)))

#2. 숫자 두개를 입력받아서 a,b  입력, a%b 를 출력하라.
print(tuple(map(lambda n1, n2 : n1%n2, list1, list2)))
print(tuple(map(lambda n1, n2 : n1/n2, list1, list2)))

#3. filter를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
#filter(function, list)
print(filter(lambda x: x>0 , [1, -2, 3, -5, 8, -3]))
print(list(filter(lambda x: x>0 , [1, -2, 3, -5, 8, -3])))
  