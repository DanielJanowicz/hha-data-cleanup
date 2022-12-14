# Installing packages 
import pandas as pd
import datetime as dt
import uuid 
import numpy as np

# Importing data into variable
slm = pd.read_csv('data\School_Learning_Modalities.csv')

# Displays csv file information
slm 

# Printing out number of columns and rows in the csv
slm_rows = len(slm.axes[0])
slm_cols = len(slm.axes[1])

print("Number of Rows: " + str(slm_rows))
print("Number of Columns: " + str(slm_cols))

# Listing the column names
column_names = list(slm)
print("The columns in this csv are " + str(column_names))

# Removing special characters & whitespace
slm.columns = slm.columns.str.replace('[^A-Za-z0-9]+', '_')
slm.columns

# Changing Week data type from object to datetime
slm['Week'] = pd.to_datetime(slm['Week'])

# Checking column information for strings
slm.dtypes
slm_strings = slm.select_dtypes(include=['object']).columns 

# Cleaning whitespace or characters from object datatypes defined prior
slm['District_Name'] = slm['District_Name'].str.replace('[^A-Za-z0-9]+', '_')
slm['Learning_Modality'] = slm['Learning_Modality'].str.replace('[^A-Za-z0-9]+', '_')
slm['City'] = slm['City'].str.replace('[^A-Za-z0-9]+', '_')

# Replacing missing information with NaN
slm.isnull().sum()
slm.replace(to_replace='', value=np.nan, inplace=True)
slm.replace(to_replace=' ', value=np.nan, inplace=True)

# Dropping rows with missing information
slm.dropna(inplace=True)
slm.isnull().sum() 
slm 

# Dropping duplicate rows from the csv file
slm.drop_duplicates()

# Making a new column to define Learning modality as a boolean
slm['Modality_Inperson'] = slm["Learning_Modality"] == 'In_Person'
slm.head()