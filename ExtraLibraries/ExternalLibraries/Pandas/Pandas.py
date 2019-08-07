# Python | Pandas DataFrame
#
# Pandas DataFrame : is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled
#                    axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned
#                    in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components,
#                    the data, rows, and columns.
#

import pandas as pd

# Creating an empty dataframe

dataFrame = pd.DataFrame()
# print(dataFrame)


print("___________________________________________")
# Creating a dataframe using List

name = ['Santanu', 'Patrha', 'Titu', 'Biki', 'Banka']
nameDataFrame = pd.DataFrame(name)
print(nameDataFrame)


print("___________________________________________")
# Creating DataFrame from dict of ndarray/lists : To create DataFrame from dict of narray/list, all the narray must be
#                                                 of same length. If index is passed then the length index should be
#                                                 equal to the length of arrays. If no index is passed, then by default,
#                                                 index will be range(n) where n is the array length.

# intialise data of lists...
data = {'Name': ['Santanu', 'Patrha', 'Titu', 'Biki', 'Banka'], 'Age': [23, 24, 25, 19, 20]}
# Create DataFrame
delailsFrame = pd.DataFrame(data)
print(delailsFrame)

print("___________________________________________")
name = ['Santanu', 'Patrha', 'Titu', 'Biki', 'Banka']
age = [23, 24, 25, 19, 20]
id = ['IT007', 'CS009', 'Sec006', 'G008', 'N003']
cources = ['IT', 'CS', 'Math', 'Economies', 'EE']
degree = ['B.Tech', 'Diploma', 'Graduate', 'Pass','ITI']

data = {'Name' : name,
        'Age' : age,
        'ID' : id,
        'Cource' : cources,
        'Degree' : degree,}
detailsData = pd.DataFrame(data)
print(detailsData)
