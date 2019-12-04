# class Point():
#     def getX(self):
#         return self.x
#
# point1 = Point()
# point2 = Point()
#
# point1.x = 5
# point2.x = 10
#
# # print(point1.x)
# # print(point2.x)
#
# print(point1.getX())

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

point1 = Point(4,6)
point2 = Point(2,3)

print(point1.getX())
print(point1.getY())