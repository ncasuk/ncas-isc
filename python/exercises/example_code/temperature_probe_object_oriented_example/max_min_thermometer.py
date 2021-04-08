from thermometer import Thermometer


class MaxMinThermometer(object):
    """
    a maximum minimum thermometer which encapsulates (i.e. contains) 
    a thermometer and also stores min / max temperature data
    """

    def __init__(self):
        self.thermometer = Thermometer()
        self.min = None
        self.max = None


    def get_measurement(self):        
        (temp, when) = self.thermometer.get_measurement()
        self.update_max_min(temp)
        return (temp, when)


    def update_max_min(self, temp):
        if self.min == None or self.min > temp:
            self.min = temp
        if self.max == None or self.max < temp:
            self.max = temp


    def reset_max_min(self):
        self.min = None
        self.max = None


    def close(self):
        self.thermometer.close()
