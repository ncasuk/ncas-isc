def readHeader(fname):
    with open(fname) as f:
        head = f.readlines()[:6]
    
    # Get important stuff
    location, variable, units = head[0].split()
    units = units.replace("(", "").replace(")", "")

    # Put others lines in comments
    comments = head[1:6]
    return (location, variable, units, comments)

(location, variable, units, comments) = readHeader("../example_data/uk_rainfall.txt")
print(location, variable, units)
print(comments[1])

def checkValue(value):
    # Check if value should be a float 
    # or flagged as missing
    if value == "---":
        value = MA.masked
    else:
        value = float(value)
    return value

import numpy.ma as MA

def readData(fname):
    # Open file and read column names and data block
    with open(fname) as f:

        # Ignore header
        for i in range(7): f.readline() 
        
        col_names = f.readline().split()
        data_block = f.readlines()

    
    # Create a data dictionary, containing
    # a list of values for each variable
    data = {}

    # Add an entry to the dictionary for each column
    for col_name in col_names:
        data[col_name] = MA.zeros(len(data_block), 'f', fill_value = -999.999)

    # Loop through each value: append to each column
    for (line_count, line) in enumerate(data_block):
        items = line.split()
        
        for (col_count, col_name) in enumerate(col_names):
            value = items[col_count]
            data[col_name][line_count] = checkValue(value)

    return data
        
data = readData("../example_data/uk_rainfall.txt")
print(data["Year"])
print(data["JAN"])

winter = data["WIN"]
print(MA.is_masked(winter[0]))
print(MA.is_masked(winter[1]))
