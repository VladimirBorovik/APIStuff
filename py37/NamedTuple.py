from typing import NamedTuple


class PointDataClass(NamedTuple):

    x: float = 0.1
    y: float = 0.2
    z: float = 0.3

    def __str__(self):
        return "{0}, {1}, {2}".format(self.x, self.y, self.z)


nt = PointDataClass(2, 3, 4)
print(nt.z)
print(x._replace(x = 10))



