# Your "readHeader" function might look like:

def readHeader(fname):
    "Reads a data file `fname` and returns a dictionary of header metadata."
    with open(fname) as f:
        header = {}

        i = 0
        while i < 3:
            line = f.readline()
            # Strip any white space from line
            line = line.strip()

            key, value = line.split(":")
            header[key] = value
            i += 1

    return header

# Test it with
head = readHeader("../example_data/weather_meta.csv")
print(head)

def readData(fname):
    "Reads a data file `fname` and returns a dictionary of arrays of values."
    with open(fname) as f:
        data = {}

        # Ignore the header
        for i in range(3):
            f.readline()

        # Read in variable names
        col_names = f.readline().strip().split(",")
        for col_name in col_names:
            data[col_name] = []
            i = 0

        for line in f.readlines():
            # Strip any white space from line
            line = line.strip()

            values = line.split(",")

            for (i, value) in enumerate(values):
                col_name = col_names[i]
                data[col_name].append(value)

    return data

print(readData("../example_data/weather_meta.csv"))
