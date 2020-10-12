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

    st.sidebar.subheader("The data visualized in this web app is referenced from Shell AI Hackathlon:")
    st.sidebar.markdown(
    """<a href="https://www.hackerearth.com/challenges/competitive/shell-hackathon/?utm_source=shell&utm_medium=redirect&utm_content=target&utm-campaign=signupIconlistControl&utm_term=ExpA">Shell AI</a>""", unsafe_allow_html=True,
)


    year_list = os.listdir('./data/wind_data/')
    years = [y.split('_')[2].split('.csv')[0] for y in year_list]
    
    analysis_type = st.sidebar.selectbox('Select the Analysis Type',(' ', 'Single Year', 'Multi Year'))

    if analysis_type == ' ':
        print ('Please Select the Analysis Type')

    elif analysis_type == 'Single Year':

    

        year_option = st.sidebar.selectbox('Select the Year',(' ', '2007','2008','2009','2013','2014','2015','2017'))

        #year_option = '2007'

        if year_option == ' ':
            print ('Please Select the Year')

        else:
            rose_diagram_header = 'Rose Diagram for the year: ' + year_option
            st.subheader(rose_diagram_header)

            dfe = analysis.analyze_rose_diagram_data(year_option)
            st.plotly_chart(analysis.get_rose_diagram(dfe), width = 600, height = 600)
            
            heat_diagram_header = 'Heat Map of Wind Speed and Direction for the year: ' + year_option
            st.subheader(heat_diagram_header)
            st.plotly_chart(analysis.heat_map_analysis(year_option), width = 1500, height = 800)

            frequency_diagram_header = 'Histogram of Wind Speed for the year: ' + year_option
            st.subheader(frequency_diagram_header)
            st.plotly_chart(analysis.frequency_analysis(year_option), width = 1500, height = 600)

            time_diagram_header = 'Time Series of for the year: ' + year_option
            st.subheader(time_diagram_header)
            st.plotly_chart(analysis.get_time_plot(year_option), width = 1500, height = 600)

            #analysis.get_time_plot(year_option).update_layout(width = 900, height = 1500)
            #analysis.get_time_plot(year_option).show()
            #analysis.heat_map_analysis(year_option).show()
    
    else:
        pass

if __name__ == "__main__":
    main()

#main()

# C:\Users\khush\github_projects\python_3.7\streamlit C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py

# In Anaconda Terminal - C:\Users\khush> streamlit run C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py 

#https://www.ul.com/apps/wind-data-management-dashboard