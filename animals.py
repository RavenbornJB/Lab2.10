class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name[0]


class Bear(Animal):

    def __init__(self):
        super().__init__("bear")


class Fish(Animal):

    def __init__(self):
        super().__init__("fish")


if __name__ == '__main__':
    f = Fish()
    test = type(f)
    print(repr(test))
