# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:30:18 2024

@author: mitch

Assignment: Visualizations with Python

Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart

I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.

"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

"""
Vis 1
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
"""
# Filter data for Utah
utah_df = covid_df[covid_df['Province_State'] == 'Utah']

# Melt the dataframe to convert dates to a single column
melted_df = utah_df.melt(id_vars=['Admin2'], 
                         value_vars=utah_df.columns[11:], 
                         var_name='Date', 
                         value_name='Cases')

# Convert Date to datetime
melted_df['Date'] = pd.to_datetime(melted_df['Date'])

# Create the plot
plt.figure(figsize=(16, 10))

# Plot all counties in grey
for county in utah_df['Admin2'].unique():
    county_data = melted_df[melted_df['Admin2'] == county]
    plt.plot(county_data['Date'], county_data['Cases'], color='grey', alpha=0.3, linewidth=1)

# Highlight Salt Lake County in a contrasting color
salt_lake_data = melted_df[melted_df['Admin2'] == 'Salt Lake']
plt.plot(salt_lake_data['Date'], salt_lake_data['Cases'], color='red', linewidth=2, label='Salt Lake County')

# Customize the plot
plt.title('COVID-19 Cases in Utah Counties Over Time', fontsize=30, pad=20)
plt.xlabel('Date', fontsize=14, labelpad=10)
plt.ylabel('Number of Cases', fontsize=14, labelpad=10)

# Format x-axis
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45, ha='right')

# Format y-axis
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

# Add legend
plt.plot([], [], color='grey', alpha=0.3, linewidth=1, label='Other Utah Counties')
plt.legend(fontsize=12, loc='upper left')

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Add data source and date information  Cite 
plt.figtext(0.98, 0.02, f'Data source: JHU CSSE COVID-19 Data\nLast updated: {melted_df["Date"].max().strftime("%Y-%m-%d")}', 
            ha='right', va='bottom', fontsize=8, style='italic')

plt.tight_layout()
plt.show()

"""
Vis 2
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
"""
# Filter data for Utah and Florida
utah_df = covid_df[covid_df['Province_State'] == 'Utah']
florida_df = covid_df[covid_df['Province_State'] == 'Florida']

# Find counties with the most cases
utah_max_county = utah_df.iloc[:, 11:].sum(axis=1).idxmax()
florida_max_county = florida_df.iloc[:, 11:].sum(axis=1).idxmax()

# Extract data for the counties with the most cases
utah_data = utah_df.loc[utah_max_county].iloc[11:]
florida_data = florida_df.loc[florida_max_county].iloc[11:]

# Convert index to datetime
utah_data.index = pd.to_datetime(utah_data.index)
florida_data.index = pd.to_datetime(florida_data.index)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the data
ax.plot(utah_data.index, utah_data.values, label=f'{utah_max_county}, Utah', linewidth=2)
ax.plot(florida_data.index, florida_data.values, label=f'{florida_max_county}, Florida', linewidth=2)

# Customize the plot
ax.set_title('COVID-19 Cases: Highest County in Utah vs. Florida', fontsize=18, pad=20)
ax.set_xlabel('Date', fontsize=14, labelpad=10)
ax.set_ylabel('Cumulative Cases', fontsize=14, labelpad=10)

# Format x-axis
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Format y-axis
def millions_formatter(x, pos):
    return f'{x/1e6:.1f}M'

ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

# Enhance grid
ax.grid(True, linestyle='--', alpha=0.7)

# Enhance legend
ax.legend(fontsize=12, loc='upper left')

# Highlight the difference
max_cases = max(utah_data.max(), florida_data.max())
difference = int(florida_data.max() - utah_data.max())
ax.annotate(f'Difference: {difference:,} cases',
            xy=(0.5, 0.95), xycoords='axes fraction',
            ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            fontsize=12)

# Add data source and date information
plt.figtext(0.98, 0.02, 'Data source: JHU CSSE COVID-19 Data', 
            ha='right', va='bottom', fontsize=8, style='italic')
plt.figtext(0.02, 0.02, f'Created: {pd.Timestamp.now().strftime("%Y-%m-%d")}', 
            ha='left', va='bottom', fontsize=8, style='italic')

plt.tight_layout()
plt.show()

"""
Vis 3
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
"""
# Select a county (e.g., Los Angeles, California)
county_data = covid_df[(covid_df['Admin2'] == 'Los Angeles') & (covid_df['Province_State'] == 'California')].iloc[0, 11:]

# Convert date strings to datetime objects
dates = pd.to_datetime(county_data.index)

