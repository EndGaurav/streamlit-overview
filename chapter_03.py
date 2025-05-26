import streamlit as st
import time


side = st.sidebar.title("Pay attention")
name = st.sidebar.text_input("Enter your name")

if name:
    some = st.success("Thank you " + name + " for coming to vote")
    time.sleep(1)
    some.empty()
    st.header("Vote for your favourite chai")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Masala Chai")
        vote1 = st.button("Vote Masala chai")    

    with col2:
        st.header("Adark Chai")
        vote2 = st.button("Vote Adark chai")    
        

    if vote1:
        st.success("You voted for Masala Chai")
    elif vote2:
        st.success("You voted for Adrak Chai")
    else:
        st.warning("Please vote")
        
    with st.expander("Show chai making instructions"):
        st.write("""
                 1. Boil water
                 2. Add milk
                 3. Add Masala
                 4. Mix well
                 5. Serve hot
                    """)