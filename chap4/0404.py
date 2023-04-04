#0404

str = "파이썬은 하하하 호호호 히히히 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 "
newnewstr = "파이썬은,하하하, 호호호 ,히히히, 파이썬은, 파이썬은, 파이썬은, 파이썬은 파이썬은 파이썬은 파이썬은 "
'''
print(2,"+",3,"=",5)
print('{}+{}={}'.format(2,3,5))

a,b=5,10.000
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f},{3:s}'.format(a,b,a+b,"hdhdh"))


#print('{2}+{0}={1}'.format(a,b,a+b))
'''
'''
print(newnewstr.split(","))

print(str.find("자바"))
#print(str.index("자바"))


print(str.find("파이썬"))
print(str.find("파"))
print(str.find("썬"))
print(str.index("파이썬"))
print(str.index("파"))
print(str.index("썬"))


'''
'''
newstr = str.replace("파이썬", "자바")
print("str: " , str )
print("newstr : " ,newstr)

print("str.count('파이썬')", str.count("파이썬"))
print('->'.join(str))
'''
'''
value = False #True
print(type(value))
print(int(value))

print(bool(0), bool(1), bool(1.1222), bool(-12))
print(bool("dssdfsfd"),bool("-1"),bool(""))
print( 'bool("") ',bool(""))

'''












