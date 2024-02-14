class Crug:
    def __init__(self,radius):
        self.radius = radius
    
    def __add__(self,other):
        return Crug(self.radius + other.radius)

    def __mul__(self,other):
        return Crug(self.radius * other.radius)

    def __truediv__(self,other):
        return Crug(self.radius / other.radius)

    def __sub__(self,other):
        return Crug(self.radius - other.radius)

    def __str__(self):
        return str(self.radius)


x = Crug(10)
y = Crug(2)
print(x+y)
print(x*y)
print(x+y)
print(x+y)
# sub mul truediv add
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")
print("hellow")