# import the required libraries
import numpy as np  
import pandas as pd  


#%matplotlib inline  

import streamlit as st

import os

import analysis

def main():
    #df = load_data()

    st.header("Shell AI Hackathlon")

    year_list = os.listdir('./data/wind_data/')
    years = [y.split('_')[2].split('.csv')[0] for y in year_list]
    
    option = st.selectbox('Select the Year',(' ', '2007','2008'))
    st.write('You selected:', option)

    if option == ' ':
        print ('Please Select the Year')

    else:
        file_name = 'wind_data_' + option + '.csv' 
    
        file_name = 'wind_data_' + option + '.csv'
        data = analysis.get_data(file_name)
        data['sped'] = pd.to_numeric(data['sped'])
        bins = [*range(0, 30, 7)] 
        data['speed_binned'] = pd.cut(data['sped'], bins)

        bins_dir = [0, 11.25, 33.75, 56.25, 78.75,101.25,123.75,146.25,168.75,191.25,213.75,236.25,258.75,281.25,303.75,326.25,348.75, 360.00]
        bins_dir_labels = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','North']

        data['dir_binned'] = pd.cut(data['drct'],bins_dir, labels=bins_dir_labels)
        
        dfe = data[['speed_binned', 'drct','sped']].copy()
        print (dfe)
        dfe = dfe.groupby('speed_binned')['drct'].apply(lambda x: x.value_counts())
        dfe = pd.DataFrame(dfe).reset_index()
        
        dfe.rename(columns={'drct':'freq',
                            'speed_binned' : 'Speed [m/s]',
                            'level_1': 'drct'}, inplace=True)  #changing the last column to represent frequencies
        
        print (dfe)

        #g = dfe.groupby(['freq','drct']).count() #grouping
        #g.reset_index(inplace=True) 
        
        dfe['percentage'] = dfe['freq']/dfe['freq'].sum()
        dfe['percentage%'] = dfe['percentage']*100
        #g['Speed [m/s]'] = g['speed_binned']

        dfe.replace(r'North', 'N', regex=True)
        print(dfe['percentage'])
        
        st.subheader("Rose Diagram")
        st.plotly_chart(analysis.get_rose_diagram(dfe), width = 900, height = 900)

        analysis.get_rose_diagram(dfe).update_layout(width = 900, height = 900)

        analysis.get_rose_diagram(dfe).show()


        #st.subheader("Year Wise Analysis")

        #st.dataframe(analysis.get_data()) 

    

if __name__ == "__main__":
    main()




# C:\Users\khush\github_projects\python_3.7\streamlit C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py

# In Anaconda Terminal - C:\Users\khush> streamlit run C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py 