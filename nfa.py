"""
TODO: Secret message encrypted.
"""
import random
from enum import Enum


class RGB:
    value_min = 0
    value_max = 255

    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

    def __repr__(self):
        return f"({self.r}, {self.g}, {self.b})"

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        if self.value_validate(r):
            self._r = r

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, g):
        if self.value_validate(g):
            self._g = g

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if self.value_validate(b):
            self._b = b

    @classmethod
    def value_validate(cls, value):
        return cls.value_min <= value <= cls.value_max


class Algorithm:
    name = NotImplemented

    def __repr__(self):
        return f"{self.name}"

    def yield_next(self, rgb_input: RGB):
        return self._calculate(rgb_input)

    def _calculate(self, rgb_input):
        raise NotImplemented


class Alpha(Algorithm):
    """Based on previous RGB."""
    name = "alpha"
    delta = 1

    def _calculate(self, rgb_input):
        rgb_output = RGB(
            r=rgb_input.r,
            g=rgb_input.g,
            b=rgb_input.b,
        )

        parameter_to_update = random.choice(["r", "g", "b"])
        delta = self.delta * random.choice([1, -1])

        if parameter_to_update == "r":
            rgb_output.r += delta
        elif parameter_to_update == "g":
            rgb_output.g += delta
        elif parameter_to_update == "b":
            rgb_output.b += delta

        return rgb_output


class Beta(Algorithm):
    """Based on surrounding RGBs."""
    name = "beta"

    def _calculate(self, rgb_input):
        raise NotImplemented


class RGBUpdater:
    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm


class Size:
    size_default = 256

    def __init__(self, x_max: int = None, y_max: int = None):
        self.x_max = x_max or self.size_default
        self.y_max = y_max or self.size_default

    def __repr__(self):
        return f"({self.x_max}, {self.y_max})"


class RelativeLocation(Enum):
    """Relative to axis' max value."""
    bottom_left = (0, 0)
    top_left = (0, 1)
    bottom_right = (1, 0)
    top_right = (1, 1)
    center = (0.5, 0.5)

    def __repr__(self):
        return f"{self.name}"

    @property
    def x_value(self):
        return self.value[0]

    @property
    def y_value(self):
        return self.value[1]


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def from_relative_location(cls, relative_location: RelativeLocation, x_max, y_max):
        return cls(
            relative_location.x_value * x_max,
            relative_location.y_value * y_max,
        )


class Heading:
    full_circle = 360
    value_min = 0
    value_max = 359

    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return f"{self._value}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        while self._value > self.value_max:
            self._value -= self.full_circle
        while self._value < self.value_min:
            self._value += self.full_circle


class Pattern(Enum):
    horizontal = "horizontal"
    vertical = "vertical"
    diagonal_1 = "diagonal_1"  # TODO: check if there is any standard
    diagonal_2 = "diagonal_2"
    concentric_circular = "concentric_circular"
    concentric_triangular = "concentric_triangular"
    concentric_squared = "concentric_squared"
    spiral = "spiral"


class Config:
    def __init__(
            self,
            canvas_size: Size,
            relative_location_start: RelativeLocation,
            heading_start: Heading,
            pattern: Pattern,
            rgb_seed: RGB,
            algorithm: Algorithm,
    ):
        self.canvas_size = canvas_size
        self.relative_location_start = relative_location_start
        self.heading_start = heading_start
        self.pattern = pattern
        self.rgb_seed = rgb_seed
        self.algorithm = algorithm

    def __repr__(self):
        return (
            f"Size: {self.canvas_size}",
            f"Start: {self.relative_location_start}",
            f"Heading: {self.heading_start}",
            f"Pattern: {self.pattern}",
            f"RGB seed: {self.rgb_seed}",
            f"Algorithm: {self.algorithm}",
        )


class Canvas:
    """Origin (0, 0) is bottom-left corner."""

    def __init__(self, size: Size):
        self.size = size
        self.pixels = [
            [None for _ in range(self.size.x_max)]
            for _ in range(self.size.y_max)
        ]

    def insert_rgb_to_pixel(self, coordinates: Coordinates, rgb: RGB):
        self.pixels[coordinates.y][coordinates.x] = rgb


class Engine:
    def __init__(self, config: Config):
        self.canvas = Canvas(config.canvas_size)
        self.coordinates_start = Coordinates.from_relative_location(
                config.relative_location_start,
                x_max=self.canvas.size.x_max - 1,
                y_max=self.canvas.size.y_max - 1,
            )
        self.heading = config.heading_start
        self.pattern = config.pattern
        self.rgb_seed = config.rgb_seed
        self.algorithm = config.algorithm
        self.rgb_array = [self.rgb_seed]

    def generate_rgb_array(self):
        # TODO: this only works with sequential algorithms (such as alpha)
        for _ in range(self.canvas.size.x_max * self.canvas.size.y_max):
            self.rgb_array.append(
                self.algorithm.yield_next(self.rgb_array[-1]),
            )

    def paint_canvas(self):
        # TODO:
        return self.canvas


class ArtPieceSignature:
    def __init__(self, series: str, units_total: int, unit_number: int):
        self.series = series
        self.units_total = units_total
        self.unit_number = unit_number  # TODO: check if there is a standard name

    def __repr__(self):
        return (
            f"Series: {self.series}",
            f"Unit: {self.unit_number}/{self.units_total}",
        )


class ArtPiece:
    def __init__(self, signature: ArtPieceSignature, canvas: Canvas):
        self.signature = signature
        self.canvas = canvas

    def generate(self):
        ...
