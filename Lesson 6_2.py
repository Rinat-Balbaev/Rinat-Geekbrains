class Road:
    _length = None
    _width = None
    weight = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def MassCalc(self):
        self.weight = 25
        self.thickness = 0.05 #толщина полотна в метрах
        MassCalc = self.length * self.width * self.weight * self.thickness / 1000
        print(f'You need {MassCalc} tons of asphault to cover the road with length {self.length} m and width {self.width} m')

MyRoad = Road(5000, 20)
MyRoad.MassCalc()
