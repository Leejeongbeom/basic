class counter:
    def reset(self):
        self.count = 0
    def increment(self):
        self.count +=1
    def get(self):
        return self.count

a=counter()
b=counter()

a.reset()
b.reset()

a.increment()
b.increment()
print("카운터 a의 값은", a.get())
print("카운터 b의 값은", b.get())