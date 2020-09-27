import pandas as pd
import os


#cwd = os.getcwd()
#print (cwd)  

def get_data():

    wind_2007 = pd.read_csv('./data/wind_data/wind_data_2007.csv')
return wind_2007