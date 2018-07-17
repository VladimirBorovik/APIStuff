from dataclasses import dataclass, _MISSING_TYPE, _DataclassParams, Field


@dataclass(order=True, frozen=True)
class PointDataClass:

    x: float = 0.1
    y: float = 0.2
    z: float = 0.3

    def __str__(self):
        return "{0}, {1}, {2}".format(self.x, self.y, self.z)

  #  __dataclass_params__ = _DataclassParams(
  #      frozen=False)
  #
  #  __dataclass_fields = {
  #      'x': Field(default=_MISSING_TYPE,
  #                 metadata={})
  # # }


#dc1, dc2 = PointDataClass(), PointDataClass(1.0, 2.0, 3.0)
#print(dc1, " | ", dc2)

nt = PointDataClass(2, 3, 4)
print(nt.z)
print(PointDataClass.__annotations__)



