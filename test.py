import streamlit as st


st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Just some text")
st.markdown("**Bold**, *Italic*, `Code`")



hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_link__1S137 {display: none;}
    </style>
"""

st.markdown(hide_footer_style, unsafe_allow_html=True)



##GANTI DIKIT


