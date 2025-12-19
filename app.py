import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Blockchain Voting DApp",
    layout="wide"
)

st.title("🗳️ Blockchain Voting DApp (Streamlit)")

# Đọc file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Nhúng HTML vào Streamlit
components.html(
    html_code,
    height=1200,
    scrolling=True
)
