import streamlit as st

st.title("Git Tutorial")
st.subheader("All In One")

col1, col2, col3 = st.columns(3)

with col1:
    st.text_input("Username")

with col2:
    st.text_input("Password", type="password")

with col3:
    st.button(label="Submit")

print("This is V4")
print("This is V5")

print("Added as part of new october25 branch")
