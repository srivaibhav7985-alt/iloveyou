import streamlit as st

st.set_page_config(page_title="For Shrejal 🌸", page_icon="🌸", layout="wide")

st.markdown("""
<style>
header[data-testid="stHeader"] { display: none; }
.stApp > div { padding: 0 !important; }
footer { display: none; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1200, scrolling=True)
