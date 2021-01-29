class student:
    def __init__(self,name,grade,number):
        self.name = name
        self.grade = grade
        self.number = number
        
    def __repr__(self):
        return repr((self.name, self.grade, self.number))
    
students = [
        student('홍길동',3.9,20165232),
        student('김범수',3.0,20165231),
        student('김지쿡',4.3,20165230),
        ]
b=sorted(students,key=lambda student:student.number)
print(b)
    