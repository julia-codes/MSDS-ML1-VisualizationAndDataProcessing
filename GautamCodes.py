import pandas as pd
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from plotly.offline import iplot_mpl

# Read original CSV
df = pd.read_csv('Crime_Data_from_2010_to_2019.csv')

# Extract year and make it an attribute
df['year'] = pd.DatetimeIndex(df['Date Rptd']).year

# Extract data set for 2019 year only to Crime2019.csv
df.loc[df['year'] == 2019].to_csv('Crime2019.csv')

# Reload the 2019 data only in df. Note we may need to get rid of df
# before reusing for smaller dataset. In original code, i start my coding 
# again i.e. essentially start from below line
df = pd.read_csv('Crime2019.csv') # read in the csv file

# Plot areas with worst crime, ordered by reducing crime in bar format.
plt.style.use('ggplot')

df_area = df.groupby(by=['AREA NAME'])
area_crime_count = df_area['AREA NAME'].count()
area_crime_count.sort_values().plot.barh(title= 'Crime Reported (2019)')

# Interesting violin plot with both Time and Area information
f, ax = plt.subplots(figsize=(20, 9))
sns.violinplot(x="AREA NAME", y="TIME OCC", data=df)

# Working on kernal density plot. So far don't have working code.

#### Watch this space for my code ####
