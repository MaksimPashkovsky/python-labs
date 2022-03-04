from dataclasses import dataclass


@dataclass
class Point3D:

    x: int
    y: int
    z: int

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

    def distance_to(self, p2: 'Point3D'):
        return ((p2.x - self.x)**2 + (p2.y - self.y)**2 + (p2.z - self.z)**2)**0.5


if __name__ == '__main__':
    point1 = Point3D(1, 2, 3)
    point2 = Point3D(3, 4, 5)
    print(point1, point2)
    print(point1.distance_to(point2))
