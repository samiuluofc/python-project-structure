from models.geometry import Point
from business_logics.triangle import Triangle

p1 = Point(x=10, y=20)
p2 = Point(x=0, y=0)
p3 = Point(x=10, y=0)

print(p1, p2, p3)

t1 = Triangle(p1, p2, p3)
t1.show_points()
t1.area()


