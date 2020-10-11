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

    st.sidebar.subheader("The data visualized in this website is referenced from Shell AI Hackathlon:")
    st.sidebar.markdown(
    """<a href="https://www.shell.in/energy-and-innovation/ai-hackathon.html#:~:text=Description%3A,and%20is%20open%20for%20participation!&text=Energy%20transition%20and%20digitalisation%20are,trends%20in%20the%20coming%20decades.">Shell AIcom</a>""", unsafe_allow_html=True,
)


    year_list = os.listdir('./data/wind_data/')
    years = [y.split('_')[2].split('.csv')[0] for y in year_list]
    
    #plot_option = st.sidebar.selectbox('Select the Plot',(' ', 'Rose Diagram'))

    #if plot_option == ' ':
    #    print ('Please Select the Plot')

    #elif plot_option == 'Rose Diagram':

    

    year_option = st.sidebar.selectbox('Select the Year',(' ', '2007','2008','2009','2013','2014','2015','2017'))

    #year_option = '2007'
    if year_option == ' ':
        print ('Please Select the Year')

    else:
        rose_diagram_header = 'Rose Diagram for the year: ' + year_option
        st.subheader(rose_diagram_header)

        dfe = analysis.analyze_rose_diagram_data(year_option)
        st.plotly_chart(analysis.get_rose_diagram(dfe), width = 600, height = 600)

        #analysis.get_rose_diagram(dfe).update_layout(width = 900, height = 900)
        #analysis.get_rose_diagram(dfe).show()
        
        time_diagram_header = 'Time Series for the year: ' + year_option
        st.subheader(time_diagram_header)

        st.plotly_chart(analysis.get_time_plot(year_option), width = 1500, height = 600)

        heat_diagram_header = 'Heat Map for the year: ' + year_option
        st.subheader(heat_diagram_header)

        st.plotly_chart(analysis.heat_map_analysis(year_option), width = 1500, height = 800)

        #analysis.get_time_plot(year_option).update_layout(width = 900, height = 1500)
        #analysis.get_time_plot(year_option).show()
        analysis.heat_map_analysis(year_option).show()

if __name__ == "__main__":
    main()

#main()

# C:\Users\khush\github_projects\python_3.7\streamlit C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py

# In Anaconda Terminal - C:\Users\khush> streamlit run C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py 

#https://www.ul.com/apps/wind-data-management-dashboard