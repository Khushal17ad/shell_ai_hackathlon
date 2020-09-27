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
    #st.subheader("Year Wise Analysis")

    #st.dataframe(analysis.get_data()) 

    data = analysis.get_data()
    data['sped'] = pd.to_numeric(data['sped'])
    bins = [*range(0, 50, 7)] 
    data['speed_bins'] = pd.cut(data['sped'], bins)
    
    st.subheader("Rose Diagram")
    st.plotly_chart(analysis.get_rose_diagram(data), width = 900, height = 900)

    analysis.get_rose_diagram(data).update_layout(width = 900, height = 900)
    analysis.get_rose_diagram(data).show()

if __name__ == "__main__":
    main()




# C:\Users\khush\github_projects\python_3.7\streamlit C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py

# In Anaconda Terminal - C:\Users\khush> streamlit run C:\Users\khush\github_projects\machine_learning\supervised_unsupervised_learning\unsupervised.py 