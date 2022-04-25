import math

class mathFunction:
    def setVelocity(pos1, pos2, shootPower = 1):
        return [math.sqrt(abs(pos1[0] - pos2[0])) * shootPower, math.sqrt(abs(pos1[1] - pos2[1])) * shootPower]

    def setDirection(pos1, pos2):
        return [math.sqrt(abs(pos1[0])) / 10 - math.sqrt(abs(pos2[0])) / 10, math.sqrt(abs(pos1[1])) / 10 - math.sqrt(abs(pos2[1])) / 10]
    
    def getDistance(pos1, pos2):
        return math.sqrt(math.pow(abs(pos1[0] - pos2[0]), 2) + math.pow(abs(pos1[1] - pos2[1]), 2))