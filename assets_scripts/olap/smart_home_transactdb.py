import pandas as pd
import duckdb

# Step 1: Read the CSV file into a pandas DataFrame
csv_file_path = r'C:\Users\Bryn\Desktop\Work\Projects\DE coaching\Data modelling course\dimensional-data-modeling\assets_files\Smart Home data _updated.csv'  # replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Step 2: Connect to DuckDB (this will create a new database if it doesn't exist)
db_file_path = r'C:\Users\Bryn\Desktop\Work\Projects\DE coaching\Data modelling course\dimensional-data-modeling\assets_scripts\Smart_Home_transactdb.duckdb'  # replace with your desired database file name
connection = duckdb.connect(db_file_path)

# You can use the DataFrame's column names and types to create the table automatically
connection.execute('''
CREATE TABLE IF NOT EXISTS smart_home AS
SELECT * FROM df
''')

# Close the DuckDB connection
connection.close()