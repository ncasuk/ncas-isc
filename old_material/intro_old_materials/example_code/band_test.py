"""
band_test.py
============

Code for testing out the class: Band.

"""

# Start managing your bands
from band_expand import Band
ws = Band("The White Stripes")
ws.employ("Meg", 100)
ws.employ("Jack", 100)
ws.writeAnnualReport()            
            
# Start another band
hs = Band("Hearsay")

applicants = ("Suzanne", "Danny", "Kym", "Myleene", "Noel")
for app in applicants:
    hs.employ(app, 10)

# oh, well...

hs.sack("Danny")

members = hs.getMembers()
print(members)

hs.promote("Kym", 5)
hs.writeAnnualReport()

# Try to employ Madonna
hs.employ("Madonna", 100000)
