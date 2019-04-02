
# coding: utf-8

# <p style="font-family: Arial; font-size:3.75em;color:purple; font-style:bold"><br>
# Pandas</p><br>
# 
# *pandas* is a Python library for data analysis. It offers a number of data exploration, cleaning and transformation operations that are critical in working with data in Python. 
# 
# *pandas* build upon *numpy* and *scipy* providing easy-to-use data structures and data manipulation functions with integrated indexing.
# 
# The main data structures *pandas* provides are *Series* and *DataFrames*. After a brief introduction to these two data structures and data ingestion, the key features of *pandas* this notebook covers are:
# * Generating descriptive statistics on data
# * Data cleaning using built in pandas functions
# * Frequent data operations for subsetting, filtering, insertion, deletion and aggregation of data
# * Merging multiple datasets using dataframes
# * Working with timestamps and time-series data
# 
# **Additional Recommended Resources:**
# * *pandas* Documentation: http://pandas.pydata.org/pandas-docs/stable/
# * *Python for Data Analysis* by Wes McKinney
# * *Python Data Science Handbook* by Jake VanderPlas
# 
# Let's get started with our first *pandas* notebook!

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# Import Libraries
# </p>

# In[4]:


import pandas as pd


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# Introduction to pandas Data Structures</p>
# <br>
# *pandas* has two main data structures it uses, namely, *Series* and *DataFrames*. 
# 
# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# pandas Series</p>
# 
# *pandas Series* one-dimensional labeled array. 
# 

# In[5]:


ser = pd.Series([100, 'foo', 300, 'bar', 500], ['tom', 'bob', 'nancy', 'dan', 'eric'])


# In[6]:


ser


# In[7]:


ser.index


# In[8]:


ser.loc[['nancy','bob']]


# ### Location of an object 
#  ser.loc['index']
#  ### Index location
#  ser.iloc[2]
#  ### check Existance
#  check if an object indexed as "Bob" exists in the series
#  'bob'in ser, returns true or false
#  

# In[ ]:


ser[[4, 3, 1]]


# In[ ]:


ser.iloc[2]


# In[ ]:


'bob' in ser


# In[ ]:


ser


# In[ ]:


ser * 2


# In[ ]:


ser[['nancy', 'eric']] ** 2


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# pandas DataFrame</p>
# 
# *pandas DataFrame* is a 2-dimensional labeled data structure.

# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold">
# Create DataFrame from dictionary of Python Series</p>

# In[9]:


d = {'one' : pd.Series([100., 200., 300.], index=['apple', 'ball', 'clock']),
     'two' : pd.Series([111., 222., 333., 4444.], index=['apple', 'ball', 'cerill', 'dancy'])}


# In[14]:


df = pd.DataFrame(d)
df


# In[15]:


df.index


# In[16]:


df.columns


# In[17]:


pd.DataFrame(d, index=['dancy', 'ball', 'apple'])


# In[29]:


pd.DataFrame(d, index=['dancy', 'ball', 'apple'], columns=['two', 'five'])


# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold">
# Create DataFrame from list of Python dictionaries</p>

# In[19]:


data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora': 10, 'alice': 20}]


# In[20]:


pd.DataFrame(data)


# In[21]:


pd.DataFrame(data, index=['orange', 'red'])


# In[22]:


pd.DataFrame(data, columns=['joe', 'dora','alice'])


# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold">
# Basic DataFrame operations</p>

# In[30]:


df


# In[31]:


df['one']


# In[32]:


df['three'] = df['one'] * df['two']
df


# In[33]:


df['flag'] = df['one'] > 250
df


# In[34]:


three = df.pop('three')


# In[35]:


three


# In[36]:


df


# In[37]:


del df['two']


# In[38]:


df


# In[39]:


df.insert(2, 'copy_of_one', df['one'])
df


# Get the first 2 values  of the column one  and assign it to the column one upper half
# 

# In[40]:


df['one_upper_half'] = df['one'][:2]df


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# Case Study: Movie Data Analysis</p>
# <br>This notebook uses a dataset from the MovieLens website. We will describe the dataset further as we explore with it using *pandas*. 
# 
# ## Download the Dataset
# 
# Please note that **you will need to download the dataset**. Although the video for this notebook says that the data is in your folder, the folder turned out to be too large to fit on the edX platform due to size constraints.
# 
# Here are the links to the data source and location:
# * **Data Source:** MovieLens web site (filename: ml-20m.zip)
# * **Location:** https://grouplens.org/datasets/movielens/
# 
# Once the download completes, please make sure the data files are in a directory called *movielens* in your *Week-3-pandas* folder. 
# 
# Let us look at the files in this dataset using the UNIX command ls.
# 

