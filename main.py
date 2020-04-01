from ecosystem import River, SizeError


class RiverSimulator:

    def __init__(self):
        self._river = None
        self.options = {
            "generate": self.generate,
            "river": self.show_river,
            "stats": self.stats,
            "add": self.add_animal,
            "advance": self.advance,
            "fast advance": self.fast_advance,
            "quit": self.quit
        }

    def run(self):
        while True:
            print("""
generate\tGenerate a new river for you to play with.
river\tShow the contents of your current river.
stats\tSee the current number of animals in your river.
add\tAdd an animal to your river.
advance\tSimulate one stage (day, month, year) or your river.
fast advance\tAdvance multiple times in one command!
quit\tQuit the simulator.
""")
            command = input("> ")

            if command in self.options:
                action = self.options[command]
                action()
            else:
                print("Invalid command.")

    def generate(self):
        size = input("What is the size of your river?\n")
        num_bears = input("The number of bears: ")
        num_fishes = input("The number of fishes: ")
        try:
            self._river = River(int(size), int(num_bears), int(num_fishes))
        except SizeError as err:
            print(err)
        except ValueError:
            print("Invalid river parameters.")
        else:
            print("New river environment generated!")

    def show_river(self):
        if self._river is None:
            print("You haven't generated a river yet. Type 'generate' to do so.")
        else:
            print(self._river)

    def stats(self):
        if self._river is None:
            print("You haven't generated a river yet. Type 'generate' to do so.")
        else:
            print(f"""
Your river has:
{self._river.total_animals("bear")} bears,
{self._river.total_animals("fish")} fishes.
""")

    def add_animal(self):
        if self._river is None:
            print("You haven't generated a river yet. Type 'generate' to do so.")
        else:
            idx = input("Enter the position (starting from 0): ")
            animal_type = input("Enter the animal type (fish/bear): ")
            if idx.isdigit():
                self._river.add(int(idx), animal_type)
            else:
                print("Invalid position.")

    def advance(self):
        if self._river is None:
            print("You haven't generated a river yet. Type 'generate' to do so.")
        else:
            self._river.advance()

    def fast_advance(self):
        if self._river is None:
            print("You haven't generated a river yet. Type 'generate' to do so.")
        else:
            times = input("How many times would you like to advance?\n")
            if times.isdigit():
                self._river.fast_advance(int(times))
            else:
                print("Invalid number of advances.")

    def quit(self):
        raise SystemExit


if __name__ == '__main__':
    RiverSimulator().run()
