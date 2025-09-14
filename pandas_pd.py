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

# Read the downloaded file
covid_df = pd.read_csv('italy-covid-daywise.csv')
#print(covid_df)
#print(covid_df.info())
#print(covid_df.describe())
#print(covid_df.columns)
#print(covid_df.shape)

#retrieving  data from dataframe
"""covid_data_dict={
    'date':['2020-08-30','2020-08-31','2020-09-01','2020-09-02'],
    'new_cases':[1444,1365,996,975,1326],
    'new_deaths':[1,4,6,8,6],
    'new_tests':[563451,42583,54395, None,None]
}"""

#print(covid_df['new_cases'])
#print(covid_df['new_cases'][246])
#print(covid_df['new_tests'][240])

#pandas also provides the .at method to directly retrieve 
#at specific row and column

#print(covid_df.at[246,'new_cases'])
#print(covid_df.at[240,'new_tests'])

#below line works without indexing notation. this method only works for
#columns whose namse does not contain special character.
#print(covid_df.new_cases)

#to access more than one column write the below line
#cases_df=covid_df[['date','new_cases']]
#print(cases_df)


#sometimes you might need a full copy of data frame,
#in which case we can use the 'copy' method.
#the data within 'covid_df_copy' is completely separate
#from covid_df and changing values inside one of them 
#will not affect the other

#covid_df_copy=covid_df.copy()


#to access specific row of data pandas provides .loc method
#each retrieve method is  a series object
#print(covid_df.loc[243])
#print(type(covid_df.loc[243]))

#to view some first or last few rows of data we use .head() 
#and .tail() methods.

#print(covid_df.head(4))
#print(covid_df.tail(5))

#if pandas does not find any values in the csv file or blank row or column
#if fills that blank with NaN 
#to check first index which does not contain a Nan we use
#first_valid_index method of series
#print(covid_df.new_tests.first_valid_index())

#to check we print first few and after values from that index
#print(covid_df.loc[108:113])

#to get the random sample data we use .sample() method
#print(covid_df.sample(10))

#analyzing the dataframe
#what is the total number of reported cases and deaths to covid-19 daily?
#total_cases= covid_df.new_cases.sum()
#total_deaths= covid_df.new_deaths.sum()
#print("the total no. of reported cases is",total_cases, "and the number of reported deaths is",total_deaths)

#what is the overall death rate(ratio of reported deaths to reported cases?
#death_rate=covid_df.new_deaths.sum()/covid_df.new_cases.sum()*100
#print("death rate is",death_rate,"%")

#what is the overall no. of tests conducted?
#a total of 935310 tests were conducted before 
#daily tests numbers were being reported

#initial_tests=935310
#total_tests=initial_tests + covid_df.new_tests.sum()
#print("total tests",total_tests)

#what fraction of test return a postive result?
#initial_tests=935310
#total_tests=initial_tests + covid_df.new_tests.sum()
#total_cases= covid_df.new_cases.sum()
#positive_result=total_cases/total_tests*100
#print(positive_result,"%""of tests in italy led to a positive diagnosis")

#querying and sorting rows
#eg if we want to look the days which have 1000 reported cases.
#we can use a boolean expression to check which rows satisfy the criterion.
#it will return the True when condition satsifies otherwise returns False.
#high_new_cases=covid_df.new_cases>1000
#print(high_new_cases)
#print(covid_df[high_new_cases])#returns only those rows which satisfies the condition.
#we can write the above two lines in a single line
#high_new_cases=covid_df[covid_df.new_cases>1000]
#print(high_new_cases)

#let's try to determine the days when the ratio of cases reported to tests conducted is higher
#than the overall postive rate.
#initial_tests=935310
#total_tests=initial_tests + covid_df.new_tests.sum()
#total_cases= covid_df.new_cases.sum()
#positive_result=total_cases/total_tests
#high_ratio_df = covid_df[covid_df .new_cases / covid_df.new_tests>positive_result]
#print(high_ratio_df)

#we can use this series to add a new column in the dataframe
#covid_df['positive_result']=covid_df.new_cases / covid_df.new_tests
#print(covid_df)

#to remove the postive_result from the dataframe
#covid_df.drop(columns=['positive_result'],inplace=True)
#print(covid_df)

