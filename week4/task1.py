"""
Point3D
"""

from dataclasses import dataclass


@dataclass
class Point3D:

    x: float
    y: float
    z: float

    def __repr__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z)

    def distance_to(self, p2: 'Point3D') -> float:
        return ((p2.x - self.x)**2 + (p2.y - self.y)**2 + (p2.z - self.z)**2)**0.5


if __name__ == '__main__':
    point1 = Point3D(1.5, 2.2, -3.8)
    point2 = Point3D(3, 4, 5)
    print(point1, point2)
    print(point1.distance_to(point2))
    # tests
    assert Point3D(0, 0, 0).distance_to(Point3D(0, 0, 0)) == 0
    assert round(Point3D(-1.0, 23.3, -3.5).distance_to(Point3D(2.3, 23.3, 0)), 2) == 4.81
    assert round(Point3D(10, 10, 0).distance_to(Point3D(10, 0, 0)), 2) == 10
    assert round(Point3D(10.2, 10, 32).distance_to(Point3D(9.4, 12, 0)), 2) == 32.07
    print("All tests passed")
