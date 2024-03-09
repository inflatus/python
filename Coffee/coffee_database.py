#take inputs from users
#add to sql database

import sqlite3

# Define database name
database_name = 'coffee.db'

connection = sqlite3.connect('coffee.db')
cursor = connection.cursor()

# Get column names from user input (replace with your prompts)
column1_name = input("Date: ")
column2_name = input("Place: ")
column3_name = input("Street: ")
column4_name = input("City: ")
column5_name = input("State: ")                    
column6_name = input("Zip Code: ")
column7_name = input("Phone Number eg: 5551231234: ")
column8_name = input("Type of Coffee Drink: ")
column9_name = input("Rating 1 worst - 5 exceptional: ")
column10_name = input("Price Rating 1 least - 5 most expensive: ")


# Create table with user-defined column names 
create_table_query = f"""CREATE TABLE IF NOT EXISTS user_data (
    {column1_name} Date,
    {column2_name} Place,
    {column3_name} Street,
    {column4_name} City,
    {column5_name} State,
    {column6_name} Zip Code,
    {column7_name} Phone Number,
    {column8_name} Type of Coffee Drink,
    {column9_name} Rating 1 worst - 5 exceptional,
    {column10_name} Price Rating 1 least - 5 most expensive
)"""

cursor.execute(create_table_query)

# Get data from user input 
data1 = input("Enter data for the first column: ")
data2 = input("Enter data for the second column: ")
data3 = input("Enter data for the third column: ")
data4 = input("Enter data for the fourth column: ")
data5 = input("Enter data for the fifth column: ")
data6 = input("Enter data for the sixth column: ")
data7 = input("Enter data for the seventh column: ")
data8 = input("Enter data for the eighth column: ")
data9 = input("Enter data for the ninth column: ")
data10 = input("Enter data for the tenth column: ")

# Insert data into the table using placeholders to prevent SQL injection
insert_query = f"""INSERT INTO user_data VALUES (?, ?)"""
cursor.execute(insert_query, (data1, data2))


connection.commit()
connection.close()