#sorting rows using columns values
#let's sort to identify the days with the highest no. of cases
#then chainw it with head method to get the 10 days with most cases.
#print(covid_df.sort_values('new_cases',ascending=False).head(10))

#let's compare it with the highest no. of deaths recorded.
#print(covid_df.sort_values('new_deaths',ascending=False).head(10))

#let's see the least no. of cases
#print(covid_df.sort_values('new_cases').head(10))
#print(covid_df.loc[169:180])
#the value at 172 is -148 is might be the accouning error or data entry error
#1. replace with zero
#2. replace with the average of the entire column
#3. replace with the average of the values on the previous and next date
#4. discard the row entirely
#we use third method to correct it,can be fixed by taking the average of previous and next date value
#covid_df.at[172,'new_cases']=(covid_df.at[171,'new_cases']+covid_df.at[172,'new_cases'])/2
#print(covid_df.loc[169:180])

#working with dates
#print(covid_df.date)
#the datatype of date is currently is object so pandas does not know that this 
#column is date. we can convert it into a datetime column using the pd.to_datetime method.
#covid_df['date'] = pd.to_datetime(covid_df.date)
#print(covid_df['date'])

#we can now extract the different parts of the 
#data into separate columns using the DatetimeIndex class.
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
#print(covid_df)

#let's check the query of the month may
#we can query the rows for may
#choose a subset of columns that we want to aggregate and use the sum method of 
#the data frame to get the sum values in each chosen column
#query for the rows of may
#covid_df_may=covid_df[covid_df.month==5]

#extract the subset of columns to be aggregated 
#covid_df_may_metrics=covid_df_may[['new_cases','new_deaths','new_tests']]

#get the column wise sum
#covid_may_totals=covid_df_may_metrics.sum()
#print(covid_may_totals)
#print(type(covid_may_totals))

#the above operations can be combined in single statement
#print(covid_df[covid_df.month==5][['new_cases','new_deaths','new_tests']].sum())


#let's check if the number of cases reported on sundays is 
#higher than the average number of cases reported every day
#this time we might want to aggregate using the .mean method.

#overall average
#print(covid_df.new_cases.mean())

#average for sundays
#print(covid_df[covid_df.weekday==6].new_cases.mean())

#grouping and aggregation
#we might want to summarize the daywise data and create a new dataframe with month-wise data.
#this is where the groupby function is useful.
#along with grouping, we need to specify a way to aggregate the data for each group

#covid_month_df= covid_df.groupby('month')[['new_cases','new_deaths','new_tests']].sum()
#print(covid_month_df)

#instead of aggregationg by sum, we can also aggregate by mean
#covid_month_mean_df= covid_df.groupby('weekday')[['new_cases','new_deaths','new_tests']].mean()
#print(covid_month_mean_df)

#apart from grouping another form of aggregation is to calculate the 
#running or cummulative sum of cases, tests or deaths up to current
#date or each row. this can be done using cumsum method.
#let's add 3 new columns:
#total_cases, total_deaths, total_tests
initial_tests=935310
covid_df['total_cases']=covid_df.new_cases.cumsum()
covid_df['total_deaths']=covid_df.new_deaths.cumsum()
covid_df['total_tests']=covid_df.new_tests.cumsum() + initial_tests
#print(covid_df) 


#merging data from multiple sources
#url = 'https://raw.githubusercontent.com/the-stranger-web/jovian_Data_Analyst/main/italy-covid-daywise.csv'
url = 'https://raw.githubusercontent.com/the-stranger-web/jovian_Data_Analyst/main/location.csv'

# Save the file locally with a name
urlretrieve(url, 'location.csv')

# Now read the saved file
locations_df = pd.read_csv('location.csv')

#print(locations_df)
#print(locations_df[locations_df.location=='Italy'])

#let's insert a location column in the covid_df dataframe with all values set to Italy.
covid_df['location']= 'Italy'
#print(covid_df)

#we can now add the columns from locations_df into covid_df using  the .merge method.
merged_df=covid_df.merge(locations_df,on="location")
#print(merged_df)

#we can now calculate the metrics like 
#cases per million, deaths per million, tests per  million
merged_df['cases_per_million']=merged_df.total_cases*1e6/merged_df.population
merged_df['deaths_per_million']=merged_df.total_deaths*1e6/merged_df.population
merged_df['tests_per_million']=merged_df.total_tests*1e6/merged_df.population
print(merged_df)