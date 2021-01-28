def fib(n):
    a,b=0,1
    while b<n:
        print(b,end='')
        a,b=b,a+b
    print()
    
print('fibo.py__name__:',__name__)
fib(1000)