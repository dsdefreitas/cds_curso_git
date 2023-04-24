import pandas as pd 
import streamlit as st 
import numpy as np 

def load_data(): 
    return pd.read_csv("C:\\Users\\Matheus\\repos\\curso_git\\projeto\\data\\processed\\bikes_completed.csv")

def main(): 
    
    df = load_data()

    st.dataframe(df)

if __name__ == '__main__': 
    main() 

