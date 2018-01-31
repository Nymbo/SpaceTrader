import math

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Vector2(self.x, self.y)
        result.x += other.x
        result.y += other.y
        return result

    def __sub__(self, other):
        result = Vector2(self.x, self.y)
        result.x -= other.x
        result.y -= other.y
        return result

    def __mul__(self, val):
        result = Vector2(self.x, self.y)
        result.x *= val
        result.y *= val
        return result

    def __truediv__(self, val):
        result = Vector2(self.x, self.y)
        result.x /= val
        result.y /= val
        return result

    # Clockwise rotation
    def rotate(self, angle):
        rads = math.radians(-angle)
        x = self.x * math.cos(rads) - self.y * math.sin(rads)
        y = self.x * math.sin(rads) + self.y * math.cos(rads)

        self.x = x
        self.y = y

    def length(self):
        l = math.sqrt(self.x ** 2 + self.y ** 2)
        return l

    def normalize(self):
        l = self.length()
        self.x = self.x  / l
        self.y = self.y  / l
        return self

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist
    
if __name__ == "__main__":
    v1 = Vector2(0,1)
    print v1.x, v1.y
    v1.rotate(45)
    print v1.x , v1.y
    v2 = Vector2(1,1)
    print v2.length()
    v2.normalize()
    print v2.length()
    
