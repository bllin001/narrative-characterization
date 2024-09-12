import streamlit as st
from dotenv import load_dotenv, find_dotenv
import json

with st.sidebar:
    st.title('Settings :gear:')
    st.write('You can use this sidebar to change the settings')
    llm_models = st.selectbox('Select a model', ['gpt-4o', 'llama3', 'mistral'])
    if llm_models == 'gpt-4o':
        temperature = st.slider('Select a temperature', 0.0, 1.0, 0.5)
        
st.title('Storymodelers Narrative Characterization')
st.write('This app characterizes narratives into actors, factors, and mechanisms. Actors can range from governmental bodies to grassroots movements, each playing a distinct role in the narrative construction. Factors encompass socioeconomic, cultural, and environmental variables, while mechanisms refer to processes or actions taken to generate events, analyze a text, and extract the actors, factors, and mechanisms.')

st.write('---')

st.write('Please enter the text you would like to analyze:')
text = st.text_area('Text')
if text != '':
    st.write('---')
    st.write('You entered:')
    st.write(text)
    st.write('---')
    st.write('Please click the button below to analyze the text:')
    if st.button('Analyze'):
        st.write('---')
        st.write('Analysis:')
        st.write('---')
        st.write('Actors, Factors, and Mechanisms:')
        st.write('---')
        st.write('Actors:')
        st.write('---')
        st.write('Factors:')
        st.write('---')
        st.write('Mechanisms:')