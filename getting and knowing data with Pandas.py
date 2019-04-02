
## Getting and Knowing your Data with pandas


import pandas as pd
import numpy as np

## getting the data
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

# see the 1st 10 entries
chipo.head(10)

# number of observations in the data sheet
chipo.shape[0] 
# or chipo.info()

#number of cooumns
chipo.shape[1]

# print all the columns' names
chipo.columns

# Most oredered item
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

#revenue in the whole period
revenue = (chipo['quantity']* chipo['item_price']).sum()
print('Revenue was: $' + str(np.round(revenue,2)))

# how many different items are sold
chipo.item_name.value_counts().count()

# create a 2x2 array of zeros
ex1 = np.zeros((2,2))      
print(ex1) 
# create a 2x2 array filled with 9.0
ex2 = np.full((2,2), 9.0)  
print(ex2)
# create a 2x2 matrix with the diagonal 1s and the others 0
ex3 = np.eye(2,2)
print(ex3) 
# create an array of ones
ex4 = np.ones((3,2))
print(ex4)
# create an array of random floats between 0 and 1
ex5 = np.random.random((2,2))
print(ex5)  
# create a 3x2 array
an_array = np.array([[11,12], [21, 22], [31, 32]])
print(an_array)

# create a filter which will be boolean values for whether each element meets this condition
filter = (an_array > 15)
filter
# we can now select just those elements which meet that criteria
print(an_array[filter])

# For short, we could have just used the approach below without the need for the separate filter array.
an_array[(an_array % 2 == 0)]

# datatypes
ex10 = np.array([11, 12]) # Python assigns the  data type
print(ex10.dtype)

ex11 = np.array([11, 21], dtype=np.int64) #You can also tell Python the  data type
print(ex11.dtype)



