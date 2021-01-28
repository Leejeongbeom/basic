short = {'B4':'Before', 'TX':'Thanks','BBL':"Be Back Later",'BCNU':"Be Seeing You",'HAND':"Have A Nice Day"}
a=input("번역할 문장을 입력하시오: ")
words = a.split()
print(short.get(a))