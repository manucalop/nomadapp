

import streamlit as st


# Main page settings
def config_page():
    st.set_page_config(
        page_title='NomadApp',
        layout='wide'
    )


# Cache
st.cache(suppress_st_warning=True)


# Home
def home():
    # Title
    st.markdown('# NomadApp')
    st.markdown('Manu!')

