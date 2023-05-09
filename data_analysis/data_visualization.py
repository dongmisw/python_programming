######################
#1) 관련 package, module impor하기 
######################



from matplotlib import pyplot as plt
import numpy as np



######################
# 2) 그래프 여러개를 하나의 그래프 좌표에 그리기
######################
plt.title("Sales comparison")
plt.xlabel('sales amount')
plt.ylabel('Company')

companies = ('company A', 'company B', 'company C', 'company D', 'company E')
sales = [10,2,4,5,6]
plt.barh(companies, sales, height=0.5 , color = 'yellow')
plt.bar(companies, sales)
plt.cla()
plt.plot([2,4,6,8],[2,4,6,8], label="label1")  
plt.plot([12,14,16,18],[12,14,16,18], color='red', marker='o', alpha=0.5, linewidth=2, label="label2")
plt.legend()  # legend를 나타내고 싶을때
 
#지우고 싶을때는 
#plt.cla() #기존에 plt 의 값을 지우고 싶을떄
plt.show() # 그래프를 그릴때
plt.cla()


######################
#3) 그래프 좌표 여러개 하나의 화면에 그리기
######################

x = np.array([1,2,3,4,5,6,7,8,9,10])
y1 = x*5
y2 = x*1
y3 = x*0.3
y4 = x*0.2

plt.subplot(1,2,1)
plt.plot(x,y1)
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.show()
 

plt.cla()
plt.subplot(2,2,1)
plt.plot(x,y1)
plt.subplot(2,2,2)
plt.barh(x,y2)
plt.subplot(2,2,3)
plt.bar(x,y3)
plt.subplot(2,2,4)
plt.pie(x)
plt.show()
