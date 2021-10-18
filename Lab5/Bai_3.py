class Member:
    def __init__(self, name: str, phone: int, email: str) -> None:

        self.name = name
        self.phone = phone
        self.email = email
    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.phone,self.email)

class Student(Member):
    def __init__(self, name: str, phone: int, email: str,student_id: int) -> None:
        super().__init__(name, phone, email)
        self.student_id = student_id
     
    def __str__(self):
        return "Student Name: {0} \nPhone Number : {1} \nEmail : {2} \nStudent_ID : {3}".format(self.name,self.phone,self.email,self.student_id)

    def __repr__(self):
        return "{0}({1},{2},{3},{4})".format(self.__class__.__name__,self.name,self.phone,self.email,self.student_id)


class Faculty(Student):
    def __init__(self, name: str, phone: int, email: str,student_id: int,learning_id: int,learning_name: str) -> None:
        super().__init__(name, phone, email,student_id)
        self.learning_id = learning_id
        self.learning_name = learning_name


    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5},{6})".format(self.__class__.__name__,self.name,self.phone,self.email,self.student_id,self.learning_id,self.learning_name)

    def __str__(self):
        return "Student Name: {0} \nPhone Number : {1} \nEmail : {2} \nStudent_ID : {3} \nLearning_id : {4} \nLearning_name : {5}".format(self.name,self.phone,self.email,self.student_id,self.learning_id,self.learning_name)

HoangViet = Student('PhamHoangViet',545,'phamviet@gmail.com',14146)
print(HoangViet)
print('*********')
NgocMinh = Faculty('Le Ngoc Hong Minh',789456,'minhminh@gmail.com',14147,46453,'Meachine Learning')
print(NgocMinh)

