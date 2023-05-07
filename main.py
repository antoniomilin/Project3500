# course: CMPS3500
# CLASS Project
# PYTHON IMPLEMENTATION: crime data analysis exploration tool
# date: 05/12/23
# Student 1: Antonio Millin
# Student 2: Connor Tennison
# Student 3: Mariana Lara
# Student 4: Ryan Gordon
# description: allows users to load, drop, search, and analyze crime data.
import pandas as pd
import time

# Function to load data from CSV files
def load_data():
    global df
    print("\nSelect the number of the file to load from the list below:")
    print("[1] Crime_Data_from_2017_to_2019.csv")
    print("[2] Crime_Data_from_2020_to_2021.csv")
    print("[3] Test.csv")

# Prompt the user to select a file to load
    file_choice = int(input("Please select an option: "))
    if file_choice == 1:
        file_name = 'Crime_Data_from_2017_to_2019.csv'
    elif file_choice == 2:
        file_name = 'Crime_Data_from_2020_to_2021.csv'
    elif file_choice == 3:
        file_name = 'Test.csv'
    else:
        print("Invalid choice. Please try again.")
        return
    
# Read the CSV file and store it in a DataFrame
    start_time = time.time()
    df = pd.read_csv(file_name)
    end_time = time.time()
    
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis=1, inplace=True)

    print(f"\nTotal Columns Read: {df.shape[1]}")
    print(f"Total Rows Read: {df.shape[0]}")
    print(f"\nFile loaded successfully! Time to load {end_time - start_time:.2f} sec.")
    
# Function to drop columns with high null values 
def drop_high_null_columns(df):
    columns_to_drop = ['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street']
    df.drop(columns_to_drop, axis=1, inplace=True)
    print(f"Dropped columns with high null values: {', '.join(columns_to_drop)}")

# Function to list all columns
def list_all_columns(df):
    print("\nColumns in the dataset:")
    for index, col in enumerate(df.columns, start=1):
        print(f"[{index}] {col}")

# Function to drop a specific column
def drop_columns(df):
    list_all_columns(df)
    col_to_drop = int(input("\nSelect a column number to drop from the list: "))
    if 0 < col_to_drop <= len(df.columns):
        col_name = df.columns[col_to_drop - 1]
        df.drop(col_name, axis=1, inplace=True)
        print(f"Column [{col_to_drop}] dropped!")
    else:
        print("Invalid column number. Please try again.")

# Calculate the count of values in a list
def count(data):
    return len(data)

# Calculate the unique count of values in a list
def unique_count(data):
    return len(set(data))

# Calculate the mean of a list of numerical data
def mean(data):
    return sum(data) / len(data)

# Calculate the median of a list of numerical data
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

