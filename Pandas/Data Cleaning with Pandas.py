# -*- coding: utf-8 -*-
"""
Created 11:11:11 2024

Assignment: Data Cleaning with Pandas
@author: mitch
#Question 1 How many flights were there from JFK to SLC? Int

#Question 2 How many airlines fly to SLC? Should be int

#Question 3 What is the average arrival delay for flights to RDU? float

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA
and JFK)? float

#Question 5 Which date has the largest average depature delay? Pd slice with date
and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)

#Question 6 Which date has the largest average arrival delay? pd slice with date
and float

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice
with tailnumber and speed
#speed = distance/airtime

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans

#Question 9 How many observations were made in Feburary? Int

#Question 10 What was the mean for humidity in February? Float

#Question 11 What was the std for humidity in February? Float

"""

##%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import zipfile  # handle ZIP files

#%% Importing Data
# Specify the path to the ZIP file
zip_file_path = r'C:\Users\mitch\OneDrive\Desktop\BMI-6018\Pandas\data.zip'
#update to your own location of the file. I'm guessing that you wont be able to run it from my computer:) 

# Extract and read the CSV files
with zipfile.ZipFile(zip_file_path) as z:
    
    # Read flights.csv
    with z.open('flights.csv') as f:
        flights_data = pd.read_csv(f)
    
    # Read weather.csv
    with z.open('weather.csv') as f:
        weather_data = pd.read_csv(f)

# Display the first 10 rows of each DataFrame
print("Flights Data:")
print(flights_data.head(10))

print("\nWeather Data:")
print(weather_data.head(10))



#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
q_1 = flights_data[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')].shape[0]
print(q_1)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = flights_data[flights_data['dest'] == 'SLC']['carrier'].nunique()
print(q_2)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data[flights_data['dest'] == 'RDU']['arr_delay'].mean()
print("Grand_total_delay_average_RDU",q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
nyc_flights_to_sea = flights_data[(flights_data['dest'] == 'SEA') & (flights_data['origin'].isin(['LGA', 'JFK']))].shape[0]
total_flights_to_sea = flights_data[flights_data['dest'] == 'SEA'].shape[0]
q_4 = nyc_flights_to_sea / total_flights_to_sea
print("proportion of flights to SEA from LGA and JFK ", q_4)

#total form LGA and JFK = 2092 
#total to SEA = 3923

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)

# Data Processing
# Create a new 'date' column in 'YYYY/MM/DD' format
flights_data['date'] = pd.to_datetime(flights_data[['year', 'month', 'day']]).dt.strftime('%Y/%m/%d')

# Calculate the date with the largest average departure delay
q_5 = flights_data.groupby('date')['dep_delay'].mean().idxmax()
largest_avg_dep_delay = flights_data.groupby('date')['dep_delay'].mean().max()

print(f"The date with the largest average departure delay is: {q_5} with an average delay of {largest_avg_dep_delay:.2f} minutes.")


#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime

# Filter flights data for the year 2013 and originating from LGA or JFK
flights_2013 = flights_data[(flights_data['year'] == 2013) & (flights_data['origin'].isin(['LGA', 'JFK']))]

# Calculate speed as distance divided by airtime
flights_2013['speed'] = flights_2013['distance'] / flights_2013['air_time']

# Find the flight with the maximum speed
fastest_flight = flights_2013.loc[flights_2013['speed'].idxmax(), ['tailnum', 'speed']]

# Print the fastest flight details
print(fastest_flight)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
weather_data.fillna(0, inplace=True)
q_8 = weather_data
print(q_8) 


#%% Numpy Data Filtering/Sorting Question Answering
# Check the shape of the weather_data
print(weather_data.shape)

# Question 9: How many observations were made in February?
# Assuming column 4 corresponds to months (1 = January, 2 = February, etc.)
q_9 = np.sum(weather_data['month'] == 2)  #  'month' column name
print("observations ", q_9)

#Question 10 What was the mean for humidity in February? Float
# Fill NaN values with 0
weather_data.fillna(0, inplace=True)

# 'humid' is the column name for humidity in your DataFrame
humidity_column_index = weather_data.columns.get_loc('humid')

# Calculate the mean of the 'humid' column for February only
q_10 = np.mean(weather_data[weather_data['month'] == 2].iloc[:, humidity_column_index])

print("Mean Humidity in February:", q_10)


# Question 11: What was the std for humidity in February? Answer will be a Float
q_11 = np.std(weather_data.loc[weather_data['month'] == 2, 'humid'])  # Filter for February

print("Standard Deviation of Humidity in February:", q_11)




