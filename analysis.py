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



def get_data(year):
    file_name = 'wind_data_' + year + '.csv'
    data = analysis.get_data(file_name)
    data['sped'] = pd.to_numeric(data['sped'])
    bins = [*range(0, 30, 7)] 
    data['speed_binned'] = pd.cut(data['sped'], bins)

    bins_dir = [0, 11.25, 33.75, 56.25, 78.75,101.25,123.75,146.25,168.75,191.25,213.75,236.25,258.75,281.25,303.75,326.25,348.75, 360.00]
    bins_dir_labels = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','North']

    data['dir_binned'] = pd.cut(data['drct'],bins_dir, labels=bins_dir_labels)
    
    dfe = data[['speed_binned', 'drct','sped']].copy()

    dfe = dfe.groupby('speed_binned')['drct'].apply(lambda x: x.value_counts())
    dfe = pd.DataFrame(dfe).reset_index()
    
    dfe.rename(columns={'drct':'freq',
                        'speed_binned' : 'Speed [m/s]',
                        'level_1': 'drct'}, inplace=True)  #changing the last column to represent frequencies
    


    
    dfe['percentage'] = dfe['freq']/dfe['freq'].sum()
    dfe['percentage%'] = dfe['percentage']*100


    dfe.replace(r'North', 'N', regex=True)
    #print(dfe['percentage'])
    
    
    return dfe
