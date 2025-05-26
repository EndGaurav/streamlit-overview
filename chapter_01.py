import streamlit as st

st.title("Hello chai App")
st.subheader("brewed with streamlit")
st.text("Welcome to your interactive App")
st.write("Choose you fav. varity of chai")

some = st.selectbox("Select your fav. IPL team", ["RCB", "RR", "LSG", "SRH"])

st.write(f"Your choice is {some} which is not bad.")

st.success(f"{some} Selected✅")
