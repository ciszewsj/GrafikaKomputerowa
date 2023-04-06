import random

from shapes.line import Line


class Polygon:
    def __init__(self, line_list=[], color=None):
        self.line_list = line_list
        self.color = color

    def __find_min(self, xyz: int) -> int:
        min_z = None
        for line in self.line_list:
            line: Line = line
            if min_z is None:
                min_z = min(line.a[xyz], line.b[xyz])
            else:
                min_z = min(min(line.a[xyz], line.b[xyz]), min_z)
        return min_z

    def __find_max(self, xyz: int) -> int:
        max_z = None
        for line in self.line_list:
            line: Line = line
            if max_z is None:
                max_z = max(line.a[xyz], line.b[xyz])
            else:
                max_z = max(max(line.a[xyz], line.b[xyz]), max_z)
        return max_z

    def __find_midpoint(self) -> [int, int, int]:
        return (self.__find_max(xyz=0) + self.__find_min(xyz=0)) / 2.0, \
               (self.__find_max(xyz=1) + self.__find_min(xyz=1)) / 2.0, \
               (self.__find_max(xyz=2) + self.__find_min(xyz=2)) / 2.0

    def change_line_order(self):
        new_polygon = Polygon([], color=self.color)
        last_point = None
        i = 0
        for line in self.line_list:
            line: Line = line
            if i == 0:
                if self.line_list[0].b == self.line_list[1].a or self.line_list[0].b == self.line_list[0].b:
                    new_polygon.line_list.append(line)
                else:
                    new_polygon.line_list.append(Line(self.line_list[i].b, self.line_list[i].a))
            else:
                if self.line_list[i].a == last_point:
                    new_polygon.line_list.append(line)
                else:
                    new_polygon.line_list.append(Line(self.line_list[i].b, self.line_list[i].a))
            last_point = new_polygon.line_list[i].b
            i += 1
        return new_polygon

    def distance(self) -> int:
        centroid = self.__find_midpoint()
        return int(centroid[0] ** 2 + centroid[1] ** 2 + centroid[2] ** 2)
