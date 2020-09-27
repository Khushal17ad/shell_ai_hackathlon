import pandas as pd
import os
import plotly.express as px


#cwd = os.getcwd()
#print (cwd)  

def get_data():

    wind_2007 = pd.read_csv('./data/wind_data/wind_data_2007.csv')

    return wind_2007



def get_rose_diagram(data):
    
    fig = px.bar_polar(data, r="drct", theta="drct",
                   color="speed_bins")
                   #color_discrete_sequence= px.colors.sequential.Plasma_r)
    

    return fig