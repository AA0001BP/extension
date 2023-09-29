import streamlit as st

st.title("My Streamlit App")

# Embed Chrome Extension using an iframe
st.markdown('<iframe src="chrome://extensions/?id=phjbepamfhjgjdgmbhmfflhnlohldchb" width="800" height="600"></iframe>', unsafe_allow_html=True)
