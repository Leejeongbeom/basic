f = open("students.txt","r", encoding = 'utf8')

for line in f.readlines():
    
    line = line.strip()
    
    print(line)
    
    words = line.split(",")
    
    for word in words:
        print("   ",word)