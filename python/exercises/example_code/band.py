"""
band.py
=======

Holds the Band class.

When you manage many bands and you need to keep track of information in your band.

You need a python class to help you do this for each band you manage.

"""

class Band(object):

    def __init__(self, name):
        """
        Defines the band name.
        Set up a dictionary belonging to the band.
        Keys will be names, values will be weekly wages in pounds.
        """
        self.name = name
        self.wages = {}

    def employ(self, member, wage):
        "Adds new band member and wage."
        if wage > 100:
            raise ValueError("{0} costs too much - cannot join the band!".format(member))

        self.wages[member] = wage

    def write_annual_report(self):
        "Displays annual report for band."
        print("Band name: %s\n" % self.name)
        print("%20s | %s" % ("Band member", "Weekly Wage"))

        members = self.wages.keys()

        for member in members:
            print("%20s | %.2f " % (member, self.wages[member]))
