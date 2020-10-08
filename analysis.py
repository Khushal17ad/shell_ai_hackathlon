import pandas as pd
import os
import plotly.express as px
import plotly.graph_objs as go


#cwd = os.getcwd()
#print (cwd)  


def get_data(file_name):

    wind_data = pd.read_csv('./data/wind_data/' + file_name)
    wind_data.rename(columns={'sped':'Speed [m/s]'},inplace=True)
    print (wind_data.columns)
    return wind_data



def get_rose_diagram(data):
    
    fig = px.bar_polar(data, r = 'percentage%' , theta="drct",
                   color="Speed [m/s]", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r) #r="drct"

    return fig

def analyze_rose_diagram_data(year):
    file_name = 'wind_data_' + year + '.csv'
    data = get_data(file_name)
    data['Speed'] = pd.to_numeric(data['Speed [m/s]'])
    bins = [*range(0, 30, 7)] 
    data['speed_binned'] = pd.cut(data['Speed'], bins)

    bins_dir = [0, 11.25, 33.75, 56.25, 78.75,101.25,123.75,146.25,168.75,191.25,213.75,236.25,258.75,281.25,303.75,326.25,348.75, 360.00]
    bins_dir_labels = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','North']

    data['dir_binned'] = pd.cut(data['drct'],bins_dir, labels=bins_dir_labels)
    
    dfe = data[['speed_binned', 'drct','Speed']].copy()

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

def get_time_plot(year):
    file_name = 'wind_data_' + year + '.csv'
    data = get_data(file_name)

    fig = px.line(data, x='date', y="Speed [m/s]")

    return fig


def create_bins(lower_bound, width, quantity):
    """ create_bins returns an equal-width (distance) partitioning. 
        It returns an ascending list of tuples, representing the intervals.
        A tuple bins[i], i.e. (bins[i][0], bins[i][1])  with i > 0 
        and i < quantity, satisfies the following conditions:
            (1) bins[i][0] + width == bins[i][1]
            (2) bins[i-1][0] + width == bins[i][0] and
                bins[i-1][1] + width == bins[i][1]
    """
    

    bins = []
    for low in range(lower_bound, 
                     lower_bound + quantity*width + 1, width):
        bins.append((low, low+width))
    return bins

def find_bin(value, bins):
    """ bins is a list of tuples, like [(0,20), (20, 40), (40, 60)],
        binning returns the smallest index i of bins so that
        bin[i][0] <= value < bin[i][1]
    """
    
    for i in range(0, len(bins)):
        if bins[i][0] <= value < bins[i][1]:
            return i
    return -1


def heat_map_analysis(year):
    file_name = 'wind_data_' + year + '.csv'
    data = get_data(file_name)
    
    data['Speed'] = pd.to_numeric(data['Speed [m/s]'])
    bins = [*range(0, 32, 2)] 
    data['speed_binned'] = pd.cut(data['Speed'], bins)#

    data['speed_binned_codes'] = data['speed_binned'].cat.codes 
    data['speed_binned_codes'] = data['speed_binned_codes'] * 2
    
    data = data.sort_values(by='speed_binned_codes')
    trace = go.Heatmap(z = data['Speed'],
                   y = data['drct'],
                   x = data['speed_binned_codes'],
                   colorscale="Viridis")
    fig = go.Figure(data=[trace],
                    layout={'xaxis': {'type': 'category'}})

    
    return fig
