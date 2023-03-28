#0328.py
'''
print("hello")
print(3)
print(10.5)

print(type("hello"))
print(type(3))
print(type(10.5))
'''

'''
i,j,k = 3,5,"hello"
print(i,j,k)
3 = ii
print(ii)
'''
'''
# a += b
a = 100
b=5
a +=b  # a = a+b = 10 + 5 = 15
print("a +=b  :   a = ", a , "\n")

a = 100
b=5
a -= b
print("a -= b :  a = ", a, "\n")

a = 100
b=5
a *= b 
print("a *= b  :  a = ", a)
'''

'''
name = input("너의 이름은?")
print("저의 이름은 ",name, "입니다.")


year2class = input("2학년 몇반? ")
print("저는 " , year2class , "반 입니다.")
print(type(year2class))
'''
'''
age = input("나이는? ")
print("저는 " , age , "살 입니다.")
print(type(age))

print("우리 아빠는 저보다 30살 많은 ", int(age)+30,"살 이에요")
#int()
#float()
#str()


a=10
str_a = str(a)
print("type(a): " , type(a))
print("type(str_a) : " , type(str_a))

'''
'''
#str 
var = "python"
ch1 = var[0]
print(var[0] , "  ", var[1], "  " , var[2],  " ")
# p
print (var[0] ,  " : " , var[-6])
print("length of var : " , len(var))

print(var[15])

#print("PYTHON"[0] , "PYTHON"[2])

print('python'[5:0:-1])
print('python'[-1:-7:-1])

print("abcdef" + "\b" + "c")
print("hello\n world")
print("aaaaaa\vbbbbbbb\vccccc")
print("aaaaaa\'bbbbbbb\'ccccc")
print("aaaaaa\"bbbbbbb\"ccccc")
print('aaaaaa"bbbbbbb"ccccc')

'''

# string method
str_var ="하하하하"
#type(str_var)  => str
print(str_var.replace("하", "호"))

str_var2 = "안녕하세요.파이썬. 파이썬. 파이썬. 파이썬파이썬. 파이썬파이썬. 파이썬파이썬. 파이썬파이썬. 파이썬 수업입니다."
str_var3 = str_var2.replace("파이썬","자바")
str_var4 = str_var2.replace("파이썬","자바", 3)


print("str_var2 " ,str_var2)
print("str_var3 " , str_var3)
print("str_var4 ", str_var4)

'''
실수를 입력 받음.
102.345
102345  
1+0+2+3+4+5 
sum을 출력하라
'''

num_str = input("실수를 입력하나 하세요")
a = num_str.replace(".","")   # 102345

sum = int(a[0]) + int(a[1]) + int(a[2]) +int(a[3]) + int(a[4]) + int(a[5]) 

print("sum: " , sum )





