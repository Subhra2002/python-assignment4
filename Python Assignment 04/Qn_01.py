class Parent:
    def length(self):
        self.a = float(input("Enter the length of the triangle: "))
        self.b = float(input("Enter the length of the triangle: "))
        self.c = float(input("Enter the length of the triangle: "))
class Subclass(Parent):
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        print(area)

p = Subclass()
p.length()
p.area()
