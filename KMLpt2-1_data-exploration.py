import pandas as pd

# save filepath to variable for easier access, path from pwd in this case
melbourne_file_path = "melb_data.csv"
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
print("dataframe 'melbourne_data' has been created from file: ", melbourne_file_path,"\n") 

# print a summary of the data in Melbourne data
print("now using panda tools to format as a dataframe table:\n", melbourne_data.describe())

#own_data = {
#    'Name': ['Alice', 'Bob', 'Charlie'],
#    'Age': [25, 30, 35],
#    'Country': ['USA', 'Canada', 'UK']
#}

#own_df = pd.DataFrame(own_data)
#print("df of my own data:\n", own_df)
