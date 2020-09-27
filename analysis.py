import pandas as pd
import os
import plotly.express as px


#cwd = os.getcwd()
#print (cwd)  


def get_data(file_name):

    wind_2007 = pd.read_csv('./data/wind_data/' + file_name)

    return wind_2007



def get_rose_diagram(data):
    
    
    
    
    fig = px.bar_polar(data, r = 'percentage%' , theta="drct",
                   color="Speed [m/s]", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r) #r="drct"

    

    return fig