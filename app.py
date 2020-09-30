# import the required libraries
import numpy as np  
import pandas as pd  


#%matplotlib inline  

import streamlit as st

import os

import analysis

def main():
    #df = load_data()

    st.sidebar.header("Shell AI Hackathlon")

    year_list = os.listdir('./data/wind_data/')
    years = [y.split('_')[2].split('.csv')[0] for y in year_list]
    
    
    plot_option = st.sidebar.selectbox('Select the Plot',(' ', 'Rose Diagram'))

    if plot_option == ' ':
        print ('Please Select the Plot')

    elif plot_option == 'Rose Diagram':

    
        year_option = st.sidebar.selectbox('Select the Year',(' ', '2007','2008','2009','2013','2014','2015','2017'))
        #st.write('Rose diagram  selected:', year_option)

        if year_option == ' ':
            print ('Please Select the Year')

        else:
            rose_diagram_header = 'Rose Diagram for the year: ' + year_option
            st.subheader(rose_diagram_header)

            dfe = analysis.analyze_rose_diagram_data(year_option)
            st.plotly_chart(analysis.get_rose_diagram(dfe), width = 900, height = 900)

            #analysis.get_rose_diagram(dfe).update_layout(width = 900, height = 900)
            #analysis.get_rose_diagram(dfe).show()
            
            st.plotly_chart(analysis.get_time_plot(year_option), width = 900, height = 1500)

            #analysis.get_time_plot(year_option).update_layout(width = 900, height = 1500)
            #analysis.get_time_plot(year_option).show()

if __name__ == "__main__":
    main()



# C:\Users\khush\github_projects\python_3.7\streamlit C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py

# In Anaconda Terminal - C:\Users\khush> streamlit run C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py 