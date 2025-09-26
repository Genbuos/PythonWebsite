import streamlit as st
import pandas

st.set_page_config(layout='wide')


# Register model-viewer web component globally at the top
st.markdown(
    '<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>',
    unsafe_allow_html=True
)

# Add a refresh button for development
if st.button('🔄 Refresh'):
    st.rerun()

# Add custom CSS for project buttons (Source Code and Website only)
st.markdown(
    """
    <style>
    .project-btn {
        display: inline-block;
        padding: 0.5em 1.2em;
        margin: 0.5em 0.3em 0.5em 0;
        font-size: 1em;
        color: #fff !important;
        border: none;
        border-radius: 6px;
        text-decoration: none;
        transition: background 0.2s;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }
    .source-btn { background: #0072E3; }
    .source-btn:hover { background: #005bb5; }
    .website-btn { background: #28a745; }
    .website-btn:hover { background: #1e7e34; }
    .project-card {
        border-radius: 10px;
        padding: 1em 1em 0.5em 1em;
        margin-bottom: 1em;
        min-height: 420px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .project-card .project-btn { margin-bottom: 0; }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.image("images/RED EYES WOLF - STARFLESH CORE.jfif", width=450)

with col2:
    st.title("Jordan Mitchell")
    content = '''Hello! I am a Python Programmer with a specialty in AWS cloud computing. This site showcases my 
    skills with python and other languages. In my journey to become a developer of software, I have learned to create the following projects below.'''
    st.info(content)



df = pandas.read_csv("data.csv", sep=";")



num_cols = 4
num_rows = 5
total_cells = num_cols * num_rows

for row_idx in range(num_rows):
    cols = st.columns(num_cols)
    for col_idx in range(num_cols):
        proj_idx = row_idx * num_cols + col_idx
        if proj_idx >= len(df):
            continue
        with cols[col_idx]:
            row = df.iloc[proj_idx]
            st.header(row['title'])
            st.write(row['description'])
            # Render .glb model for the first project, otherwise show image
            if proj_idx == 0:
                st.markdown(
                    '<iframe src="http://localhost:8000/test.html" width="100%" height="350" frameborder="0" scrolling="no"></iframe>',
                    unsafe_allow_html=True
                )
            elif row['title'].lower().startswith('portfolio'):
                st.markdown(
                    '<iframe src="http://localhost:8000/portfolio_preview.html" width="100%" height="350" frameborder="0" scrolling="no"></iframe>',
                    unsafe_allow_html=True
                )
            elif row['title'].lower().startswith('food'):
                st.markdown(
                    '<iframe src="http://localhost:8000/foodtrax.html" width="100%" height="350" frameborder="0" scrolling="no"></iframe>',
                    unsafe_allow_html=True
                )
            else:
                st.image("images/" + str(row['image']))
            
            # Show buttons based on project - hide website button for Bank Application
            if row['title'].lower().startswith('bank'):
                # Only show Source Code button for Bank Application
                st.markdown(
                    f'<a href="{row["url"]}" class="project-btn source-btn" target="_blank">Source Code</a>',
                    unsafe_allow_html=True
                )
            else:
                # Show both buttons for other projects
                st.markdown(
                    f'<a href="{row["url"]}" class="project-btn source-btn" target="_blank">Source Code</a>'
                    f'<a href="{row["website_url"]}" class="project-btn website-btn" target="_blank">Website</a>',
                    unsafe_allow_html=True
                )
                if not row["website_url"] or row["website_url"] == "#":
                    st.warning("Website not running!")
            st.markdown('</div>', unsafe_allow_html=True)

