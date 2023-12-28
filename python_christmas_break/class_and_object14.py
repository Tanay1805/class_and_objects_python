import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

if __name__ == "__main__":
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)

    distance = point1.calculate_distance(point2)


    print(f"Euclidean Distance between ({point1.x}, {point1.y}) and ({point2.x}, {point2.y}): {distance}")
