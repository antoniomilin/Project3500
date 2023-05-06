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
    print("List all columns:")
    print("*****************")
    for col in df.columns:
        print(col)

def drop_columns(df):
    # Prompt user for columns to drop
    print("Drop Columns:")
    print("*************")
    columns_to_drop = input("Select a column number to Drop from the list: ").split(",")

    # Drop specified columns
    df.drop(columns_to_drop, axis=1, inplace=True)

    print("Columns dropped successfully.")

def describe_columns():
    # Read the CSV file and extract column names
    with open("Crime_Data_from_2017_to_2019.csv") as f:
        header = f.readline().strip().split(",")

    # Print available columns and prompt user to select one
    print("Describe Columns:\n**********************")
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Select column number to Describe:\n")
    for i, name in enumerate(header):
        print(f"[{i+1}] {name}")
    col_num = int(input(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] "))

    # Load column data and calculate statistics
    start_time = time.time()
    data = []
    with open("Crime_Data_from_2017_to_2019.csv") as f:
        f.readline()
        for line in f:
            fields = line.strip().split(",")
            if len(fields) < col_num:
                data.append(None)
            else:
                data.append(fields[col_num-1])

    count = len(data)
    unique_count = len(set(data))
    mean = sum(float(x) for x in data if x is not None) / count
    median = sorted(float(x) for x in data if x is not None)[count//2]
    mode = max(set(data), key=data.count)
    sd = (sum((float(x) - mean)**2 for x in data if x is not None) / count)**0.5
    variance = sd**2
    minimum = min(float(x) for x in data if x is not None)
    maximum = max(float(x) for x in data if x is not None)

    # Print statistics
    print(f"\nColumn {col_num} stats:\n{'='*15}")
    print(f"Count: {count}")
    print(f"Unique: {unique_count}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation (SD): {sd:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Minimum: {minimum:.2f}")
    print(f"Maximum: {maximum:.2f}\n")
    print(f"Stats printed successfully! Time to process is {time.time()-start_time:.2f} sec.")


def search_element_in_column(df):
   # Prompt user for column and element to search for
    print("Search Element in Column:")
    print("*************************")
    column_name = input("Select column number to perform a search: \n")
    search_value = input("Enter the value to search for: ")

    # Search for element in specified column
    search_result = df[df[column_name] == search_value]

    print("Search result:")
    print(search_result)

# Main program loop

while True:
    # Prompt user for menu choice
    print("\nMain Menu:")
    print("1. Load Data")
    print("2. Exlopring Data")
    print("3. Data Analysis")
    print("4. Print Data Set")
    print("0. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        load_data()
    elif choice == "2":
        #read the file first
        #df = read_csv_file()
        # Prompt user for manipulation choice
        print("Exploring Data:")
        print("***************")
        print("1. List all columns")
        print("2. Drop columns")
        print("3. Describe columns")
        print("4. Search element in column")
        print("0. Back to Main Menu")

        option = input("Enter your choice: ")
        print("\n")
        # Call the appropriate function based on the user's choice
        if option == "1":
            list_all_columns(df)
        elif option == "2":
            df = drop_columns(df)
        elif option == "3":
            print("Describe Columns:")
            print("*****************")
            describe_columns()
        elif option == "4":
            search_element_in_column(df)
        elif option == "0":
            #go back to main menu
            print("\n...going back to Main Menu...\n")
        else:
            print("Invalid choice. Please try again.")

    elif choice == "3":
        #read the file first
        #df = read_csv_file()
        # Prompt user for manipulation choice
        print("Data Analysis:")
        print("**************")

        print("Show the total unique count of crimes per year sorted in descending order.")

        print("\nList the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018 in West LA.")

    elif choice == "0":
        # Exit program
        break
    else:
        print("Invalid choice. Please try again.")
