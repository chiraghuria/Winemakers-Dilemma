import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image



def insert_sliders():
    with st.sidebar:
        st.markdown("## Choose your values here\n")
        st.markdown("##### % Chance of High Sugar: ")
        high_sugar = st.slider(label="", min_value=1, max_value=100)
        st.markdown("##### % Chance of Typical Sugar: ")
        typical_sugar = st.slider(label=" ", min_value=1, max_value=100)
        st.markdown("##### % Chance of No Sugar: ")
        no_sugar = st.slider(label="  ", min_value=1, max_value=100)
        st.markdown("##### % Chance of Botrytis: ")
        botrytis = st.slider(label="   ", min_value=1, max_value=100)
        return high_sugar, typical_sugar, no_sugar, botrytis
        


def insert_image(file):
    image = Image.open(file)
    np_image = np.asarray(image)
    st.image(np_image, width=200)


def insert_app_info():
    insert_image('image/wine.png')
    st.title("Winemakers Dilemma: Assignment 3")
    st.markdown("## Machine Learning in Practice, Spring 2022")
    st.markdown("##### Developed by Chirag Huria")
    
def calc_evalue(high_sugar, typical_sugar, no_sugar, botrytis):
    with st.sidebar:
        p_ds = 0.65*((botrytis/100)*3300000 + 0.9*420000) + 0.35*((no_sugar/100)*960000 + (typical_sugar/100)*1410000 + (high_sugar/100)*1500000) 
        p_dns = 0.81*((no_sugar/100)*960000 + (typical_sugar/100)*1410000 + (high_sugar/100)*1500000) + 0.19*((botrytis/100)*3300000 + 0.9*420000)
        e_value = 0.23* (p_ds) + 0.77*(p_dns)
        return e_value


def print_results(e_value):
    st.success(f'EV = {e_value}')
    if e_value > 960000:
        st.success(f'Recommendation: Buy Clairvoyance')
    else:
        st.error(f'Recommendation: Do Not Buy Clairvoyance')
    
def main():
    insert_app_info()
    high_sugar, typical_sugar, no_sugar, botrytis = insert_sliders()
    if st.sidebar.button('Calculate Expected Value'):
        e_value = calc_evalue(high_sugar, typical_sugar, no_sugar, botrytis)
        print_results(e_value)

if __name__ == '__main__':
    main()

    
    
    

    



   
    