# Analyzing Marketing Campaign with Python

# CHAPTER 1. Pandas

# 1. Introduction to pandas for marketing
# analyze marketing compaign performance
# attribute credit for conversions to marketing channels
# A/B testing
# 'pandas' library to help analyzing marketing campaign

# EXAMPLE:
# Importing the dataset
# Import pandas into the environment
import pandas as pd
# Import marketing.csv
marketing = pd.read_csv('marketing.csv')
# Print the first five rows of the DataFrame
print(marketing.head())
# Print the statistics of all columns
print(marketing.describe())
# Check column data types and non-missing values
print(marketing.info())

# 2. Data types and data merging
# 'dtype' to show the data type of a column
# astype() to change the data type of a column
# map() to map values to existing columns
# dealing with date columns:
# --1) pd.read_csv('', parse_dates=[])
# --2) pd.to_datetime()

# EXAMPLE:
# Updating the data type of a column
# Check the data type of is_retained
print(marketing['is_retained'].dtype)
# Convert is_retained to a boolean
marketing['is_retained'] = marketing['is_retained'].astype('bool')
# Check the data type of is_retained, again
print(marketing['is_retained'].dtype)

# Adding new columns
# Mapping for channels
channel_dict = {"House Ads": 1, "Instagram": 2,
                "Facebook": 3, "Email": 4, "Push": 5}
# Map the channel to a channel code
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)
# Import numpy
import numpy as np
# Add the new column is_correct_lang
marketing['is_correct_lang'] = np.where(marketing['language_displayed'] == marketing['language_preferred'], 'Yes', 'No')

# Date columns
# Import marketing.csv with date columns
marketing = pd.read_csv('marketing.csv', parse_dates=['date_served', 'date_subscribed', 'date_canceled'])
# Add a DoW column (day of week)
marketing['DoW'] = marketing['date_subscribed'].dt.dayofweek

# 3. Initial exploratory analysis
# groupby() and nunique() are great for exploratory analysis
# visualize results with 'plt' library

# EXAMPLE:
# Daily marketing reach by channel
# Group by date_served and count number of unique user_id's
daily_users = marketing.groupby(['date_served'])['user_id'].nunique()
# Print head of daily_users
print(daily_users.head())
import matplotlib.pyplot as plt
# Plot daily_subscribers
daily_users.plot()
# Include a title and y-axis label
plt.title('Daily users')
plt.ylabel('Number of users')
# Rotate the x-axis labels by 45 degrees
plt.xticks(rotation=45)
# Display the plot
plt.show()


# CHAPTER 2. Exploratory Analysis & Summary Statistics

# 1. Introduction to common marketing metrics
#

# 2.