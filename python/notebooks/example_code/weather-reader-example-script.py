import sys


# Functions
def split_and_strip(line):
	values = []
	
	for value in line.split(","):
		values.append(value.strip())

	return values
		

def read_data_file(fpath):
	"""
	Reads weather data from CSV file.
	Params:
	 - fpath: file path to CSV file
	Returns:
	 - data dictionary.
	"""
	# Main code
	data = {}

	with open(fpath, 'r') as reader:

		# Read header
		header = reader.readline()
		col_names = split_and_strip(header)
		
		# Set up dictionary for loading
		for col in col_names:
			data[col] = []

		# Read data
		for line in reader:
			data_items = split_and_strip(line)
			print(f"[INFO] Data items: {data_items}")
			
			for (index, item) in enumerate(data_items):
				col = col_names[index]
				value = item
				data[col].append(value)
				
	return data
	
		
if __name__ == "__main__":
	# Call the function
	args = sys.argv[1:]
	
	for arg in args:
	
		print("[INFO] Reading from: {}".format(arg))
		data = read_data_file(arg)
		print(data)
