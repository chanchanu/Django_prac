print(type([]))
# <class 'list'> 라고 출력되는데
# 즉, class 파이썬은 모든것이 객체로 설정된다
#--------------------------------------------

class sample():
    pass
x = sample()
print(type(x))
# <class '__main__.sample'> 직접 만든 class
#---------------------------------------------

class Dog():
    # CLASS OBJECT ATTRIVUTE
    species = "mammal"
    # 초기화
    def __init__(self, breed,name):
        self.breed = breed
        self.name = name
#mydog = Dog(breed = "Lab", name="Sammy")   이게 기본 원리
mydog = Dog("Lab","Sammy")                 #이건 약식
print(mydog.breed)      #Lab
print(mydog.name)       #Sammy
print(mydog.species)    #mammal
