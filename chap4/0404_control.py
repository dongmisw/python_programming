#0404
#제어문
#if문
'''
if 조건 :
    실행문1
else:
    실행문2   
'''
#오전? 오후
hour = 19
if hour<12 :
    print("12시가 지나지 않았으니까 오전이네요.")
elif hour<18 :
    print("12시가 지나고, 18시가 안지났으니 오후입니다.")
else :
    print("18시가 지나서 저녁입니다.")
'''
#장학금 
#       score < 200 50만원을 줌
# 200<= score < 400 100만원
# 400<= score < 500 10000만원.
# 
score_str = input("점수는? ")
score = int(score_str)
if score < 200 :
    print("50만원 획득")
elif score < 400:
    print("100만원 획득")
else :
    print("1000만원 획득")
'''
'''
# 점심식사
answer = input("서브웨이 먹을래? 먹고싶으면 yes로 쓰세요.")
if answer=='yes' :
    print("8호관 1층")
else :
    again_answer = input("학식?")
    if again_answer =='yes':
        print("8호관 3층")
    else :
        print("먹지마세요.")
'''

#반복문 
#for 
#for(int i =0 ; i<5 ; i++){
#    print("ahahhah")
#}

'''

for i in 1,3,4,5,6,8 :
    print(i)

# 0,1,2,3....10 
print("range1 ")
for i in range(0,11,1) :
    print(i)

print("range2 ")
for i in range(11) :
    print(i)

#1부터 10까지 합을 구하시오.
sum = 0 
i=3
for i in range(11) :
    sum = sum + i
    print(i, " 번째 sum은 ", sum)
    #sum += i
else:
   print("for문의 조건이 더이상 만족하지 않습니다. ")
   print("i가 range(11)에서 벗어남. ") 
   print("for 문이 break나 continue로 종료된게 아니라 정상종료시에만 실행")

print("sum : " , sum )



'''

'''
while 조건:
    수행문   
'''
i = 10
while i>5 :
    print(i ," 는 5보다 크다.")
    i = i-1

#n=1부터 5까지 찍어보는 프로그래밍
# 1 2 3 4 5
i = 1 
while i <= 5 :
    print(i, end= '   **  ')    
    i = i + 1
else:
    print("while이 잘 끝남")
    print("현재 i의 값은 ", i, "입니다")











#놀이기구 탑승 
#4명 탑승 가능 , 5명은 안되요.
#키 150이상 사람만 탑승가능
#입력을 키를 받음
# 탑승인원 체크, 키 체크, 
# while문을 끝내는 조건은? 사람이 4명을 채웠는가?
'''
while 5명이아닐것 :
    150이 넘는가? 
    - yes: 
    - no: 
else:
    4명 다 탔습니다. 놀이기구 출발
'''
'''
people = 0 
while people<4 :
    height = input("키는?")
    int_height = int(height)
    if int_height>150 :
        people = people +1
        print("한명 더 탑승")
        print("현재 인원 : " , people)
    else:
        print("못타요")
else:
    print("완료.놀이기구 시작")

'''

# continue , break
# 반복문 중간에 반복을 더이상 하지 않고 실행을 종료
# 반복문 안쪽에서 실행된다.
# 주로 if문 안쪽에서 사용됨
#
 

'''
while True :
    str = input("단어를 넣으세요.")
    if str=="exit" :
        print("넌 exit을 입력했다. 종료한다.")
        break
    else:
        if str=="apple":
            print("apple을 입력받았음")
            print("continue실행함")
            continue
        print("넌 이 단어를 입력했다.  ", str)
    
    print(str, " 저는 아직 while안에 있어요.")


print("while이 종료됨")

'''
# input으로 입력을 받는데, 
# 무한반복. 
# exit이라는 값을 받으면, 입력받는것을 종료.
# apple을 받으면. "apple을 입력했다."" 하고 다시 입력받기
# 그 외의 단어를 입력받으면,해당 단어를 3번 찍어줄것. 
# continue, break를 활용해서 해본다.






















