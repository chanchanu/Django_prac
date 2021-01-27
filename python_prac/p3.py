class Circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * Circle.pi
        # 그냥 radius 하면 에러 뜸
        # 그냥 pi 쓰면 에러 뜸
    
    def set_radius(self, new_r):
        self.radius = new_r
circle = Circle(3)
circle.radius = 10  # 이건 직접 접근
circle.set_radius(100)  # 이건 간접 접근
print(circle.area())