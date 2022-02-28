

import streamlit as st
import pandas as pd


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
    st.markdown('# NomadApp')
    st.markdown('Welcome to NomadApp!')


# User filters
user_filters = ('leisure',
                'activities',
                'schools',
                'beach/mountain',
                'co-working')


def on_click_info_button(filters: dict):
    """
    Receives a dictionary of the selected parameters by the user.
    This information will be used to make the request to Google API.

    Params:
        - filters: dict expected
    Return:
        - filters: dict, parameters to make the request
    Raises:
        - TypeError if 'filters' type is not dict
    """
    if isinstance(filters, dict):
        # TEST
        st.markdown('## FILTERS SELECTED:')
        for filter_type, boolean in filters.items():
            if filter_type == 'radio':
                st.markdown(f'#### Selected Radio: {boolean} km')
            elif boolean:
                st.markdown(f'#### {filter_type.capitalize()}')
        # return filters
    else:
        raise TypeError(f'Dict expected, received {type(filters)}.')

    df = pd.DataFrame({'lat': [40.4279488, ],
                       'lon': [-3.68675]})

    st.map(df)

def output(data=None):
    """
    When the user press the 'info_button', this function is activated.
    Receives data from the Google API, and display the requested results
    in the Streamlit app.

    Params:
        - data
    """
    pass


# Travel
def travel():
    st.text_input('Search your address here')
    st.sidebar.markdown('### Filters:')

    leisure = st.sidebar.checkbox('Leisure')
    activities = st.sidebar.checkbox('Activities')
    schools = st.sidebar.checkbox('Schools')
    beach_mountain = st.sidebar.checkbox('Beach-Mountain')
    co_working = st.sidebar.checkbox('CoWorking')
    st.sidebar.markdown('\n')
    radio = st.sidebar.slider('Choose the radio (in km)',
                              1, 10)
    st.sidebar.markdown('\n\n\n\n')

    # Filters Dict
    filters_dict = {
        'leisures': False,
        'activities': False,
        'schools': False,
        'beach_mountain': False,
        'coworking': False,
        'radio': radio}

    if leisure:
        filters_dict['leisures'] = True
    if activities:
        filters_dict['activities'] = True
    if schools:
        filters_dict['schools'] = True
    if beach_mountain:
        filters_dict['beach_mountain'] = True
    if co_working:
        filters_dict['coworking'] = True


    info_button = st.sidebar.button(label='Get Info',
                                    help='Press to get your selected info')

    if info_button:
        on_click_info_button(filters_dict)

