import streamlit as st 
from Form.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contant_form():
    contact_form()
    

# --------------Hero Section--------------
col1, col2 = st.columns(2, gap= "small", vertical_alignment="center")

with col1:
    st.image("./assets/Ahmed log.jpg", width = 200)
    
with col2:
    st.title("Ahmed Islam", anchor= False)
    st.write(
        """
        Deep Learning Intern at Itsolera Company, \n
        Alpha MLSA,
        IBM Machine Learning Specialization
        """
    )
    
    if st.button("💌 Contact Me"):
        show_contant_form()
        
        
#--------------Experience & Qualification------------

st.write("\n")
st.subheader("Experience & Qualification", anchor = False)

st.write(
    """
    - Student of BS Computer Science 
    - 1 Year Experience in the Field of Artificial Intelligence
    - Strong Hands-on Experience and Knowledge in Python
    - Excellent team-player and displaying a strong sense of initiative task
    """
)

#--------------------skills--------------

st.write('\n')
st.subheader("Hard Skills", anchor = False)
st.write(
    """
    - Programming: Python(Scikit-learn, Pandas, Numpy, Tensorflow, Seaborn, Matplotlib)
    - Data Visualization: PowerBI, Ms Excel, Plotly 
    - Modeling: Logistic Regression, Linear Regression, Decision Tree, Neural Networks, Transfer Learning
    - Tools: Photoshop, Canva, Lightroom, Discord, Slack
    - Databases: MySQL
    """
)        
        
