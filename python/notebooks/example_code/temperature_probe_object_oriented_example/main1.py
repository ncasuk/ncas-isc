from thermometer import Thermometer

thermometer = Thermometer()

for i in range(5):
    temp, when = thermometer.get_measurement()
    print("{} temperature = {} degrees".format(when.isoformat(),
                                               temp))

thermometer.close()
