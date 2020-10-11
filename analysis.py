import pandas as pd
import os
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots



#cwd = os.getcwd()
#print (cwd)  


def get_data(file_name):

    wind_data = pd.read_csv('./data/wind_data/' + file_name)
    wind_data.rename(columns={'sped':'Wind Speed [m/s]'},inplace=True)
    return wind_data



def get_rose_diagram(data):
    
    fig = px.bar_polar(data, r = 'percentage%' , theta="drct",
                   color="Wind Speed [m/s]", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r) #r="drct"

    return fig

def analyze_rose_diagram_data(year):
    file_name = 'wind_data_' + year + '.csv'
    data = get_data(file_name)

    data['Speed'] = pd.to_numeric(data['Wind Speed [m/s]'])
    bins = [*range(0, 30, 7)] 
    data['speed_binned'] = pd.cut(data['Speed'], bins)

    bins_dir = [0, 11.25, 33.75, 56.25, 78.75,101.25,123.75,146.25,168.75,191.25,213.75,236.25,258.75,281.25,303.75,326.25,348.75, 360.00]
    bins_dir_labels = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','North']

    data['dir_binned'] = pd.cut(data['drct'],bins_dir, labels=bins_dir_labels)
    
    dfe = data[['speed_binned', 'drct','Speed']].copy()

    dfe = dfe.groupby('speed_binned')['drct'].apply(lambda x: x.value_counts())
    dfe = pd.DataFrame(dfe).reset_index()
    
    dfe.rename(columns={'drct':'freq',
                        'speed_binned' : 'Wind Speed [m/s]',
                        'level_1': 'drct'}, inplace=True)  #changing the last column to represent frequencies
    
    dfe['percentage'] = dfe['freq']/dfe['freq'].sum()
    dfe['percentage%'] = dfe['percentage']*100

    dfe.replace(r'North', 'N', regex=True)
    #print(dfe['percentage'])

    return dfe

def get_time_plot(year):
    file_name = 'wind_data_' + year + '.csv'
    data = get_data(file_name)

    fig = px.line(data, x='date', y="Wind Speed [m/s]")

    return fig


def heat_map_analysis(year):
    file_name = 'wind_data_' + year + '.csv'
    data = get_data(file_name)
    
    data['Speed'] = pd.to_numeric(data['Wind Speed [m/s]'])
    bins = [*range(0, 32, 2)] 
    data['speed_binned'] = pd.cut(data['Speed'], bins)#

    data['speed_binned_codes'] = data['speed_binned'].cat.codes 
    data['speed_binned_codes'] = data['speed_binned_codes'] * 2
    
    data = data.sort_values(by='speed_binned_codes')
    trace = go.Heatmap(z = data['Speed'],
                   y = data['drct'],
                   x = data['speed_binned_codes'],
                   colorscale="Viridis",
                   colorbar={"title": 'Wind Speed (m/s)'})
    fig = go.Figure(data=[trace],
                    layout={'xaxis': {'title' : 'Wind Speed (m/s)','type': 'category'},
                    'yaxis': {'title' : 'Direction'}})

    
    return fig

def frequency_analysis(year_list):
    

    fig = make_subplots(rows=1, cols=1)
    
    for year in year_list:
        file_name = 'wind_data_' + year + '.csv'
        data = get_data(file_name)

        fig.add_trace(go.Histogram(x=data['Wind Speed [m/s]'], histnorm='percent',
                        xbins=dict(start=0,
                                    size=2,
                                    end=data['Wind Speed [m/s]'].max()),
                        marker=dict(color='rgb(50, 50, 125)'),name = year), row  = 1 , col = 1)

        layout = go.Layout(
            title="Histogram with Frequency Count"
        )

    #fig = go.Figure(data=go.Data([trace]), layout=layout)

    """group_labels = ['Wind Speed'] 
    fig = ff.create_distplot([data['Wind Speed [m/s]']], group_labels,  bin_size=.2)
    """

    return fig



#print (frequency_analysis(['2007','2008','2009']).show())
