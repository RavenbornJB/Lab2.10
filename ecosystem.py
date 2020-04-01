import random
from animals import Bear, Fish


class SizeError(ValueError):
    pass


class River:

    def __init__(self, size, num_bears, num_fishes):
        self.size = size
        self._elements = self.generate(size, num_bears, num_fishes)

    def __str__(self):
        return "|" + "".join([" " if el is None else repr(el)
                              for el in self._elements]) + "|"
        # return str(self._elements)

    @staticmethod
    def generate(size, num_bears, num_fishes):
        lst = [None] * size
        if num_fishes + num_bears > size:
            raise SizeError("Number of animals must be smaller than the size.")
        indexes = random.sample(range(size), num_bears + num_fishes)
        for i in indexes[:num_bears]:
            lst[i] = Bear()
        for i in indexes[num_bears:]:
            lst[i] = Fish()
        return lst

    @staticmethod
    def animal_by_type(animal_type):
        if animal_type == "fish":
            return Fish()
        elif animal_type == "bear":
            return Bear()
        else:
            return None

    def total_animals(self, animal_type):
        return len([animal for animal in self._elements
                    if animal is not None and animal.name == animal_type])

    def add(self, idx, animal_type):
        if self._elements[idx] is not None or idx > self.size - 1:
            return

        if animal_type == "fish":
            self._elements[idx] = Fish()
        if animal_type == "bear":
            self._elements[idx] = Bear()

    def move(self, idx, animal_type, direction):
        new_pos = idx + direction
        if new_pos < 0 or new_pos > self.size - 1 or direction == 0:
            return

        inhabitant = self._elements[new_pos]
        if inhabitant is None:
            self._elements[idx] = None
            self.add(new_pos, animal_type)
        elif inhabitant.name != animal_type:
            self._elements[idx] = None
            self._elements[new_pos] = None
            self.add(new_pos, "bear")
        elif None in self._elements:
            empty_pos = self._elements.index(None)
            self._elements[empty_pos] = self.animal_by_type(animal_type)

    def advance(self):
        for idx, animal in enumerate(self._elements):
            if animal is not None:
                direction = random.randint(-1, 1)
                self.move(idx, animal.name, direction)

    def fast_advance(self, times):
        for time in range(times):
            self.advance()


if __name__ == '__main__':
    r = River(10, 2, 6)
    print(r)
    r.fast_advance(5)
