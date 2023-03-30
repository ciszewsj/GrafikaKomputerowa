import numpy as numpy
import pygame.draw
from pygame import Surface

from shapes.line import Line


class Cube:
    def __init__(self, xd, xy, xz, color, distance_from_camera, distance_between_points):
        self.line_list = []
        self.point_list = []
        self.polygon_list = []
        self.distance_from_camera = distance_from_camera
        self.distance_between_points = distance_between_points

        self.color = color

        self.__init_point_list(xd, xy, xz)
        self.__init_lines()

    def __init_point_list(self, xd, xy, xz):
        d = self.distance_between_points / 2.0
        self.point_list.append(
            [numpy.float64(-d) + xd, numpy.float64(-d) + xy, numpy.float64(self.distance_from_camera + d) + xz])
        self.point_list.append(
            [numpy.float64(-d) + xd, numpy.float64(d) + xy, numpy.float64(self.distance_from_camera + d) + xz])
        self.point_list.append(
            [numpy.float64(d) + xd, numpy.float64(d) + xy, numpy.float64(self.distance_from_camera + d) + xz])
        self.point_list.append(
            [numpy.float64(d) + xd, numpy.float64(-d) + xy, numpy.float64(self.distance_from_camera + d) + xz])

        self.point_list.append(
            [numpy.float64(- d) + xd, numpy.float64(-d) + xy, numpy.float64(self.distance_from_camera + 3 * d) + xz])
        self.point_list.append(
            [numpy.float64(-d) + xd, numpy.float64(d) + xy, numpy.float64(self.distance_from_camera + 3 * d) + xz])
        self.point_list.append(
            [numpy.float64(d) + xd, numpy.float64(d) + xy, numpy.float64(self.distance_from_camera + 3 * d) + xz])
        self.point_list.append(
            [numpy.float64(d) + xd, numpy.float64(-d) + xy, numpy.float64(self.distance_from_camera + 3 * d) + xz])

    def __init_lines(self):
        for i in range(0, 3):
            self.line_list.append(Line(self.point_list[i], self.point_list[i + 1]))
            self.line_list.append(Line(self.point_list[i + 4], self.point_list[i + 5]))
            self.line_list.append(Line(self.point_list[i], self.point_list[i + 4]))

        self.line_list.append(Line(self.point_list[0], self.point_list[3]))
        self.line_list.append(Line(self.point_list[4], self.point_list[7]))
        self.line_list.append(Line(self.point_list[3], self.point_list[7]))

    def draw_points(self, screen: Surface):
        pygame.draw.circle(screen, (200, 0, 0), (150.0, 75.0), 20)
        for point in self.point_list:
            print(point[0], point[1])
            pygame.draw.circle(screen, (200, 0, 0), (point[0], point[1]), 1)
