import pandas as pd
import time

file1 = 'Crime_Data_from_2017_to_2019.csv'
file2 = 'Crime_Data_from_2020_to_2021.csv'
file3 = 'Test.csv'

df = pd.read_csv("Crime_Data_from_2017_to_2019.csv")

def load_data():
    global df
    print("[{}] Select the number of the file to load from the list below:".format(time.ctime()))
    print("[1] {}".format(file1))
    print("[2] {}".format(file2))
    print("[3] {}".format(file3))
    file_choice = input("[{}] ".format(time.ctime()))
    start_time = time.time()
    if file_choice == "1":
        df = pd.read_csv(file1)
    elif file_choice == "2":
        df = pd.read_csv(file2)
    elif file_choice == "3":
        df = pd.read_csv(file3)
    else:
        print("Invalid choice")
        return
    end_time = time.time()
    print("[{}] Total Columns Read: {}".format(time.ctime(), len(df.columns)))
    print("[{}] Total Rows Read: {}".format(time.ctime(), len(df)))
    print("File loaded successfully!")
    print("Time to load {:.2f} sec.".format(end_time - start_time))

def list_all_columns(df):
    # Print all column names
    print("Column Names:")
    for col in df.columns:
        print(col)

def drop_columns(df):
    # Prompt user for columns to drop
    columns_to_drop = input("Enter the column to drop: ").split(",")

    # Drop specified columns
    df.drop(columns_to_drop, axis=1, inplace=True)

    print("Columns dropped successfully.")

def describe_columns(df):
    """# Prompt user for column to describe
    column_name = input("Enter the name of the column to describe: ")

    # Describe specified column
    print(df[column_name].describe())
    """
    print(df.describe())


def search_element_in_column(df):
    # Prompt user for column and element to search for
    column_name = input("Enter the name of the column to search in: ")
    search_value = input("Enter the value to search for: ")

    # Search for element in specified column
    search_result = df[df[column_name] == search_value]

    print("Search result:")
    print(search_result)

# Main program loop
while True:
    # Prompt user for menu choice
    print("Menu:")
    print("1. Load Data")
    print("2. Manipulate data")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        load_data()
    elif choice == "2":
        #read the file first
        #df = read_csv_file()
        # Prompt user for manipulation choice
        print("Manipulation options:")
        print("1. List all columns")
        print("2. Drop columns")
        print("3. Describe columns")
        print("4. Search element in column")

        option = input("Enter your choice: ")

        # Call the appropriate function based on the user's choice
        if option == "1":
            list_all_columns(df)
        elif option == "2":
            df = drop_columns(df)
        elif option == "3":
            describe_columns(df)
        elif option == "4":
            search_element_in_column(df)
        else:
            print("Invalid choice. Please try again.")
    elif choice == "3":
        # Exit program
        break
    else:
        print("Invalid choice. Please try again.")
