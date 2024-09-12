import streamlit as st

with st.sidebar:
    st.title('Settings :gear:')
    st.write('You can use this sidebar to change the settings')
    llm_models = st.selectbox('Select a model', ['gpt-4o', 'llama3', 'mistral'])
    if llm_models == 'gpt-4o':
        temperature = st.slider('Select a temperature', 0.0, 1.0, 0.5)
        
st.title('Storymodelers Narrative Characterization')

