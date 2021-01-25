print("숫자게임에 오신 것을 환영합니다")
number = 62
s=input("1부터 100사이의 숫자를 추측해보세요:")
guess = int(s)
while guess != number:
    s=input("1부터100사이의 숫자를 추측해보세요:")
    guess = int(s)
print("게임이 종료되었습니다")