import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Find path to the csv file
covid19_path="https://project-pandemix.s3.us-east-2.amazonaws.com/COVID-10+Cases+v2.csv"

# Read in csv and print head of df
covid19_df = pd.read_csv(covid19_path)

# Create DB Connection
rds_connection_string = "root:postgress@corona.cuo7ivhfh3jn.us-east-1.rds.amazonaws.com:5432/corona"
engine = create_engine(f'postgresql://{rds_connection_string}')

# If corona_db already exists, delete it
with engine.connect() as connection:
    result = connection.execute("DROP TABLE IF EXISTS corona_db;")

# Select necessary columns and renaming if needed
covid19_df_2 = covid19_df[['Date', 'Case_Type', 'Cases', 'Difference', 'Country_Region',
       'Province_State', 'Admin2']]
covid19_df_2 = covid19_df_2.rename(columns = {'Cases':'Cumulative_Cases','Difference':'Daily_Cases',
                                                              'Country_Region':'Country', 'Province_State':'State',
                                                              'Admin2':'County'}) 

# Fill in NaN values in columns so they dont dropped when pivoting the df
covid19_df_2 = covid19_df_2.fillna('None')

# Pivot df so Case_Type (Deaths and Confirmed) become columns of their own
covid19_pivoted_df = covid19_df_2.pivot_table(index=['Date', 'Country', 'State', 'County'], 
                        columns='Case_Type', 
                        values='Daily_Cases',
                        aggfunc=sum)

# Reset index so we dont have grouped columns
covid19_pivoted_df.reset_index(inplace=True)

# Now we want to get rid of any rows that have zero (0) on noth the Confirmed and Deaths columns, and reset the index
cols_of_interest = ['Confirmed', 'Deaths']
covid19_cleaned_df = covid19_pivoted_df[(covid19_pivoted_df[cols_of_interest] != 0).any(axis=1)]
covid19_cleaned_df = covid19_cleaned_df.reset_index(drop=True)

# Save cleaned df into new csv
covid19_cleaned_df.to_csv('corona.csv', index=False)
covid19_cleaned_df.to_sql(name='corona_db', con=engine, if_exists='append', index=False)
