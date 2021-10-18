class Nematode:
    def __init__(self,name: str,height: float, sex: str,age: int) -> None:
        self.name = name
        self.height = height
        self.sex = sex
        self.age = age
    
    def __str__(self):
        return "C. elegans: \nName : {} \nHeight : {}\nGender : {}\nAge :{}".format(self.name,self.height,self.sex,self.age)
    
    def __repr__(self):
        return "{0}({1},{2},{3},{4})".format(self.__class__.__name__,self.name,self.height,self.sex,self.age)
Robin = Nematode('Robin',1.12,'Male',12)

print(Robin)
