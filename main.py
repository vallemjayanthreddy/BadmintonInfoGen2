import streamlit as st
import langchainhelper
st.title("Badminton Information")
country_name = st.sidebar.selectbox("Pick a country",("China","France","Indonesia","Malaysia","Denmark","Japan","Korea","India","Thailand",))

if(country_name):
    response = langchainhelper.generate_storename_and_storeitems(country_name)
    st.header(response['store_name'])
    list_of_items = response['store_items'].strip().split(",")
    st.write("**Players**")
    for item in list_of_items:
        st.write(item)