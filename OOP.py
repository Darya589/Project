"""class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, a):
        return Vector (self.x + a.x, self.y + a.y)
    
V1 = Vector(1, 2)
V2 = Vector(3, 4)
s = V1 + V2
print(s.x, s.y)"""

class Count:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
    def __str__(self):
        return "Привет"
A = Count()
print(A())
print(A())
print(A)