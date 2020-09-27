import pandas as pd
import os
import plotly.express as px


#cwd = os.getcwd()
#print (cwd)  

def get_data():

    wind_2007 = pd.read_csv('./data/wind_data/wind_data_2007.csv')

    
    fig = px.bar_polar(wind_20007, r="frequency", theta="drct",
                   color="speed", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)

    return fig