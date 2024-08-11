import streamlit as st 

#------------about page---------

about_page = st.Page(
    page = 'pages/about_me.py',
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,
)

project_1_page = st.Page(
    page = "pages/chatbot.py",
    title ="Chat Bot",
    icon = ":material/smart_toy:",
)



#-------------Navigation setup-------------

pg = st.navigation(
    {
        "Info":[about_page],
        "Projects" : [project_1_page],
    }   
)


#--------------Shared on All pages-----------
st.logo("assets/logo1.jpg")
st.sidebar.text("Made with ❤️ By Ahmed")
#------------Run Navigation-------------

pg.run()