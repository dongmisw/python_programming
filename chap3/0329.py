#0329
'''
print("안녕하세요.")
print(3)
print(10.6)

var = "안녕"
print(var)
print(type(var))
print(type(3))

var1 = 3
_var = 10
height = 180
weight = 50
length_list = 
'''
'''

a,b = 100,10
a *= b   
print("a*=b : ",  a)

a,b = 100,10
a /= b   
print("a/=b : ",  a)

a,b = 100,10
a -= b   
print("a-=b : ",  a)
'''
'''

name = input("이름이 뭔가요?")
print("제 이름은", name, "입니다.")
age = input("나이는?")
print("나이는", age, "입니다.")  # "20"   , int("20")
print("아버지 나이는 ", int(age) +30, "입니다.")
print(type(age))
'''


#int("30")
#float("20.6")
#str(30)

#a= "python"
'''
a ="동양미래대학교"
print(a[0], "  ",  a[1], "..." , a[5]) #p y n
print("python"[0], "... ", "python"[1], " ..." , "python"[5])
print("동양미래대학교"[8])
print(len(a))
'''
'''
school = "동양미래대학교-컴퓨터소프트웨어공학과"
print("school[::-1] : "   , school[::-1])
print("school[::] : "   , school[::]) #동양미래대학교-컴퓨터소프트웨어공학과
print("school[0:len(school):2] : " ,school[0:len(school):2]) #동미대교컴....
print("school[8:len(school):2] : ", school[8:len(school):2])#컴터프웨공과
print("school[8:len(school)] : ", school[8:len(school)]) #컴퓨터소프트웨어공학과
print("school[:15:4]  : ", school[:15:4])
#동양미래대학교-컴퓨터소프트웨어  4칸씩 뛰기.동대컴프

'''

'''
school="동양미래대학교"
print("school[:] : "   , school[:]) #동양미래대학교
print("school[0:3] : " ,school[0:3]) #동양미
print("school[1:4] : ", school[1:4])#양미래
print("school[2:4] : ", school[2:4]) #미래
print("school[1:]  : ", school[1:])#양미래대
 

print('동양미래대학교'[5:0:-1])
print('동양미래대학교'[-1:-7:-1])


print("hello \n world")
print("hello \t world")
print("hello\bworld")
print("hello\vworld")
'''

str_a= "하하하"
#str_b = "호호호"
print(type(str_a))
str_a.replace("하", "호")
print(str_a.replace("하", "호"))
str_a = str_a.replace("하", "호",2)
print("str_a: ", str_a)
#print("str_b: ", str_b)

str_c = "안녕하세요. 파이썬 수업입니다. 파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬."
print(str_c.replace("파이썬","자바", 5))

'''
#입력: 6자리 실수    222.788
#출력: 실수의 각 자리의 합을 출력한다.  2+2+2+7+8+8  => ??
#input(), int(), str.replace()
'''
num = input(" 실수를 입력하세요")   #212.222
num = num.replace(".","")   # 213456 -> str
print("sum : " ,int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])+ int(num[4])+ int(num[5]))






 




