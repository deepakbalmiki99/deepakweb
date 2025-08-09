# import streamlit as st

# st.title("Hello -- Welcome to my Page")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
from streamlit.components.v1 import html
import pathlib

# --- Page config & title
#st.set_page_config(page_title="Embed HTML Demo", layout="centered")
#st.title("Embedding an External HTML File")

# --- Read your HTML file
html_path = pathlib.Path(__file__).parent / "page.html"
raw_html  = html_path.read_text(encoding="utf-8")

# --- Embed!
#height controls the iframe height, scrolling=True adds scrollbars if needed
html(raw_html,width=1600, height=1200, scrolling=True)

# --- Fallback link
# st.markdown(
#     "[Or view the raw HTML here](./page.html)",
#     unsafe_allow_html=True
# )