# In[ ]:


# Note: Adjust the name of the folder to match your local directory

get_ipython().system('ls ./movielens')


# In[ ]:


get_ipython().system('cat ./movielens/movies.csv | wc -l')


# In[ ]:


get_ipython().system('head -5 ./movielens/ratings.csv')

# Using the *read_csv* function in pandas, we will ingest these three files.

# In[41]:

# sep is the separator used
movies = pd.read_csv('./movielens/movies.csv', sep=',')
print(type(movies))
movies.head(15)


# In[42]:


# Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970

tags = pd.read_csv('./movielens/tags.csv', sep=',')
tags.head()


# In[ ]:


ratings = pd.read_csv('./movielens/ratings.csv', sep=',', parse_dates=['timestamp'])
ratings.head()


# In[ ]:


# For current analysis, we will remove timestamp (we will come back to it!)

del ratings['timestamp']
del tags['timestamp']




# In[ ]:


#Extract 0th row: notice that it is infact a Series

row_0 = tags.iloc[0]
type(row_0)


# In[ ]:


print(row_0)


# In[ ]:


row_0.index


# In[ ]:


row_0['userId']


# In[ ]:


'rating' in row_0


# In[ ]:


row_0.name


# In[ ]:


row_0 = row_0.rename('first_row')
row_0.name


# <h1 style="font-size:1.5em;color:#2467C0">DataFrames </h1>

# In[ ]:


tags.head()


# In[ ]:


tags.index


# In[ ]:


tags.columns


# In[ ]:


# Extract row 0, 11, 2000 from DataFrame

tags.iloc[ [0,11,2000] ]


# <h1 style="font-size:2em;color:#2467C0">Descriptive Statistics</h1>
# 
# Let's look how the ratings are distributed! 

# In[ ]:


ratings['rating'].describe()


# In[ ]:


ratings.describe()


# In[ ]:


ratings['rating'].mean()


# In[ ]:


ratings.mean()


# In[ ]:


ratings['rating'].min()


# In[ ]:


ratings['rating'].max()


# In[ ]:


ratings['rating'].std()


# In[ ]:


ratings['rating'].mode()


# In[ ]:


ratings.corr()


# In[ ]:


filter_1 = ratings['rating'] > 5
print(filter_1)
filter_1.any()


# In[ ]:


filter_2 = ratings['rating'] > 0
filter_2.all()


# <h1 style="font-size:2em;color:#2467C0">Data Cleaning: Handling Missing Data</h1>
# fill misising data gaps forward and backward

# ths last known value forward/before
df.fillna(method='ffill')
# the last known value back/after
df.fillna(method='backfill')



# Drop th efields with missing values

# rows with missing value eliminated
df.dropna(axis=0)
# columnwith misisng value eliminated
df.dropna(axis=0)
#Perform linear interpolation
df.interpolate()

# In[ ]:


movies.shape


# In[ ]:


#is any row NULL ?

movies.isnull().any()


# Thats nice ! No NULL values !

# In[ ]:


ratings.shape


# In[ ]:


#is any row NULL ?

ratings.isnull().any()


# Thats nice ! No NULL values !

# In[ ]:


tags.shape


# In[ ]:


#is any row NULL ?

tags.isnull().any()


# We have some tags which are NULL.

# In[ ]:


tags = tags.dropna()


# In[ ]:


#Check again: is any row NULL ?

tags.isnull().any()


# In[ ]:


tags.shape


# Thats nice ! No NULL values ! Notice the number of lines have reduced.

# <h1 style="font-size:2em;color:#2467C0">Data Visualization</h1>

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

ratings.hist(column='rating', figsize=(15,10))


# In[ ]:


ratings.boxplot(column='rating', figsize=(15,20))


# <h1 style="font-size:2em;color:#2467C0">Slicing Out Columns</h1>
#  

# In[ ]:


tags['tag'].head()


# In[ ]:


movies[['title','genres']].head()


# In[ ]:


ratings[-10:]


# In[ ]:


tag_counts = tags['tag'].value_counts()
tag_counts[-10:]


# In[ ]:


tag_counts[:10].plot(kind='bar', figsize=(15,10))


# <h1 style="font-size:2em;color:#2467C0">Filters for Selecting Rows</h1>

# In[ ]:


is_highly_rated = ratings['rating'] >= 4.0

ratings[is_highly_rated][30:50]


# In[ ]:


is_animation = movies['genres'].str.contains('Animation')

