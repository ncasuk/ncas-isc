# encoding: utf-8
"""
read_table.py
=============

Contains the "print_table" function which can be used
to print a table to output with only selected columns.

"""

headers = ['time', 'temperature', 'wind_direction', 'wind_speed', 'humidity']
data = [
    ['08:00', 14, 200, 3, 54],
    ['09:00', 15, 200, 4, 54],
    ['10:00', 17, 190, 3, 54],
    ['11:00', 20, 190, 5, 54],
]


def print_table(column_names):
    """
    This programme displays a table on the screen
    but only shows the selected columns.

    :param column_names: Columns to print
    """

    if not column_names:
        return

    # Find the column indices for the requested columns
    indices = []
    for header in column_names:
        indices.append(headers.index(header))

    # Print the headers
    output = [headers[i] for i in indices]
    print('\t'.join(output))

    # Print data
    for row in data:
        output = [str(row[i]) for i in indices]
        print('\t'.join(output))

