"""
band_expand.py
==============

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

    def writeAnnualReport(self):
        "Displays annual report for band."
        print("Band name: {0}\n".format(self.name))
        print("{0:20s} | {1:s}".format("Band member", "Weekly Wage"))

        members = self.wages.keys()

        for member in members:
            print("{0:20s} | {1:.2f}".format(member, self.wages[member]))
            
    def getMembers(self):
        "Return a list of band members."
        members = self.wages.keys()
        return members

    def sack(self, member):
        "Removes a band member."
        del self.wages[member]

    def promote(self, member, payrise):
        "Increases wage of band member."
        self.wages[member] += payrise
