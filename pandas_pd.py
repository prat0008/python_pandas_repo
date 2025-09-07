from urllib.request import urlretrieve
import pandas as pd

# Use RAW file link from GitHub
url = 'https://raw.githubusercontent.com/the-stranger-web/jovian_Data_Analyst/main/italy-covid-daywise.csv'

# Save the file locally with a name
urlretrieve(url, 'italy-covid-daywise.csv')

# Now read the saved file
covid_df = pd.read_csv('italy-covid-daywise.csv')

print(covid_df.head())
