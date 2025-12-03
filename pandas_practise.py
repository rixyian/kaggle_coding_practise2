import pandas as pd

df1 = pd.read_csv("orders.csv") #`.read_csv` is what pd uses for csv files
print(df1)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}

df2 = pd.DataFrame(data) #`.dataframe` is what pd uses for dictionaries
print(data)
print(df2)
print(df1)