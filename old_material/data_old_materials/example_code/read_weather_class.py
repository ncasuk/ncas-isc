# Your new class might look like:
class Weather(object):

    def __init__(self, fname):
        self.readHeader(fname)
        self.readData(fname)

    def readHeader(self, fname):
        "Reads header from data file `fname` and populates instance dictionary: self.header."
        with open(fname) as f:
            self.header = {}

            i = 0
            while i < 3:
                line = f.readline()
                # Strip any white space from line
                line = line.strip()

                key, value = line.split(":")
                self.header[key] = value
                i += 1


    def readData(self, fname):
        "Reads a data file `fname` and populates instance dictionary: self.data."
        with open(fname) as f:
            self.data = {}

            # Ignore the header
            for i in range(3):
                f.readline()

            # Read in variable names
            col_names = f.readline().strip().split(",")
            for col_name in col_names:
                self.data[col_name] = []
                i = 0

            for line in f.readlines():
            
                # Strip any white space from line
                line = line.strip()
                values = line.split(",")

                for (i, value) in enumerate(values):
                    col_name = col_names[i]
                    self.data[col_name].append(value)


# Test it with:
weather = Weather("../example_data/weather_meta.csv")
print(weather.header)
print(weather.data)
