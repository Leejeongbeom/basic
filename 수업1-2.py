print("숫자게임에 오신것을 환영합니다.")
a='40'
while a!='76':
    a=input("1부터 100사이의 숫자를 추측해보세요:")
    if a<'76':
        print("정답보다 작습니다")
    else: 
        if a>'76':
            print("정답보다 큽니다")
        else:
            print("정답입니다")
print("게임을 종료합니다")