movies[is_animation][5:15]


# In[ ]:


movies[is_animation].head(15)


# <h1 style="font-size:2em;color:#2467C0">Group By and Aggregate </h1>

# In[ ]:


ratings_count = ratings[['movieId','rating']].groupby('rating').count()
ratings_count


# In[ ]:


average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()


# In[ ]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()


# How many ratings there are in our db


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.tail()


# <h1 style="font-size:2em;color:#2467C0">Merge Dataframes</h1>

# In[ ]:


tags.head()


# In[ ]:


movies.head()


# In[ ]:


t = movies.merge(tags, on='movieId', how='inner')
t.head()


# More examples: http://pandas.pydata.org/pandas-docs/stable/merging.html

# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"><br>
# 
# 
# Combine aggreagation, merging, and filters to get useful analytics
# </p>

# In[ ]:

# obtain the average of ratings by usierId
avg_ratings = ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
avg_ratings.head()


# In[ ]:

#Show/append the average rating in the movie dataframe
box_office = movies.merge(avg_ratings, on='movieId', how='inner')
box_office.tail()


# In[ ]:


is_highly_rated = box_office['rating'] >= 4.0

box_office[is_highly_rated][-5:]


# In[ ]:


is_comedy = box_office['genres'].str.contains('Comedy')

box_office[is_comedy][:5]


# In[ ]:


box_office[is_comedy & is_highly_rated][-5:]


# <h1 style="font-size:2em;color:#2467C0">Vectorized String Operations</h1>
# 

# In[ ]:


movies.head()


# <p style="font-family: Arial; font-size:1.35em;color:#2462C0; font-style:bold"><br>
# 
# Split 'genres' into multiple columns
# 
# <br> </p>

# In[ ]:


movie_genres = movies['genres'].str.split('|', expand=True)


# In[ ]:


movie_genres[:10]


# <p style="font-family: Arial; font-size:1.35em;color:#2462C0; font-style:bold"><br>
# 
# Add a new column for comedy genre flag
# 
# <br> </p>

# In[ ]:


movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')


# In[ ]:


movie_genres[:10]


# <p style="font-family: Arial; font-size:1.35em;color:#2462C0; font-style:bold"><br>
# 
# Extract year from title e.g. (1995)
# 
# <br> </p>

# In[ ]:


movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)


# In[ ]:


movies.tail()


# <p style="font-family: Arial; font-size:1.35em;color:#2462C0; font-style:bold"><br>
# 
# More here: http://pandas.pydata.org/pandas-docs/stable/text.html#text-string-methods
# <br> </p>


# 

# In[ ]:
# <h1 style="font-size:2em;color:#2467C0">Parsing Timestamps</h1>

# Timestamps are common in sensor data or other time series datasets.
# Let us revisit the *tags.csv* dataset and read the timestamps!

tags = pd.read_csv('./movielens/tags.csv', sep=',')


# In[ ]:


tags.dtypes


# <p style="font-family: Arial; font-size:1.35em;color:#2462C0; font-style:bold">
# 
# Unix time / POSIX time / epoch time records 
# time in seconds <br> since midnight Coordinated Universal Time (UTC) of January 1, 1970
# </p>

# In[ ]:


tags.head(5)


# In[ ]:

tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit='s')
#we change the initial format int64 to <M8 to be readable 
# Data Type datetime64[ns] maps to either <M8[ns] or >M8[ns] depending on the hardware

tags['parsed_time'].dtype

tags.head(2)

# Selecting rows based on timestamps

greater_than_t = tags['parsed_time'] > '2015-02-01'

selected_rows = tags[greater_than_t]

tags.shape, selected_rows.shape

# Sorting the table using the timestamps

tags.sort_values(by='parsed_time', ascending=True)[:10]


#Average Movie Ratings over Time 
# Are Movie ratings related to the year of launch?
average_rating = ratings[['movieId','rating']].groupby('movieId', as_index=False).mean()
average_rating.tail()


# In[]:


joined = movies.merge(average_rating, on='movieId', how='inner')
joined.head()
joined.corr()


# In[ ]:
movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)

yearly_average = joined[['year','rating']].groupby('year', as_index=False).mean()
yearly_average[:10]


# In[ ]:


yearly_average[-20:].plot(x='year', y='rating', figsize=(15,10), grid=True)


# <p style="font-family: Arial; font-size:1.35em;color:#2462C0; font-style:bold">
# 
# Do some years look better for the boxoffice movies than others? <br><br>
# 
# Does any data point seem like an outlier in some sense?
# 
# </p>
