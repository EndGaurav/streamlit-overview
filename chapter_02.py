import streamlit as st
import datetime

st.title("Chai Maker App")

if st.button("Make chai"):
    st.success("Your chai is being brewed")

# Controlled Input
isChecked = st.checkbox("Add masala")
print("isChecked: ", isChecked)
if isChecked:
    st.write("Masala added to your chai")
    
selectedBase = st.radio("Pick your chai base", ["Milk", "Water", "Honey"])
st.write(f"Selected base {selectedBase}")

selectedFlavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"Selected base {selectedFlavour}")

sugarSpoon = st.slider("Sugar level: ", 0, 10, 2, 2 )
st.write(f"Sugar level spoon {sugarSpoon}")


# Uncontrolled Input
cups = st.number_input("How many cups: ", 1, 10, 1, 1)
st.write(f"Number of cups {cups}")

name = st.text_input("Enter your name")
if name : 
    st.write(f"Welcome {name}, Your chai is on the way")


dob = st.date_input("Select your date of birth", datetime.date(2002, 1, 1))
today = datetime.date.today()
st.write(f"Your age {today.year - dob.year}")
