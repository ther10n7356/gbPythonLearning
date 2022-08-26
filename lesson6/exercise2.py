class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass_of_asphalt(self, mass_asphalt, depth_asphalt):
        mass_of_asphalt = self._length*self._width*mass_asphalt*depth_asphalt
        print(mass_of_asphalt/1000)


road = Road(20, 5000)
road.get_mass_of_asphalt(25, 5)
