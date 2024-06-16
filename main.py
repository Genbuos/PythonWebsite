import streamlit as st


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image("images/e442e74a-1c08-40ea-8a25-ede9bb424a25.jfif", width=300)

    with col2:
        st.title("Jordan Mitchell")
        content = '''Hello! I am a freelance Python Programmer with a specialty in AWS cloud computing. I graduated 
        in 2024 from Wilmington University with a Undergraduate Certificate in Web App Development.'''
        st.info(content)