# Avatar generator, by eBLDR
import random
import uuid
from PIL import Image


class Avatar:
    def __init__(self, size=5, symmetric=False, save_file=False):
        self.size = size
        self.symmetric = symmetric
        self.save_file = save_file
        self.array = Array(size=size, symmetric=symmetric)
        self.image = Canvas(unit_size=size)
    
    def generate(self):
        self.array.generate_array()
        self.image.fill_canvas(self.array.values)
        if self.save_file:
            self.save()
    
    def display(self):
        self.image.canvas.show()
    
    def save(self):
        self.image.canvas.save('avatar_{}.png'.format(str(uuid.uuid4())), 'PNG')


class Array:
    def __init__(self, **kwargs):
        self.values = []
        self.size = kwargs.get('size', 5)
        self.symmetric = kwargs.get('symmetric', False)
        if self.symmetric:
            assert self.size % 2 != 0, 'Only odd numbers for symmetric mode - it looks cooler.'
    
    def generate_array(self):
        white_color = (255, 255, 255)
        color = self.get_random_rgb_color()
        if self.symmetric:
            array = []
            for j in range(self.size):
                row = []
                for i in range(self.size):
                    if i <= (self.size - 1) / 2:
                        if random.randint(0, 1) == 1:
                            row.append(color)
                        else:
                            row.append(white_color)
                    else:
                        row.append(row[self.size - i - 1])
                array.append(row)
            self.values = array
        else:
            self.values = [[color if random.randint(0, 1) == 1 else white_color for c in range(self.size)] for r in range(self.size)]
    
    def get_random_rgb_color(self):
        color = tuple()
        for i in range(3):
            color += (self.get_random_value(),)
        return color
    
    @staticmethod
    def get_random_value(max_=255):
        return random.randint(0, max_)


class Canvas:
    def __init__(self, unit_size):
        self.pixels_per_unit_size = 50
        self.pixels = self.pixels_per_unit_size * unit_size
        self.canvas = Image.new('RGB', (self.pixels, self.pixels))
    
    def fill_canvas(self, array_of_rgb_values):
        for i in range(len(array_of_rgb_values)):
            for j in range(len(array_of_rgb_values[i])):
                for x in range(self.pixels_per_unit_size):
                    for y in range(self.pixels_per_unit_size):
                        self.canvas.putpixel((x + self.pixels_per_unit_size * j, y + self.pixels_per_unit_size * i), array_of_rgb_values[i][j])


if __name__ == '__main__':
    avatar = Avatar(symmetric=True, size=5, save_file=False)
    avatar.generate()
    avatar.display()
