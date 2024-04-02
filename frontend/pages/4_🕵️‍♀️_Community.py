import streamlit as st
import pandas as pd
import numpy as np
import controller as ct

# Define some HTML templates for displaying the posts
title_temp = """
<div style="background-color:#CEFAF6;padding:10px;border-radius:10px;margin:40px;">
<h4 style="color:black;text-align:center;">{}</h4>
<h4 style="color:black;text-align:center;">{}</h6>
<p style="color:black;text-align:center;">Author: {}</p>
</div>

"""

st.set_page_config(layout="wide", page_title="Comunnity")

st.write("## Community")
st.write(
    ":bug: Record your findings, information, curiosities in this blog so that the entire community is aware. :spiral_note_pad:"
)

def show_comunity_page():
    posts = ct.get_all_blogs()
    # Display each post as a card
    for post in posts:
        st.markdown(title_temp.format(post[1], post[2], post[0]), unsafe_allow_html=True)


    st.sidebar.write(f"{st.session_state.userN}, here you can add a new post to the blog.")
    # Create a form to get the post details
    with st.sidebar.form(key="add_form"):
        #author = st.text_input("Author")
        title = st.text_input("Title")
        content = st.text_area("Content")
        submit = st.form_submit_button("Submit")
    # If the form is submitted, add the post to the database
    if submit:
        ct.insertRowBlog(st.session_state.userN,title,content)
        st.sidebar.success("Post added successfully")
        show_comunity_page.empty()

if st.session_state['loggedIn']:
    show_comunity_page()
else:        
    st.write("To access this functionality you must log in.")