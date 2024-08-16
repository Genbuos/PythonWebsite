import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image("images/1718722988499.jfif", width=400)

with col2:
    st.title("Jordan Mitchell")
    content = '''Hello! I am a freelance Python Programmer with a specialty in AWS cloud computing. I graduated 
in 2024 from Wilmington University with a Undergraduate Certificate in Web App Development.'''
    st.info(content)
st.write("Below are some projects that I have worked on. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

