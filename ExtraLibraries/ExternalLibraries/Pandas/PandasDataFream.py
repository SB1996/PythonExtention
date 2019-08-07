# Python | Dealing with Rows and Columns in Pandas DataFrame
import pandas as pd

# Details list ...
name = ['Santanu', 'Patrha', 'Titu', 'Biki', 'Banka']
age = [23, 24, 25, 19, 20]
id = ['IT007', 'CS009', 'Sec006', 'G008', 'N003']
cources = ['IT', 'CS', 'Math', 'Economies', 'EE']
degree = ['B.Tech', 'Diploma', 'Graduate', 'Pass','ITI']

# data Dictionary ....
data = {'Name' : name,
        'Age' : age,
        'ID' : id,
        'Cource' : cources,
        'Degree' : degree,}
detailsData = pd.DataFrame(data)
print(detailsData)
# ______________________________________________________________________________________________________________________
# Dealing with Columns :  In order to deal with columns, we perform basic operations on columns
#                         like => 1. selecting
#                                 2. deleting
#                                 3. adding
#                                 4. renaming.
#
# 1. Column Selection : In Order to select a column in Pandas DataFrame, we can either access the columns by calling
#                       them by their columns name.

# select two columns (Name, Age) => detailsData[['Name', 'Age']]
print("_________________________________")
print(detailsData[['Name', 'Age']])
#
# 2. Column Addition : In Order to add a column in Pandas DataFrame, we can declare a new list as a column and add to
#                      a existing Dataframe.

print("_________________________________")
# add data to datafream...
address = ['Delhi', 'Bangalore', 'Chennai', 'Mumbai', 'Kolkata']
# Using 'Address' as the column name and equating it to the list
detailsData['Address'] = address
print(detailsData)

# Column Deletion : In Order to delete a column in Pandas DataFrame, we can use the drop() method. Columns is deleted by
#                   dropping columns with column names.
#
print("_________________________________")
detailsData.drop(['Age'], axis = 1, inplace = True)
print(detailsData)
# ______________________________________________________________________________________________________________________
# Dealing with Row :  In order to deal with Rows, we perform basic operations on Rows
#                         like => 1. selecting
#                                 2. deleting
#                                 3. adding
#                                 4. renaming.

# 1. Row Selection : Pandas provide a unique method to retrieve rows from a Data frame.DataFrame.loc[] method is used
#                    to retrieve rows from Pandas DataFrame. Rows can also be selected by passing integer location to
#                    an iloc[] function.
#
#       Name      ID     Cource    Degree    Address
# 0  Santanu   IT007         IT    B.Tech      Delhi
# 1   Patrha   CS009         CS   Diploma  Bangalore
# 2     Titu  Sec006       Math  Graduate    Chennai
# 3     Biki    G008  Economies      Pass     Mumbai
# 4    Banka    N003         EE       ITI    Kolkata
print("_________________________________")
print(detailsData.iloc[4])

# 2. Row Addition : In Order to add a Row in Pandas DataFrame, we can concat the old dataframe with new one.
print("_________________________________")
addData = {'Name' : 'Rimi',
           'ID' : 'E001',
           'Cource' : 'Geography',
           'Degree' : 'B.a',
           'Address' : 'Burdwan'}
new_row = pd.DataFrame(addData, index =[0])
# simply concatenate both dataframes
detailsData = pd.concat([new_row, detailsData]).reset_index(drop = True)

print(detailsData)

# 3. Row Deletion : In Order to delete a row in Pandas DataFrame, we can use the drop() method. Rows is deleted
#                   by dropping Rows by index label.

print("_________________________________")
detailsData.drop(['Rimi'], axis = 1, inplace = True)
print(detailsData)