# Calculate the mode of a list of data
def mode(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return max(counts, key=counts.get)

# Calculate the variance of a list of numerical data
def variance(data):
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / len(data)

# Calculate the standard deviation of a list of numerical data
def std_dev(data):
    return variance(data) ** 0.5

# Find the minimum value in a list of numerical data
def minimum(data):
    return min(data)

# Find the maximum value in a list of numerical data
def maximum(data):
    return max(data)

# Describe a selected column
def describe_custom(df, col_name):
    start_time = time.time()
    numerical_data = [x for x in df[col_name] if isinstance(x, (int, float))]
    if not numerical_data:
        print("The selected column does not contain numerical data.")
        return

    # count
    count = 0
    for _ in numerical_data:
        count += 1

    #unique coutn
    unique_count = 0
    unique_values = []
    for value in numerical_data:
        if value not in unique_values:
            unique_values.append(value)
            unique_count += 1
    
    #mean
    mean = 0
    for value in numerical_data:
        mean += value
    mean /= count

    # median
    sorted_data = sorted(numerical_data)
    if count % 2 == 0:
        median = (sorted_data[count // 2 - 1] + sorted_data[count // 2]) / 2
    else:
        median = sorted_data[count // 2]

    #mode section
    mode = None
    mode_count = 0
    for value in unique_values:
        value_count = 0
        for data_value in numerical_data:
            if value == data_value:
                value_count += 1
        if value_count > mode_count:
            mode_count = value_count
            mode = value

    # stand. deviation
    deviation_sum = 0
    for value in numerical_data:
        deviation_sum += (value - mean) ** 2
    deviation = (deviation_sum / (count - 1)) ** 0.5

    #variance
    variance = deviation ** 2

    #min
    minimum = numerical_data[0]
    for value in numerical_data:
        if value < minimum:
            minimum = value
    
    #max
    maximum = numerical_data[0]
    for value in numerical_data:
        if value > maximum:
            maximum = value


    print(f"\n{col_name} stats:")
    print("===================")
    print(f"Count: {count}")
    print(f"Unique Count: {unique_count}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {deviation:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    
    end_time = time.time()
    processing_time = end_time - start_time
    print(f"\nStats printed successfully! Time to process is {processing_time:.2f} sec.")

def describe_columns(df):
    list_all_columns(df)
    col_to_describe = int(input("\nSelect column number to describe: "))
    if 0 < col_to_describe <= len(df.columns):
        col_name = df.columns[col_to_describe - 1]
        describe_custom(df, col_name)
    else:
        print("Invalid column number. Please try again.")

def search_element_in_column(df):
    list_all_columns(df)
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    col_to_search = int(input(f"\n{current_time} Select column number to perform a search: "))
    
    if 0 < col_to_search <= len(df.columns):
        col_name = df.columns[col_to_search - 1]
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        search_element = input(f"{current_time} Enter element to search: ")
        
        start_time = time.time()
        found = df[df[col_name].apply(lambda x: str(x).lower()) == search_element.lower()].index.tolist()
        end_time = time.time()
        processing_time = end_time - start_time
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{current_time} Element found in {len(found)} rows.")
        
        print(f"\nSearch was successful! Time to search was {processing_time:.2f} sec.")
    else:
        print("Invalid column number. Please try again.")

# Analysis functions
# Task 1: Show the total unique count of crimes per year sorted in descending order.
def crimes_per_year(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Year'] = df['DATE OCC'].dt.year
    crimes_by_year = df['Year'].value_counts().sort_index(ascending=False)
    print(crimes_by_year)

# Task 2: Show the top 5 areas (AREA NAME) with the most crime events in all years (Sorted by the number of crime events)
def top_5_areas_with_most_crimes(df):
    top_areas = df['AREA NAME'].value_counts().nlargest(5)
    print(top_areas)

# Task 3: Show all months and the unique total count of crimes sorted in increasing order.
def crimes_by_month(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Month'] = df['DATE OCC'].dt.month
    crimes_by_month = df['Month'].value_counts().sort_index()
    print(crimes_by_month)

# Task 4: Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.
def top_10_streets_in_2019(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Year'] = df['DATE OCC'].dt.year
    streets_2019 = df[df['Year'] == 2019]
    top_streets = streets_2019['LOCATION'].value_counts().nlargest(10)
    print("\nTop 10 streets with the most crimes in LA in 2019 and the total amount of crimes in each street:")
    print(top_streets)



# Task 5: Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.
def top_5_dangerous_hours_in_hollywood(df):
    hollywood_df = df[df['AREA NAME'] == 'Hollywood'].copy()
    hollywood_df['DATE OCC'] = pd.to_datetime(hollywood_df['DATE OCC'])
    hollywood_df['Hour'] = hollywood_df['DATE OCC'].dt.hour
    dangerous_hours = hollywood_df['Hour'].value_counts().nlargest(5)
    print(dangerous_hours)

# Task 6: Print the details of the crime that took the most time (in hours) to be reported.
def crime_with_longest_report_time(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'])
    df['Report Time'] = (df['Date Rptd'] - df['DATE OCC']).dt.total_seconds() / 3600
    longest_report_index = df['Report Time'].idxmax()
    longest_report = df.loc[longest_report_index]
    print(longest_report)

# Task 7: Show the 10 top most common crime types (Crm Cd Desc) overall across all years.
def top_10_common_crime_types(df):
    common_crimes = df['Crm Cd Desc'].value_counts().nlargest(10)
    print(common_crimes)

# Task 8: Are women or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?
def gender_victim_lunchtime(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')
    df['Hour'] = df['DATE OCC'].dt.hour
    lunchtime_df = df[(df['Hour'] >= 11) & (df['Hour'] <= 13)]
    gender_counts = lunchtime_df['Vict Sex'].value_counts()
    print(gender_counts)

# Task 9: What is the month that has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.
def most_credit_card_frauds_month_2019(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Year'] = df['DATE OCC'].dt.year
    df['Month'] = df['DATE OCC'].dt.month
    credit_card_frauds = df[(df['Year'] == 2019) & (df['Crm Cd Desc'] == 'CREDIT CARDS, FRAUD USE ($950 & UNDER)')]
    frauds_by_month = credit_card_frauds['Month'].value_counts().idxmax()
    print("\nMonth with the most major credit card frauds in LA in 2019:")
    print(frauds_by_month)

# Task 10: List the top 5 more dangerous areas for older men (age from 65 and more) in December of 2018.
def top_5_dangerous_areas_older_men_dec_2018(df):
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Year'] = df['DATE OCC'].dt.year
    df['Month'] = df['DATE OCC'].dt.month
    older_men_crimes = df[(df['Year'] == 2018) & (df['Month'] == 12) & (df['Vict Sex'] == 'M') & (df['Vict Age'] >= 65)]
    dangerous_areas = older_men_crimes['AREA NAME'].value_counts().head(5)
    print("\nTop 5 more dangerous areas for older men (age 65 and more) in December of 2018:")
    print(dangerous_areas)


def main():
    global df
    df = None
    while True:
        print("\nMain Menu:")
        print("**********")
        print("(1) Load Data")
        print("(2) Exploring Data")
        print("(3) Data Analysis")
        print("(4) Print Data Set")
        print("(5) Quit")
        choice = int(input("Please select an option: "))

        if choice == 1:
            load_data()
            drop_high_null_columns(df)
        elif choice == 2:
            if df is None:
                print("Please load the data first.")
                continue
            exploring_data_menu(df)
        elif choice == 3:
            if df is None:
                print("Please load the data first.")
                continue
            data_analysis_menu(df)
        elif choice == 4:
            if df is None:
                print("Please load the data first.")
                continue
            print_data_set(df)
        elif choice == 5:
            break
        else:
                        print("Invalid option. Please try again.")

def exploring_data_menu(df):
    while True:
        print("\nExploring Data Menu:")
        print("*********************")
        print("(1) List All Columns")
        print("(2) Drop a Column")
        print("(3) Describe a Column")
        print("(4) Search Element in Column")
        print("(5) Return to Main Menu")
        choice = int(input("Please select an option: "))

        if choice == 1:
            list_all_columns(df)
        elif choice == 2:
            drop_columns(df)
        elif choice == 3:
            describe_columns(df)
        elif choice == 4:
            search_element_in_column(df)
        elif choice == 5:
            break
        else:
            print("Invalid option. Please try again.")

def data_analysis_menu(df):
    while True:
        print("\nData Analysis Menu:")
        print("*********************")
        print("(1) Show the total unique count of crimes per year sorted in descending order.")
        print("(2) Show the top 5 areas (AREA NAME) with the most crime events in all years.")
        print("(3) Show all months and the unique total count of crimes sorted in increasing order.")
        print("(4) Show the top 10 streets with the most crimes in LA in 2019.")
        print("(5) Show the top 5 most dangerous times (in hours) to be in Hollywood.")
        print("(6) Print the details of the crime that took the most time (in hours) to be reported.")
        print("(7) Show the 10 top most common crime types (Crm Cd Desc) overall across all years.")
        print("(8) Are women or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?")
        print("(9) What is the month that has the most major credit card frauds in LA in 2019?")
        print("(10) List the top 5 more dangerous areas for older men (age from 65 and more) in December of 2018.")
        print("(11) Return to Main Menu.")
        
        try:
            choice = int(input("Please select an option: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            crimes_per_year(df)
        elif choice == 2:
            top_5_areas_with_most_crimes(df)
        elif choice == 3:
            crimes_by_month(df)
        elif choice == 4:
            top_10_streets_in_2019(df)
        elif choice == 5:
            top_5_dangerous_hours_in_hollywood(df)
        elif choice == 6:
            crime_with_longest_report_time(df)
        elif choice == 7:
            top_10_common_crime_types(df)
        elif choice == 8:
            gender_victim_lunchtime(df)
        elif choice == 9:
            most_credit_card_frauds_month_2019(df)
        elif choice == 10:
            top_5_dangerous_areas_older_men_dec_2018(df)
        elif choice == 11:
            break
        else:
            print("Invalid option. Please try again.")

def print_data_set(df):
    print(df)

if __name__ == "__main__":
    main()
