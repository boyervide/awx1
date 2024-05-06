import streamlit as st
error = st.alert("This is error alert.", title="Error", type="error", icon="🚨")
if st.button("Open alert error", key="third_spec_alert_button"):
    error.open()
