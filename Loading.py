import streamlit as st
import time

st.title("Loading")

with st.spinner("🧬 processing..."):
    time.sleep(3)

st.switch_page("pages/Result.py")