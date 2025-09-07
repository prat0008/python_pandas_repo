from urllib.request import urlretrieve
import pandas as pd

# Use RAW file link from GitHub
url = 'https://raw.githubusercontent.com/the-stranger-web/jovian_Data_Analyst/main/italy-covid-daywise.csv'

# Save the file locally with a name
urlretrieve(url, 'italy-covid-daywise.csv')

# Now read the saved file
covid_df = pd.read_csv('italy-covid-daywise.csv')

#prints the data from the csv file
#print(covid_df)

#to view some basic information about the dataframe we use .info method
#print(covid_df.info())

#to view the statistical info like mean,standard deviation,min/max values,
#and no. of non empty values using the .describe method.
#print(covid_df.describe())

#to retrieve the no. of rows and columns within the df.
#print(covid_df.shape)

#columns property contains the list of columns within the df.
#print(covid_df.columns)