# Calculate daily new cases
daily_cases = county_data.diff().fillna(0)

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Plot total cases
ax1.plot(dates, county_data, color='blue', linewidth=2, label='Total Cases')
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Cases', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Plot daily new cases
ax2.bar(dates, daily_cases, color='red', alpha=0.3, label='Daily New Cases')
ax2.set_ylabel('Daily New Cases', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Format x-axis dates
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Set title and legend
plt.title('COVID-19 Cases in Los Angeles County, California', fontsize=16)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Adjust layout and display the plot
fig.tight_layout()
plt.show()

"""
Vis 4
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
"""
states = ["Colorado", "Massachusetts", "Oregon", "Pennsylvania", "Utah", "Wyoming"]
filtered_data = covid_df[covid_df['Province_State'].isin(states)]

# Extract relevant columns: Admin2 (County), Province_State (State), and latest date data
latest_date = filtered_data.columns[-1]
state_county_data = filtered_data[['Province_State', 'Admin2', latest_date]]

# Aggregate county contributions to the total cases per state
state_grouped = state_county_data.groupby(['Province_State', 'Admin2'])[latest_date].sum().reset_index()

# Get top 5 counties for each state
top_counties = state_grouped.groupby('Province_State').apply(lambda x: x.nlargest(5, latest_date)).reset_index(drop=True)

# Calculate 'Other' for each state
other = state_grouped.groupby('Province_State')[latest_date].sum() - top_counties.groupby('Province_State')[latest_date].sum()
other_df = pd.DataFrame({'Province_State': other.index, 'Admin2': 'Other', latest_date: other.values})

# Combine top counties and 'Other'
plot_data = pd.concat([top_counties, other_df])

# Pivot the data for visualization
pivoted_data = plot_data.pivot(index='Province_State', columns='Admin2', values=latest_date).fillna(0)

# Sort states by total cases
states_sorted = pivoted_data.sum(axis=1).sort_values(ascending=False).index

# Generate a stacked bar chart
colors = plt.cm.tab20.colors  # Predefined set of colors
fig, ax = plt.subplots(figsize=(20, 10))

# Create the stacked bar plot
pivoted_data.loc[states_sorted].plot(kind='bar', stacked=True, ax=ax, color=colors[:pivoted_data.shape[1]])

# Add titles and labels
ax.set_title('County Contributions to Total COVID-19 Cases in Selected States', fontsize=24, pad=20)
ax.set_xlabel('States', fontsize=20, labelpad=15)
ax.set_ylabel('Number of Cases', fontsize=20, labelpad=15)

# Customize x-axis labels
plt.xticks(rotation=0, ha='center', fontsize=16)

# Customize y-axis labels
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
ax.tick_params(axis='y', labelsize=14)

# Customize legend
legend = ax.legend(title="Counties", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
legend.get_title().set_fontsize(14)

# Add data source and date information
plt.figtext(0.98, 0.02, f'Data source: JHU CSSE COVID-19 Data\nDate: {latest_date}', 
            ha='right', va='bottom', fontsize=10, style='italic')

plt.tight_layout()

# Show the plot
plt.show()

"""
Vis Extra credit (5 points)
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
"""
# Melt the dataframe to convert dates to a single column
melted_df = covid_df.melt(id_vars=['Province_State'], 
                          value_vars=covid_df.columns[11:], 
                          var_name='Date', 
                          value_name='Cases')

# Convert Date to datetime
melted_df['Date'] = pd.to_datetime(melted_df['Date'])

# Group by state and date, then sum cases
state_cases = melted_df.groupby(['Province_State', 'Date'])['Cases'].sum().reset_index()

# Get the total cases for each state on the last date
last_date = state_cases['Date'].max()
total_cases = state_cases[state_cases['Date'] == last_date].sort_values('Cases', ascending=False)

# Select top 20 states for better visibility
top_20_states = total_cases.head(20)['Province_State'].tolist()

# Filter data for top 20 states
plot_data = state_cases[state_cases['Province_State'].isin(top_20_states)]

# Create the plot
plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")

# Create box plot
ax = sns.boxplot(x='Province_State', y='Cases', data=plot_data, 
                 order=top_20_states, palette='viridis')

# Customize the plot
plt.title('Distribution of COVID-19 Cases by State', fontsize=24, pad=20)
plt.xlabel('States', fontsize=20, labelpad=15)
plt.ylabel('Number of Cases', fontsize=20, labelpad=15)
plt.xticks(rotation=45, ha='right')

# Format y-axis labels
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

# Add data source and date information
plt.figtext(0.98, 0.02, f'Data source: JHU CSSE COVID-19 Data\nLast updated: {last_date.strftime("%Y-%m-%d")}', 
            ha='right', va='bottom', fontsize=8, style='italic')

plt.tight_layout()
plt.show()

