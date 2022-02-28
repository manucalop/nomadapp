

# Imports
import streamlit as st
import function_streamlit as ft


# Page settings
ft.config_page()

# Cache
st.cache(suppress_st_warning=True)

# Sidebar - Menu
menu = st.sidebar.selectbox('Menu',
    ['Home', 'Travel'])

if menu == 'Home':
    ft.home()
elif menu == 'Travel':
    ft.travel()


