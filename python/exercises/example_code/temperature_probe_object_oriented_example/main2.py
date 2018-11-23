from max_min_thermometer import MaxMinThermometer

mmt = MaxMinThermometer()

for i in range(10):

    temp, when = mmt.get_measurement()
    print("{} current={} min={} max={}".format(when.isoformat(),
                                               temp,
                                               mmt.min,
                                               mmt.max))

    if i == 5:
        print("Resetting max and min")
        mmt.reset_max_min()

mmt.close()
