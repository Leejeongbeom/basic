def process(w):
    output = ""
    for ch in w:
        if(ch.isalpha()):
            output += ch
    return output.lower()

words = set()
fname = input("입력 파일 이름:")
file = open(fname,"r")

for line in file:
    linewords = line.split()
    for word in linewords:
        words.add(process(word))
        
print("사용된 단어의 개수=", len(words))
print(words)