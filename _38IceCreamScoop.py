class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops():
    scoops = [Scoop('chocolate'),
                Scoop('vanilla'),
                Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)

if __name__ == '__main__':
    create_scoops()