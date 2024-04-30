print('Welcome Advanced programming')


class BirdSpecies:

    def __init__(self, name, habitat,wing_span):
        self.name = name
        self.habitat = habitat
        self.wing_span = wing_span
    
    def describe(self):
        return f'name: {self.name}\thabitat: {self.habitat}\twing_span: {self.wing_span}'


class Eagle (BirdSpecies):
    def __init__(self, name, habitat, wing_span, specie):
        super().__init__(name, habitat, wing_span)
        self.specie = specie

    def to_prey (self, prey):
        return f'this {self.specie} {self.name} is preying a/an {prey} '


def main():
    print("Main")
    bird = BirdSpecies("Eagle", "Mountains", 15)
    print(bird.describe())

    bald_eagle = Eagle("eagle", "mountains", 15, "bald")
    print(bald_eagle.to_prey("trout"))


if __name__ == "__main__":
    main()
